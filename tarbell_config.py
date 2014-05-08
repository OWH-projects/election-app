# -*- coding: utf-8 -*-

"""
Tarbell project configuration
"""

# Short project name
NAME = "election_2014"

# Descriptive title of project
TITLE = "Nebraska Primary 2014"

# Google spreadsheet key
SPREADSHEET_KEY = "1ZdCFzblVySFMSiPkUT_8fgIA9fn_b5RlhokoOCu5mrM"

# Exclude these files from publication
EXCLUDES = ["*.md", "requirements.txt"]

# Create JSON data at ./data.json, disabled by default
# CREATE_JSON = True

# S3 bucket configuration
#S3_BUCKETS = {
    # Provide target -> s3 url pairs, such as:
    #     "mytarget": "mys3url.bucket.url/some/path"
    # then use tarbell publish mytarget to publish to it
#}

# Default template variables
DEFAULT_CONTEXT = {
    'name': 'election_2014',
    'title': 'Nebraska Primary 2014'
}