"""
Module/Script Name: maincontainer.py

Author: M. W. Hefner

Created: 7/01/2023

Last Modified: 10/28/2023

Project: RIEEE DataDash

Project Version Id: 1.0.0

Script Description: This script defines the layout and callback functionality of the main container.

Exceptional notes about this script:
(none)

Callback methods: 0

~~~

This Dash application component was created using the template provided by the Research Institute for Environment, Energy, and Economics at Appalachian State University.

"""

# Component ID (Should be the same as the title of this file)
component_id = "maincontainer"

# Background styling for the image is handled here to avoid cross-origin errors
styles = {
    'component' : {
        'background-position': 'center',  # Center the background image
        'background-size': 'cover',  # Adjust the background image size
        'background-image' : 'url("./assets/images/Stock_4.jpg")',  # Add the path to your image file or provide a URL
    }
}

# Import Dependencies
import dash.html
# import components.examplesubcomponent as examplesubcomponent
import components.header.header as header
import components.contentarea as contentarea

# LAYOUT is dynamic
def layout(userIsSignedIn, UID, userRole) :
    return dash.html.Div(
    id = component_id,
    style=styles['component'],
    children= [

        # Used to achieve that fade effect in the center of the background
        dash.html.Div(
            children = [
                header.layout(userIsSignedIn, UID),
                contentarea.layout(userIsSignedIn, UID, userRole),
            ]
        ),
    ]
)

# CALLBACKS (0)
