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

# STYLES (CSS DICT)
styles = {
    # CSS Dictionary goes here.  Format:
    # 'css-example-attribute' : 'value',
    'component' : {
        'display': 'flex',
        'flex-direction': 'row',
        'align-items': 'center',
        'justify-content': 'flex-end',  # Change to right-justify
        'max-width': '400px',
        'flex': '1 1 auto',
    },

    'login-link': {
        'color': '#FFF',
    }
}

# SIGN ON/SIGN OFF
def authorizedContent(userIsSignedIn, UID) :
    if userIsSignedIn :
        return [
            dash.html.P("Welcome, " + UID + "."),
            dash.html.Img(
                src="./assets/icons/id_GOLD.png", 
                title = "You are logged in as " + UID, 
                style = {
                    'height' : '32px', 
                    'margin-left' : '10px', 
                    'margin-right' : '10px'
                    }), # Info icon set to H1 Height
            dash.html.A("  Logout", title = "Click here to logout.", href="/Shibboleth.sso/Logout", style = styles['login-link'])
        ]
    else :
        return [
            dash.html.P("Public View"),
            dash.html.Img(
                src="./assets/icons/international_GOLD.png", 
                title = "DataDash Public View", 
                style = {
                    'height' : '32px', 
                    'margin-left' : '10px', 
                    'margin-right' : '10px'
                    }), # Info icon set to H1 Height
            dash.html.A("  Shibboleth Login", title = "Click here to log in.", href="/Shibboleth.sso/Login", style = styles['login-link'])
        ]

# LAYOUT is dynamic
def layout(userIsSignedIn, UID) :
    return dash.html.Div(
        id = component_id,
        style = styles["component"],
        children = authorizedContent(userIsSignedIn, UID)
    )

# CALLBACKS (0)
