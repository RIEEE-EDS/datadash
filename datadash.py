"""
Module/Script Name: datadash.py

Author: M. W. Hefner

Created: 7/01/2023

Last Modified: 10/28/2023

Project: RIEEE DataDash

Last Update Project Version: 1.0.0

Script Description: This script initializes the datadash dash application.

Exceptional notes about this script:

1. This script is for development on a local machine: after loading into a python environment with the dependencies in requirements.txt, found in this directory, installed, run this script to run the application server on local host at port 8050.

2. While there is at least one external style sheet, most styling is intentionally left in python just to keep things mostly unilingual.  Unfortunately this does limit the ability of certain IDEs' ability to assist and debug.

Callback methods: 0

~~~

This Dash application was created using the template provided by the Research Institute for Environment, Energy, and Economics at Appalachian State University.

"""

import os 

if 'REDIS_URL' in os.environ:

    # RUNNING ON SERVER

    LOCAL_DEVELOPMENT = False

else:

    # RUNNING ON A LOCAL MACHINE FOR DEVELOPMENT

    # NOTE: MUST BE CONNECTED TO APP'S VPN FOR THIS TO ACTUALLY DELIVER
    # THE APPLICATION'S CONTENTS TO THE BROWSER.

    LOCAL_DEVELOPMENT = True

# Import Dependencies
import dash
import secrets
import components.maincontainer as mc
import components.utils.login as login
from components.utils.config import cfg

# Import Styles that _have_ to be CSS;
external_stylesheets = [
    "assets/externalstylesheets/styling.css"
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
        # A data component stores a hash to prevent memorization
        dash.dcc.Store(data = secrets.token_hex(), id='memory'),
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
# The second input is to prevent memorization.
@dash.callback(
    dash.Output('secure-div', 'children'),
    dash.Output('memory', 'data'),
    dash.Input('url', 'pathname'),
    dash.State('memory', 'data'),
    cache_timeout = 0
)
def authorize(pathname, hash):

    # DataDash Authorization Token
    authorizationToken = secrets.token_hex()

    # Grab https request header / metadata
    shibbInfo = login.userAuthentication(LOCAL_DEVELOPMENT, hash)

    # Is the user signed in through shibboleth? (bool)
    userSignedIn = shibbInfo[0]

    # Username or None
    UID = shibbInfo[1]

    # DataDash user role from application metadata on the data server or None
    userRole = shibbInfo[2]

    return mc.layout(userSignedIn, UID, userRole), authorizationToken

# Boilerplate index HTML
app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>
'''

# Main script execution for (local development only)
if __name__ == '__main__' and LOCAL_DEVELOPMENT:
    # True for hot reloading
    app.run_server(debug = True)

# WSGI Entry Pointer (Used in deployment)
server = app.server 
