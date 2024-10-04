from flask import Flask, jsonify  # Correctly import Flask
import psycopg2
from datetime import datetime

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host="dpg-cs029d3tq21c738t145g-a",  # Internal hostname
        database="canaryproject",            # Database name
        user="canaryproject_user",           # Database username
        password="tBvTtZE65hv2WdYnTreIiXJwxaRq7UEh"  # Database password
    )
    return conn

@app.route('/api/logs', methods=['GET'])  # Correct the route definition
def get_logs():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT email_id, public_ip, user_agent, access_time FROM logs ORDER BY access_time DESC')
    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    logs = [
        {
            "email_id": row[0],
            "public_ip": row[1],
            "user_agent": row[2],
            "access_time": row[3].strftime('%Y-%m-%d %H:%M:%S')  # Make sure access_time is included in the SELECT statement
        }
        for row in rows
    ]
    return jsonify(logs)

if __name__ == '__main__':  # Corrected the equality operator
    app.run(host='0.0.0.0', port=5000)

