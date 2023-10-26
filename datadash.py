"""
Module/Script Name: datadash.py
Author: M. W. Hefner

Created: 7/01/2023
Last Modified: 7/05/2023

Project: RIEEE DataDash
Project Version Id: 1.0

Script Description: This script initializes the dash application for development on a local machine. 

Exceptional notes about this script:

1. This script is for development on a local machine: after loading into a python environment with the dependencies in requirements.txt, found in this directory, installed, run this script to run the application server on local host at port 8050.

2. While there is at least one external style sheet, most styling is intentionally left in python just to keep things mostly unilingual.  Unfortunately this does limit the ability of certain IDEs' ability to assist and debug.

Callback methods: 0

~~~

This Dash application was created using the template provided by the Research Institute for Environment, Energy, and Economics at Appalachian State University.

"""

# !!! IMPORTANT: CHANGE TO FALSE BEFORE PUSHING !!!
LOCAL_DEVELOPMENT = True
# !!! IMPORTANT: CHANGE TO FALSE BEFORE PUSHING !!!

# Import Dependencies
import dash
import components.maincontainer as mc
import components.utils.login as login
from components.utils.config import cfg

# Import Styles that _have_ to be CSS;
external_stylesheets = [
    "./assets/externalstylesheets/dynamic_styling.css"
]

# Initialize Dash Application
app = dash.Dash(
    __name__, 
    external_stylesheets = external_stylesheets,
    title = "RIEEE | DataDash",
    update_title = None,
    url_base_pathname = cfg.get('app', 'url_prefix', fallback='/'),
    suppress_callback_exceptions=True,
)

# Define Application Layout
app.layout = dash.html.Div(
    children = [
        # A location object tracks the address bar url
        dash.dcc.Location(id='url'),

        # Used to prevent cacheing of authorization
        dash.dcc.Store(id='authorization-anti-memorization'),

        # Secure div holder for main container
        dash.html.Div(id='secure-div')
    ],
)

# Checks to see if the user is authorized and returns 
# the main container as the app layout, passing it
# user credentials.
#
# This is called any time there is a change to the url.
#
# The second output is to provide a place to include
# "no_update" as an output.  Dash does not memorize 
# callbacks whose output contains "no_update."
@dash.callback(
    dash.Output('secure-div', 'children'),
    dash.Output('authorization-anti-memorization', 'data'),
    dash.Input('url', 'pathname')
)
def authorize(pathname):

    # Grab http request header metadata
    shibbInfo = login.userAuthentication()

    # Is the user signed in through shibboleth? (bool)
    userSignedIn = shibbInfo[0]

    # Username or None
    UID = shibbInfo[1]

    # DataDash user role from application metadata on the data server or None
    userRole = shibbInfo[2]

    if LOCAL_DEVELOPMENT:
        # For local development, return an admin view
        return mc.layout(True, "LOCAL_DEVELOPER", "ADMIN"), dash.no_update
    
    else:
        # Return the main container layout, passing it user credentials.
        return mc.layout(userSignedIn, UID, userRole), dash.no_update

# Main script execution for (local development only)
if __name__ == '__main__' and LOCAL_DEVELOPMENT:
    # True for hot reloading (leave True)
    app.run_server(debug = True)

# WSGI Entry Pointer (Used in deployment)
server = app.server
