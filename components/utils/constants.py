"""
Module/Script Name: constants.py
Author: M. W. Hefner
Created: 6/28/2023
Last Modified: 7/09/2023
Version: 1.0
"""

# Import Dependencies
import math
#
## Application constants
#

# Markdown pages are constants
# Welcome Banner Markdown
with open("./assets/markdown/welcomebanner.md", "r") as file:
    welcomebanner_markdown = file.read()

# Footer Markdown
with open("./assets/markdown/footer.md", "r") as file:
    footer_markdown = file.read()

# The mathematical constant phi
# used so that the thumbnails are golden rectangles at max width
phi = 1.61803

# Standard AppState gold from university communications
appstate_gold = "#ffcc00"

# height of the header
header_height = "90px"

# max width of the content area
content_max_width = 1140

thumbnails_per_row = 2

thumbnail_margin = 5

# Calculated Constants

application_display_padding = thumbnail_margin

whitespace = 2 * application_display_padding + thumbnails_per_row * 2 * thumbnail_margin

usable_space = content_max_width - whitespace

thumbnail_max_width = usable_space / thumbnails_per_row

# Floor to prevent overflow of flex thumbnails from rounding error
thumbnail_height = thumbnail_max_width / phi