# Temporary file for connecting to the data server.

from mysql.connector import connect, Error

# MySQL connection configuration
config = {
    'user': 'datadashapp',
    'password': 'uXINl[k18bT_5Q(G',
    'host': 'rieeedata.its.appstate.edu',
    'port': '3306',
    'database': 'datadash_application',
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
