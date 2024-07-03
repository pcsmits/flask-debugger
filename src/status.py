from flask import Blueprint, current_app, request

import psycopg2
import subprocess

status = Blueprint('status', __name__)

@status.route('/status', methods=['GET', 'POST'])
def status_main():

    # Establish the connection
    try:
        connection = psycopg2.connect(
            dbname=current_app.config["pg_db"], user=current_app.config["pg_user"], password=current_app.config["pg_pass"], host=current_app.config["pg_host"], port=5432
        )
        return "Connected to the database"
    
#        # Create a cursor object to interact with the database
#        cursor = connection.cursor()
#    
#        # Example: Execute a simple SQL query
#        cursor.execute("SELECT version();")
#        version = cursor.fetchone()
#        print("PostgreSQL version:", version)
#    
#        # Close the cursor and connection when done
#        cursor.close()
#        connection.close()
#        print("Connection closed")
    
    except Exception as e:
        return f'Error: Unable to connect to the database: {e}'
