from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import psycopg2

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

def get_db_connection():
    conn = psycopg2.connect(
        host='postgres-container',
        database='mydatabase',
        user='postgres',
        password='Kaplior0909',
        port='5432'
    )
    return conn

@app.route('/cities', methods=['GET'])
def get_cities():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM table1')
    cities = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify([{'id': row[0], 'city': row[1]} for row in cities])

@app.route('/city/<int:city_id>', methods=['GET'])
def get_city(city_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM table1 WHERE id = %s', (city_id,))
    city = cur.fetchone()
    cur.close()
    conn.close()
    if city:
        return jsonify({'id': city[0], 'city': city[1]})
    else:
        return jsonify({'error': 'City not found'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
