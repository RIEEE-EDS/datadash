"""
Module/Script Name: content.py
Author: M. W. Hefner

Created: 7/01/2023
Last Modified: 7/10/2023

Project: RIEEE DataDash
Project Version Id: 1.0

Script Description: This script defines the style, layout, and callback functionality of the content.

Exceptional notes about this script:
(none)

Callback methods: 0

~~~

This Dash application component was created using the template provided by the Research Institute for Environment, Energy, and Economics at Appalachian State University.

"""

# Component ID (Should be the same as the title of this file)
component_id = "content"

# Import Dependencies
import dash.html.Div
# import components.examplesubcomponent as examplesubcomponent
import components.utils.sqlconnection as sqlconnection
import components.utils.constants as d

# STYLES (CSS DICT)
styles = {
    # CSS Dictionary goes here.
    'component' : {
        'display': 'flex',
        'flex-wrap': 'wrap',
        'justify-content': 'center',
        'align-items': 'flex-start',
        'padding' : str(d.application_display_padding) + 'px',
        'background-image' : 'linear-gradient(to right, rgba(255, 255, 255, 0.9), rgba(255, 255, 255, 0.7)',
        'border-bottom-left-radius': '25px',
        'border-bottom-right-radius': '25px',
    },

    # Top inner thumbnail
    'h3' : {
        'color' : 'black',
        'background-image' : 'linear-gradient(to top, rgba(255,255,255,1), rgba(255,255,255,0.75)',
        'margin' : '0px',
        'padding' : '20px',
        'padding-bottom' : '5px',
        'text-shadow' : '#fff 1px 1px 10px, #fff 1px 1px 5px, #fff -1px -1px 10px, #fff -1px -1px 5px'
    },

    # Bottom inner thumbnail
    'p' : {
        'color' : '#000',
        'background-image' : 'linear-gradient(to bottom, rgba(255,255,255,1), rgba(255,255,255,0.75)',
        'margin' : '0px',
        'padding' : '20px',
        'padding-top' : '5px',
        'text-shadow' : '#fff 1px 1px 10px, #fff 1px 1px 5px, #fff -1px -1px 10px, #fff -1px -1px 5px'
    },

    'thumbnail_components_container' : {
        'width' : '100%',
        'height' : '100%',
        # Text within Thumbnail
        #'text-align' : 'center',
        'display': 'flex',
        'flex-flow' : 'column nowrap',
        'justify-content': 'space-between',
        'align-items': 'flex-start'
    }
}

# Special Function for creating Dashboard Thumbnails
def thumbnail_style(image):
    return  {
        # Form and Function
        'max-width' : str(d.thumbnail_max_width) + 'px',
        'min-width' : str(d.thumbnail_height) + 'px',
        'height' : str(d.thumbnail_height) + 'px',
        "border-radius": "25px",
        "margin": str(d.thumbnail_margin) + "px",
        'padding' : '0px',
        'overflow-y' : 'hidden',
        'box-sizing' : 'border-box',
        
        # Remove text decoration defaulted for A elements
        'text-decoration' : 'none',

        # Background image should be thumbnail display image
        'background-color' : '#ffffff',
        'background-position': 'center',  # Center the background image
        'background-size': 'cover',  # Adjust the background image size
        'background-image' : image,  # Add the path to your image file or provide a URL

        # Send the container within Thumbnail to the center
        #'text-align' : 'center',
        'display': 'flex',
        'justify-content': 'center',
        'align-items': 'center'
    }



# For public/resticted inset thumbnail
def privacy_indicator(privacy_level):
    if privacy_level == "Public" :
        return "./assets/icons/no_border_international_academic_BW.png"
    elif privacy_level == "Restricted" :
        return "./assets/icons/no_border_id_BW.png"
    else :
        return "./assets/icons/no_border_technology_BW.png"



def buildDashboardOptions(application_type, UID):

    component_children = []

    # Get appropriate application records for the application type
    if (application_type == "publicdashboards") :
        # Display public dashboards
        app_records = sqlconnection.get_public_applications()

    elif (application_type == "myapplications") :
        # My Applications
        app_records = sqlconnection.get_applications_by_user(UID)

    elif (application_type == 'backend') :
        # Backend for Admin only
        app_records = sqlconnection.get_backend_applications()

    elif (application_type == 'adminall') :
        # Backend for Admin only
        app_records = sqlconnection.get_admin_all()

    else :
        return component_children

    # Split Records into lists
    titles = app_records['title']
    descriptions = app_records['description']
    authors = app_records['author']
    links = app_records['link']
    thumbnails = app_records['thumbnail']
    privacies = app_records['privacy']

    # Use zip iterator to create thumbnail for each application record
    for title, description, author, link, thumbnailurl, privacy in zip(titles, descriptions, authors, links, thumbnails, privacies):

        # Append Dashboard Thumbnail
        component_children.append(
            dash.html.A(
                href = link,

                className="dashboard-thumbnail",

                style = thumbnail_style('url("' + thumbnailurl + '")'),

                id = application_type + title,

                title= "Title: " + title + 
                    "\n\nAuthor(s): " + author + 
                    "\n\nPrivacy: " + privacy + 
                    "\n\nDescription: " + description,

                children = dash.html.Div(
                    
                    style = styles['thumbnail_components_container'],

                    children = [

                        dash.html.Div(
                            className = "Upper-Inner Thumbnail Container",
                            children = [
                                dash.html.Img(src = privacy_indicator(privacy), style = {'margin' : '10px', 'height' : '52px'}), # Info icon set to H1 Height
                            ]
                        ),

                        dash.html.Div(
                            className = "Lower-Inner Thumbnail Container",
                            children = [
                                dash.html.H2(title, style = styles['h3']),
                                dash.html.P(description, style = styles['p'])
                            ]
                        ),
                    ]
                )
            )
        )

    if component_children == [] :
        # Empty list of dashboards
        return dash.html.H4("There is nothing to display here.", style = {'width' : '100%', 'text-align' : 'center', 'color' : 'black'})

    return component_children

# DYNAMIC LAYOUT
def dynamic_layout(application_type, UID) :
    return dash.html.Div(
    id = application_type + component_id,
    style = styles['component'],
    children = buildDashboardOptions(application_type, UID)
)

# CALLBACKS (0)
