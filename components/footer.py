"""
Module/Script Name: footer.py
Author: M. W. Hefner

Created: 7/07/2023
Last Modified: 7/12/2023

Project: RIEEE DataDash
Project Version Id: 1.0

Script Description: This script defines the style, layout, and callback functionality of the footer.

Exceptional notes about this script:

TODO: Write an appropriate footer!

Callback methods: 0

~~~

This Dash application component was created using the template provided by the Research Institute for Environment, Energy, and Economics at Appalachian State University.

"""

# Component ID (Should be the same as the title of this file)
component_id = "footer"

# Import Dependencies
import dash.html.Div
import components.utils.constants as d

# import components.examplesubcomponent as examplesubcomponent

# STYLES (CSS DICT)
styles = {
    # CSS Dictionary goes here.
    'component' : {
        'display' : 'flex',
        'flex-flow' : 'row nowrap',
        'justify-content' : 'space-around',
        'align-items' : 'center',

        # Appearance
        'box-sizing' : 'border-box',
        'margin': '0 auto',
        'width' : '100%',
        'padding' : '30px',
        'padding-bottom' : '0px',
        'border-top-left-radius': '50px',
        'border-top-right-radius': '50px',
        'background-image' : 'linear-gradient(to right, rgba(255, 255, 255, 1), rgba(255, 255, 255, 0.75)',
        'margin-top' : '0px',
    },

    'h1' : {
        'text-align' : 'center'
    },

    'left-footer' : {
        'margin' : '20px',
    },

    'right-footer' : {
        
    },
}

# LAYOUT
layout = dash.html.Div(
    id = component_id,
    style = styles['component'],
    title = "Welcome to RIEEE's DataDash",
    children= [
        dash.html.Div(
            
            style = styles['left-footer'],

            children = [
                dash.html.Img(src = "./assets/images/RIEEE_LOGO.svg", height = 200)
            ]
        ),
        dash.html.Div(

            style = styles['right-footer'],

            children = [
                dash.dcc.Markdown(children = d.footer_markdown, style={'text-align' : 'right'})
            ]
        ),
    ]
)

# CALLBACKS (0)
