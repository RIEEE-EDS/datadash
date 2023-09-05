"""
Module/Script Name: datadash.py
Author: M. W. Hefner

Created: 7/01/2023
Last Modified: 7/05/2023

Project: RIEEE DataDash
Project Version Id: 1.0

Script Description: This script initializes the dash application for development on a local machine. 

Exceptional notes about this script:

1. This script is for development on a local machine: after loading into a python environment with the dependencies in requirements.txt, found in this directory, installed, run this script to run the application server on local host at port 8050.

2. While there is at least one external style sheet, most styling is intentionally left in python just to keep things mostly unilingual.  Unfortunately this does limit the ability of certain IDEs' ability to assist and debug.

Callback methods: 0

~~~

This Dash application was created using the template provided by the Research Institute for Environment, Energy, and Economics at Appalachian State University.

"""

# Import Dependencies
from dash import Dash
import components.maincontainer as mc
from components.utils.config import cfg

# Import Styles that _have_ to be CSS;
external_stylesheets = [
    "./assets/externalstylesheets/dynamic_styling.css"
]

# Initialize Dash Application
app = Dash(
    __name__, 
    external_stylesheets = external_stylesheets,
    title = "RIEEE | DataDash",
    update_title = None,
    url_base_pathname = cfg.get('app', 'url_prefix', fallback='/')
)

# Define Application Layout
app.layout = mc.layout

# Main script execution (Used for running on the local machine for development)
#if __name__ == '__main__':
#    app.run_server(debug = True)

# WSGI Entry Pointer (Used in production deployment)
server = app.server
