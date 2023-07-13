"""
Module/Script Name: container.py
Author: M. W. Hefner

Created: 7/01/2023
Last Modified: 7/05/2023

Project: RIEEE DataDash
Project Version Id: 1.0

Script Description: This script defines the style, layout, and callback functionality of the contentcontainer.

Exceptional notes about this script:
(none)

Callback methods: 0

~~~

This Dash application component was created using the template provided by the Research Institute for Environment, Energy, and Economics at Appalachian State University.

"""

# Component ID (Should be the same as the title of this file)
component_id = "container"

# Import Dependencies
import dash.html.Div

# import components.examplesubcomponent as examplesubcomponent
import components.applicationsdisplay.containertop as top
import components.applicationsdisplay.content as content

# STYLES (CSS DICT)
styles = {
    'component' : {
        'margin': '0 auto',
        'width' : '100%',
        'padding' : '0px',
        'border-top-left-radius': '10px',
        'border-top-right-radius': '10px',
        'border-bottom-left-radius': '25px',
        'border-bottom-right-radius': '25px',

        # This was moved into the content and containertop elements to have a more
        # consistent background for the containertop element
        #'background-image' : 'linear-gradient(to bottom, rgba(0, 0, 0, 0.9), rgba(100, 131, 98, 0.5)',
        'margin-top' : '0px',
        'margin-bottom' : '40px'
    }
}

# DYNAMIC LAYOUT
def dynamic_layout(application_type) :
    return dash.html.Div(
        id = application_type + component_id,
        style = styles['component'],
        children= [
            top.dynamic_layout(application_type),
            content.dynamic_layout(application_type)
        ]
)

# CALLBACKS (0)
