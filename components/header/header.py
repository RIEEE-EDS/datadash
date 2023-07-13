"""
Module/Script Name: header.py
Author: M. W. Hefner

Created: 7/01/2023
Last Modified: 7/05/2023

Project: RIEEE DataDash
Project Version Id: 1.0

Script Description: This script defines the style, layout, and callback functionality of the header.

Exceptional notes about this script:
(none)

Callback methods: 0

~~~

This Dash application component was created using the template provided by the Research Institute for Environment, Energy, and Economics at Appalachian State University.

"""

# Component ID (Should be the same as the title of this file)
component_id = "header"

# Import Dependencies
import dash.html.Div
import components.header.west as west
import components.header.east as east

# import components.examplesubcomponent as examplesubcomponent
import components.utils.constants as d

# STYLES (CSS DICT)
styles = {
    # Header form and position
    'component' : {
        'position': 'fixed',
        'top': '0',
        'left': '0',
        'width': '100%',
        'height' : d.header_height,
        'padding': '15px',
        'box-sizing': 'border-box',
        'z-index': '100',

        # Behavior of elements within header
        'display' : 'flex',
        'flex-flow' : 'row wrap',
        'align-items' : 'center',
        'justify-content' : 'center',
        'overflow-x' : 'hidden',

        # Header style
        'background-color' : '#000000',
        'color' : '#FFF',
        'border-bottom': '3px solid ' + d.appstate_gold
    },

    'inner-header' : {
        # Behavior of elements within header
        'max-width' : d.content_max_width,
        'display' : 'flex',
        'flex': '1 1 auto',  # This line is added
        'flex-flow' : 'row no-wrap',
        'justify-content' : 'space-between',
        'align-items' : 'center',
        'overflow-x' : 'hidden',
        'background-color' : '#000000'
    }
}

# LAYOUT
layout = dash.html.Div(
    id = component_id,
    style = styles['component'],
    children= [

        dash.html.Div(
            style = styles['inner-header'],
            children = [
                # West side header content
                west.layout,

                # East side header content
                east.layout

            ]
        )
    ]
)

# CALLBACKS (0)
