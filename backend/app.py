from flask import flask,jsonify
import psycopg2
from datetime import datetime

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host="your-db-host",
        database="your-database-name",
        user="your-db-username",
        password="your-db-password"
        )
    return conn

@app.route('api/logs', methods=['GET'])
def get_logs():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT email_id,public_ip,user_agent_access_time FROM logs ORDER BY access_time DESC')
    rows = cursor.fetchall()
    cursor.close()
    conn.close()


    logs = [
        {"email_id": row[0], "public_ip": row[1], "user_agent": row[2], "access_time": row[3].strftime('%Y-%m-%d %H:%M:%S')}
    for row in rows
        ]
    return jsonify(logs)

if __name__ = '__main__':
    app.run(host='0.0.0.0', port=5000)
