from config.config import get_config
from flask import jsonify

CONNECTION = get_config().connection()


def connection():
    """Get database connection"""
    return CONNECTION


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
