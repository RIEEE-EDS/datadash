"""
Module/Script Name: east.py
Author: M. W. Hefner

Created: 7/01/2023
Last Modified: 7/05/2023

Project: RIEEE DataDash
Project Version Id: 1.0

Script Description: This script defines the style, layout, and callback functionality of the eastern element of the header.

Exceptional notes about this script:
(none)

Callback methods: 0

~~~

This Dash application component was created using the template provided by the Research Institute for Environment, Energy, and Economics at Appalachian State University.

"""

# Component ID (Should be the same as the title of this file)
component_id = "east"

# Import Dependencies
import dash.html.Div
# import components.examplesubcomponent as examplesubcomponent
import components.utils.login as login

# STYLES (CSS DICT)
styles = {
    # CSS Dictionary goes here.  Format:
    # 'css-example-attribute' : 'value',
    'component' : {
        'display' : 'flex',
        'flex-flow' : 'row no-wrap',
        'align-items' : 'center',
        'justify-content' : 'space-between',
        'max-width' : '300px',
        'flex': '1 1 auto'  # This line is added
    },

    'login-link' : {
        'color' : '#FFF',
    }
}

# Define behavior on whether or not someone is logged in through shibboleth
def authorizedContent() :
    if login.loggedIn :
        return [
            dash.html.P("Welcome, " + login.loggedInAs + "."),
            dash.html.Img(src="./assets/icons/id_GOLD.png", title = "You are logged in as " + login.loggedInAs, style = {'height' : '52px'}), # Info icon set to H1 Height
            dash.html.A("Logout", title = "Click here to logout.", href="./", style = styles['login-link'])
        ]
    else :
        return [
            # TODO: Fix login and logout links once we know what to do about shibboleth
            dash.html.P("Public View"),
            dash.html.Img(src="./assets/icons/international_GOLD.png", title = "DataDash Public View", style = {'height' : '52px'}), # Info icon set to H1 Height
            dash.html.A("Shibboleth Login", title = "Click here to log in.", href="./", style = styles['login-link'])
        ]

# LAYOUT
layout = dash.html.Div(
    id = component_id,
    style = styles["component"],
    children = authorizedContent()
)

# CALLBACKS (0)
