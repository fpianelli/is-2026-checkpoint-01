import os
from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

def get_db_connection():
    return psycopg2.connect(
        host=os.environ.get("DB_HOST"),
        database=os.environ.get("DB_NAME"),
        user=os.environ.get("DB_USER"),
        password=os.environ.get("DB_PASSWORD")
    )

@app.route("/api/health")
def health():
    return jsonify({"status": "ok"})

@app.route("/api/info")
def info():
    return jsonify({
        "service": "backend",
        "version": "1.0",
        "status": "running"
    })

@app.route("/api/team")
def get_team():
    try:
        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute("SELECT nombre, apellido, legajo, feature, servicio, estado FROM members;")
        rows = cur.fetchall()

        members = []
        for row in rows:
            members.append({
                "nombre": row[0],
                "apellido": row[1],
                "legajo": row[2],
                "feature": row[3],
                "servicio": row[4],
                "estado": row[5]
            })

        cur.close()
        conn.close()

        return jsonify(members)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


app.run(host="0.0.0.0", port=5000)
