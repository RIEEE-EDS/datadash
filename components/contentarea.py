"""
Module/Script Name: contentarea.py
Author: M. W. Hefner

Created: 7/01/2023
Last Modified: 7/05/2023

Project: RIEEE DataDash
Project Version Id: 1.0

Script Description: This script defines the style, layout, and callback functionality of the contentarea.

Exceptional notes about this script:
(none)

Callback methods: 0

~~~

This Dash application component was created using the template provided by the Research Institute for Environment, Energy, and Economics at Appalachian State University.

"""

# Component ID (Should be the same as the title of this file)
component_id = "contentarea"

# Import Dependencies
import dash.html
# import components.examplesubcomponent as examplesubcomponent
import components.applicationsdisplay.container as applications_container
import components.welcomebanner as welcomebanner
import components.footer as footer
import components.utils.constants as d
import components.utils.sqlconnection as sqlconnection

# STYLES (CSS DICT)
styles = {
    'componet' : {
        'max-width': str(d.content_max_width) + "px",
        'height' : '100%',
        'margin': '0 auto',
        'padding-top': d.header_height,

        # organize application display containers and other content
        'display' : 'flex',
        'flex-direction' : 'column',
        'align-tiems' : 'center',
        'overflow-y' : 'visible'
    }
}



# Render different content dependent upon login
def authorizedContent(userIsSignedIn, UID, userRole) :

    if userIsSignedIn:

        if userRole is None :
            return [
                # users that have no specified role just see the public dash
                welcomebanner.layout,
                applications_container.dynamic_layout("publicdashboards", UID),
                footer.layout
            ]
        
        elif userRole == "DEVELOPER" :
            return [
                # users with the developer role can see the applications that "belong" to them
                welcomebanner.layout,
                applications_container.dynamic_layout("myapplications", UID),
                applications_container.dynamic_layout("publicdashboards", UID),
                footer.layout
            ]
        
        elif userRole == "ADMIN" :
            return [
                # admin users have a special display for backend apps and a display for all apps
                welcomebanner.layout,
                applications_container.dynamic_layout("backend", UID),
                applications_container.dynamic_layout("adminall", UID),
                applications_container.dynamic_layout("publicdashboards", UID),
                footer.layout
                ]
        
    else :

        # Public Page
        return [
            # If someone is not logged in
            welcomebanner.layout,
            applications_container.dynamic_layout("publicdashboards", UID),
            footer.layout
        ]

# LAYOUT is dynamic
def layout(userIsSignedIn, UID, userRole) :
    return dash.html.Div(
        id = component_id,
        style = styles['componet'],
        children = authorizedContent(userIsSignedIn, UID, userRole)
    )

# CALLBACKS (0)
