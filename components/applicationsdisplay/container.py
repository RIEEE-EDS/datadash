"""
Module/Script Name: container.py

Author: M. W. Hefner

Created: 7/01/2023

Last Modified: 10/28/2023

Project: RIEEE DataDash

Last Update Project Version: 1.0.0

Script Description: This script defines application display containers.

Exceptional notes about this script:
(none)

Callback methods: 0

~~~

This Dash application component was created using the template provided by the Research Institute for Environment, Energy, and Economics at Appalachian State University.

"""

# Import Dependencies
import dash.html.Div

# import components.examplesubcomponent as examplesubcomponent
import components.applicationsdisplay.containertop as top
import components.applicationsdisplay.content as content

# DYNAMIC LAYOUT
def dynamic_layout(application_type, UID) :
    return dash.html.Div(
        className = "applicationdisplay",
        children= [
            top.dynamic_layout(application_type, UID),
            content.dynamic_layout(application_type, UID)
        ]
)

# CALLBACKS (0)
