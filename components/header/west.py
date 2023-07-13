"""
Module/Script Name: west.py
Author: M. W. Hefner

Created: 7/01/2023
Last Modified: 7/05/2023

Project: RIEEE DataDash
Project Version Id: 1.0

Script Description: This script defines the style, layout, and callback functionality of the western element of the header.

Exceptional notes about this script:
(none)

Callback methods: 0

~~~

This Dash application component was created using the template provided by the Research Institute for Environment, Energy, and Economics at Appalachian State University.

"""

# Component ID (Should be the same as the title of this file)
component_id = "west"

# Import Dependencies
import dash.html
# import components.examplesubcomponent as examplesubcomponent

# STYLES (CSS DICT)
styles = {
    # CSS Dictionary goes here.  Format:
    # 'css-example-attribute' : 'value',
    'component' : {

    }
}

# LAYOUT
layout = dash.html.Div(
    id = component_id,
    style = styles["component"],
    children= [

        dash.html.A(
            href = "https://www.appstate.edu",

            children=[

                dash.html.Img(
                    src="https://www.appstate.edu/_images/_theme/appstate-logo-white-black-600.png",
                    style={"height": "40px"}
                )

            ]

        )

    ]
)

# CALLBACKS (0)
