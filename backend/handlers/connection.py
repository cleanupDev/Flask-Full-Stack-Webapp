from flask import jsonify
from handlers import get_config
import logging

CONFIG = get_config()


def connection():
    """Get database connection"""
    return CONFIG.connection()


def ping():
    """Test database connection"""
    logging.debug("Pinging database")
    try:
        conn = connection()
        cursor = conn.cursor()
        cursor.execute("SELECT 1")
        logging.debug("Database ping successful")
        return jsonify({"message": "Pong!"}), 200

    except Exception as e:
        logging.error("Error pinging database: " + str(e))
        return jsonify({"message": str(e)}), 500

    finally:
        conn.close()
