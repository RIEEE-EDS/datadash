"""
Module/Script Name: maincontainer.py
Author: M. W. Hefner

Created: 7/01/2023
Last Modified: 7/05/2023

Project: RIEEE DataDash
Project Version Id: 1.0

Script Description: This script defines the style, layout, and callback functionality of the main container.

Exceptional notes about this script:
(none)

Callback methods: 0

~~~

This Dash application component was created using the template provided by the Research Institute for Environment, Energy, and Economics at Appalachian State University.

"""

# Component ID (Should be the same as the title of this file)
component_id = "maincontainer"

# Import Dependencies
import dash.html
# import components.examplesubcomponent as examplesubcomponent
import components.header.header as header
import components.contentarea as contentarea

# STYLES (CSS DICT)
styles = {
    'component' : {
        'background-position': 'center',  # Center the background image
        'background-size': 'cover',  # Adjust the background image size
        'background-image' : 'url("./assets/images/Stock_4.jpg")',  # Add the path to your image file or provide a URL
        'position': 'fixed',
        'width': '100%',
        'height': '100%',
        'overflow-y' : 'auto'
    }
}

# LAYOUT is dynamic
def layout(userIsSignedIn, UID, userRole) :
    return dash.html.Div(
    id = component_id,
    style = styles['component'],
    children= [
        header.layout(userIsSignedIn, UID),
        contentarea.layout(userIsSignedIn, UID, userRole),
    ]
)

# CALLBACKS (0)
