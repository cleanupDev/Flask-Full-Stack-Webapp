from handlers.connection import connection
from flask import jsonify


def init_db():
    try:
        conn = connection()
        cursor = conn.cursor()

        cursor.execute(
            """
                       CREATE TABLE IF NOT EXISTS users (
                           id INT NOT NULL UNIQUE,
                            username VARCHAR(255) NOT NULL UNIQUE,
                            password VARCHAR(255) NOT NULL,
                            email VARCHAR(255) NOT NULL UNIQUE,
                            first_name VARCHAR(255) NOT NULL,
                            last_name VARCHAR(255) NOT NULL,
                            created_at DATETIME NOT NULL,
                            is_active BOOLEAN NOT NULL,
                            is_admin BOOLEAN NOT NULL,
                            is_verified BOOLEAN NOT NULL,
                            is_authenticated BOOLEAN NOT NULL,
                       )"""
        )

        conn.commit()

        return jsonify(
            {
                "status": "success",
                "message": "Database initialized successfully",
                "data": None,
            }
        ), 200

    except Exception as e:
        return jsonify(
            {
                "status": "error",
                "message": "Error initializing database: " + str(e),
                "data": None,
            }
        ), 500

    finally:
        conn.close()
