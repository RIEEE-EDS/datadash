"""
Module/Script Name: welcomebanner.py

Author: M. W. Hefner

Created: 7/07/2023

Last Modified: 10/28/2023

Project: RIEEE DataDash

Last Update Project Version: 1.0.0

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



# LAYOUT
layout = dash.html.Div(
    id = component_id,

    title = "Welcome to RIEEE's DataDash",
    children= [

        # Left Welcome Banner

        dash.html.Div(
            
            id = 'left-welcome-banner',

            children = [
                dash.html.Img(src = "./assets/images/RIEEE_LOGO.svg", height=300)
            ]
        ),

        # Right Welcome Banner

        dash.html.Div(

            id = 'right-welcome-banner',

            children = [
                dash.html.H1("Discover RIEEE DataDash"),

                # Load in Welcome banner markdown.
                dash.dcc.Markdown(

                    children = d.welcomebanner_markdown, 

                    style = {
                        'border-bottom' : '1px solid white',
                        'max-height' : '300px',
                        'overflow-y' : 'auto', 
                        'margin' : '0px', 
                        'font-size' : '18px',
                        'padding' : '15px'
                    }
                )
            ]
        ),
    ]
)

# CALLBACKS (0)
