# Temporary file for connecting to the data server.

from mysql.connector import connect, Error
from components.utils.config import cfg

# MySQL connection configuration
config = {
    'user': cfg.get('app', 'dbuser'),
    'password': cfg.get('app', 'dbpass'),
    'host': cfg.get('app', 'dbhost'),
    'port': cfg.get('app', 'dbport'),
    'database': cfg.get('app', 'dbname'),
    'ssl_ca': './assets/rieeedata.crt'
}

# Establish a secure connection to the MySQL server
try:
    connection = connect(**config)
    # this can be helpful for debugging
    #print("Connected to MySQL server...")
except Error as e:
    print(f"Error connecting to MySQL server: {e}.  Are you connected to App's VPN?")
    exit(1)

# Create a cursor object to execute SQL queries
cursor = connection.cursor()

# Returns a user's role, should they have one.
def get_user_role(username):
    sql = "SELECT user_type FROM Users WHERE username = %s"
    values = (username,)
    cursor.execute(sql, values)
    result = cursor.fetchone()
    if result is not None:
        return result[0]
    else:
        return None

# This function is just a helper function to return application records in a nice format
def format_application_records(applications):
    formatted_records = {
        'title': [],
        'description': [],
        'author': [],
        'link': [],
        'thumbnail': [],
        'privacy' : []
    }
    
    for app in applications:
        formatted_records['title'].append(app[1])
        formatted_records['description'].append(app[2])
        formatted_records['author'].append(app[3])
        formatted_records['link'].append(app[5])
        formatted_records['thumbnail'].append(app[6])
        formatted_records['privacy'].append(app[7])
    
    return formatted_records

# Function to retrieve applications belonging to a user
def get_applications_by_user(username):
    sql = '''
    SELECT a.app_id, a.title, a.description, a.author, a.doi, a.link, a.thumbnail, a.permission_level
    FROM Applications a
    JOIN User_Application_Permissions p ON p.app_id = a.app_id
    JOIN Users u ON u.username = p.username
    WHERE u.username = %s
    '''
    values = (username,)
    cursor.execute(sql, values)
    result = cursor.fetchall()
    return format_application_records(result)

# Function to retrieve public applications
def get_public_applications():
    sql = '''
    SELECT app_id, title, description, author, doi, link, thumbnail, permission_level
    FROM Applications
    WHERE permission_level = 'Public'
    '''
    cursor.execute(sql)
    result = cursor.fetchall()
    return format_application_records(result)

# Function to retrieve backend applications
def get_backend_applications():
    sql = '''
    SELECT app_id, title, description, author, doi, link, thumbnail, permission_level
    FROM Applications
    WHERE permission_level = 'Backend'
    '''
    cursor.execute(sql)
    result = cursor.fetchall()
    return format_application_records(result)

# Function to retrieve all applications fpr admins
def get_admin_all():
    sql = '''
    SELECT app_id, title, description, author, doi, link, thumbnail, permission_level
    FROM Applications
    '''
    cursor.execute(sql)
    result = cursor.fetchall()
    return format_application_records(result)