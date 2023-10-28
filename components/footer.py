"""
Module/Script Name: footer.py

Author: M. W. Hefner

Created: 7/07/2023

Last Modified: 10/28/2023

Project: RIEEE DataDash

Last Update Project Version: 1.0.0

Script Description: This script defines the style, layout, and callback functionality of the footer.

Exceptional notes about this script:

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

# LAYOUT
layout = dash.html.Div(

    id = component_id,

    title = "Welcome to RIEEE's DataDash",

    children= [
        dash.html.Div(
            
            id = "left-footer",

            children = [
                dash.html.Img(src = "./assets/images/RIEEE_LOGO.svg", height = 200)
            ]

        ),
        dash.html.Div(

            children = [
                dash.dcc.Markdown(children = d.footer_markdown, style={'text-align' : 'right'})
            ]
        ),
    ]
)

# CALLBACKS (0)
