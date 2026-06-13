import os
import time
from flask import Flask, jsonify
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

def get_db_connection():
    # Attempt to connect to the database container using environment variables
    retries = 5
    while retries > 0:
        try:
            connection = mysql.connector.connect(
                host=os.environ.get('DB_HOST', 'db'),
                user=os.environ.get('DB_USER', 'root'),
                password=os.environ.get('DB_PASSWORD', 'secure_password'),
                database=os.environ.get('DB_NAME', 'my_app_db'),
                port=3306
            )
            if connection.is_connected():
                return connection
        except Error as e:
            print(f"Database not ready yet, retrying... ({retries} left). Error: {e}")
            retries -= 1
            time.sleep(5)
    return None

@app.route('/')
def home():
    connection = get_db_connection()
    if connection is None:
        return jsonify({
            "status": "error",
            "message": "Could not establish a connection to the MySQL database container."
        }), 500

    try:
        cursor = connection.cursor()
        # Initialize a table if it doesn't exist yet
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS page_views (
                id INT AUTO_INCREMENT PRIMARY KEY,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        # Insert a new record to verify write capabilities
        cursor.execute("INSERT INTO page_views () VALUES ()")
        connection.commit()

        # Retrieve the total count of logs
        cursor.execute("SELECT COUNT(*) FROM page_views")
        count = cursor.fetchone()[0]
        
        cursor.close()
        connection.close()

        return jsonify({
            "status": "success",
            "message": "Connected to the MySQL database successfully over the Docker network!",
            "total_database_writes": count,
            "architecture": "Multi-Container Decoupled Architecture"
        })
    except Error as e:
        return jsonify({"status": "error", "message": f"Query failed: {e}"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
