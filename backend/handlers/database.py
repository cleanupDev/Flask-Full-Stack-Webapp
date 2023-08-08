from flask import jsonify
from backend.handlers import connection
import logging


def init_db():
    logging.info("Initializing database")
    try:
        conn = connection()
        cursor = conn.cursor()

        cursor.execute(
            """
                       CREATE TABLE IF NOT EXISTS users (
                            id CHAR(36) NOT NULL UNIQUE,
                            username VARCHAR(255) NOT NULL UNIQUE,
                            password VARCHAR(255) NOT NULL,
                            email VARCHAR(255) NOT NULL UNIQUE,
                            first_name VARCHAR(255) NOT NULL,
                            last_name VARCHAR(255) NOT NULL,
                            created_at DATETIME NOT NULL,
                            is_active BOOLEAN NOT NULL,
                            is_admin BOOLEAN NOT NULL,
                            is_verified BOOLEAN NOT NULL,
                            is_authenticated BOOLEAN NOT NULL
                       )"""
        )

        conn.commit()

        logging.info("Database initialized successfully")
        return jsonify(
            {
                "status": "success",
                "message": "Database initialized successfully",
                "data": None,
            }
        ), 200

    except Exception as e:
        logging.error("Error initializing database: " + str(e))
        return jsonify(
            {
                "status": "error",
                "message": "Error initializing database: " + str(e),
                "data": None,
            }
        ), 500

    finally:
        conn.close()
