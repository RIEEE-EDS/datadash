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
