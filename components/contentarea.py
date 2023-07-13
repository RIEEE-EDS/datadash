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
import components.applicationsdisplay.container as app_display
import components.welcomebanner as welcomebanner
import components.footer as footer
import components.utils.constants as d
import components.utils.login as login
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

# Returns a user's role, should they have one.
def get_user_role(username):
    sql = "SELECT user_type FROM Users WHERE username = %s"
    values = (username,)
    sqlconnection.cursor.execute(sql, values)
    result = sqlconnection.cursor.fetchone()
    if result is not None:
        return result[0]
    else:
        return None

# Render different content dependent upon login
def authorizedContent() :
    if login.loggedIn:

        # If logged in, get the user's role
        user_role = get_user_role(login.loggedInAs)

        if user_role is None :
            return [
                # users that have no specified role just see the public dash
                welcomebanner.layout,
                app_display.dynamic_layout("publicdashboards"),
                footer.layout
            ]
        elif user_role == "DEVELOPER" :
            return [
                # users with the developer role can see the applications that "belong" to them
                welcomebanner.layout,
                app_display.dynamic_layout("myapplications"),
                app_display.dynamic_layout("publicdashboards"),
                footer.layout
            ]
        elif user_role == "ADMIN" :
            return [
                # admin users have a special display for backend apps and a display for all apps
                welcomebanner.layout,
                app_display.dynamic_layout("backend"),
                app_display.dynamic_layout("adminall"),
                app_display.dynamic_layout("publicdashboards"),
                footer.layout
                ]
    else :
        # Public Page
        return [
            # If someone is not logged in
            welcomebanner.layout,
            app_display.dynamic_layout("publicdashboards"),
            footer.layout
        ]

# LAYOUT
layout = dash.html.Div(
    id = component_id,
    style = styles['componet'],
    children = authorizedContent()
)

# CALLBACKS (0)
