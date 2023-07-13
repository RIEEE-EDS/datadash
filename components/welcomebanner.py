"""
Module/Script Name: welcomebanner.py
Author: M. W. Hefner

Created: 7/07/2023
Last Modified: 7/13/2023

Project: RIEEE DataDash
Project Version Id: 1.0

Script Description: This script defines the style, layout, and callback functionality of the welcomebanner.

Exceptional notes about this script:
(none)

Callback methods: 0

~~~

This Dash application component was created using the template provided by the Research Institute for Environment, Energy, and Economics at Appalachian State University.

"""

# Component ID (Should be the same as the title of this file)
component_id = "welcomebanner"

# Import Dependencies
import dash.html.Div
# import components.examplesubcomponent as examplesubcomponent
import components.utils.constants as d

# STYLES (CSS DICT)
styles = {
    # CSS Dictionary goes here.
    'component' : {
        # Display Behavior
        'display' : 'flex',
        'flex-flow' : 'row nowrap',
        'justify-content' : 'space-around',
        'align-items' : 'center',

        # Appearance
        'margin': '0 auto',
        'width' : '100%',
        'padding' : '30px',
        'box-sizing' : 'border-box',
        'border-bottom-left-radius': '50px',
        'border-bottom-right-radius': '10px',
        'border-top-left-radius': '10px',
        'border-top-right-radius': '50px',
        'background-image' : 'linear-gradient(to right, rgba(255, 255, 255, 1), rgba(255, 255, 255, 0.75)',
        'margin-top' : '40px',
        'margin-bottom' : '40px'

    },

    'h1' : {
        'text-align' : 'center',
        'margin' : '10px',
    },

    'left-welcome-banner' : {
        'margin' : '20px',
    },

    'right-welcome-banner' : {
        'margin' : '20px',
    },

}

# LAYOUT
layout = dash.html.Div(
    id = component_id,
    style = styles['component'],
    title = "Welcome to RIEEE's DataDash",
    children= [

        # Left Welcome Banner

        dash.html.Div(
            
            style = styles['left-welcome-banner'],

            children = [
                dash.html.Img(src = "./assets/images/RIEEE_LOGO.svg", height=300)
            ]
        ),

        # Right Welcome Banner

        dash.html.Div(

            style = styles['right-welcome-banner'],

            children = [
                dash.html.H1("Discover RIEEE's DataDash", style = styles['h1']),

                # Load in Welcome banner markdown.
                dash.dcc.Markdown(

                    children = d.welcomebanner_markdown, 

                    style = {
                        'text-align' : 'center', 
                        'overflow-y' : 'auto', 
                        'margin' : '0px', 
                        'font-size' : '20px'
                    }
                )
            ]
        ),
    ]
)

# CALLBACKS (0)
