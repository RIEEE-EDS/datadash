"""
Module/Script Name: containertop.py

Author: M. W. Hefner

Created: 7/01/2023

Last Modified: 10/28/2023

Project: RIEEE DataDash

Last Update Project Version: 1.0.0

Script Description: This script defines the style, layout, and callback functionality of the contentcontainertop.

Exceptional notes about this script:
(none)

Callback methods: 0

~~~

This Dash application component was created using the template provided by the Research Institute for Environment, Energy, and Economics at Appalachian State University.

"""

# Component ID (Should be the same as the title of this file)
component_id = "containertop"

# Import Dependencies
import dash.html
# import components.examplesubcomponent as examplesubcomponent
import components.utils.constants as d

# DYNAMIC LAYOUT (Think of this component as starting here)
def dynamic_layout(application_type, UID) :

    # Get appropriate strings for the different application display area types:
    if (application_type == "publicdashboards") :
        # Display public dashboards
        title = "Public Dashboards"
        information = "These applications are available without a Shibboleth login."
        altxt = information
    elif (application_type == "myapplications") :
        # My Applications
        title = UID + "'s Applications"
        information = "These applications are directly associated with your user account.  Public applications are indicated with a globe icon."
        altxt = information
    elif (application_type == 'backend') :
        # Backend for Admin only
        title = "Backend Applications (Admin View)"
        information = "This application view is for ITS and RIEEE technical administrators only.  Please contact RIEEE if you believe to be viewing this in error."
        altxt = information
    elif (application_type == 'adminall') :
        # All for Admin only
        title = "All Applications (Admin View)"
        information = "This application view is for ITS and RIEEE technical administrators only.  Please contact RIEEE if you believe to be viewing this in error."
        altxt = information
    else :
        title = "Unknown Application Type"
        information = "Something went wrong.  Please contact RIEEE if you believe to be viewing this in error."
        altxt = information

    # Return appropriate heading for the application display
    return dash.html.Div(
    className = "appdisplaycontainertop",
    children = [
        dash.html.H2(title),
        dash.html.Img(src="./assets/icons/information_BW.png", title = information, alt = altxt) # Info icon set to H1 Height
    ]
)

# CALLBACKS (0)
