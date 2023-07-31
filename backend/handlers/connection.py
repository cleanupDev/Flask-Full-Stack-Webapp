from flask import jsonify
from handlers import get_config

CONFIG = get_config()


def connection():
    """Get database connection"""
    return CONFIG.connection()


def ping():
    """Test database connection"""

    conn = connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT 1")
        return jsonify({"message": "Pong!"}), 200

    except Exception as e:
        return jsonify({"message": str(e)}), 500

    finally:
        conn.close()
