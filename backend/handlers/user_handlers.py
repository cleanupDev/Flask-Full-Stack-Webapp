from handlers.connection import connection
from models.user import User
from app import bcrypt
from flask import jsonify
from flask_jwt_extended import create_access_token
import uuid
import datetime


def login_user(user: User):
    try:
        conn = connection()
        cursor = conn.cursor()

        cursor.execute(
            """
                        SELECT * FROM users WHERE username = %s
                            """,
            (user.username,),
        )

        result = cursor.fetchone()

        if result:
            if bcrypt.check_password_hash(result[2], user.password):
                logged_in_user = User(
                    id=result[0],
                    username=result[1],
                    # password=result[2],
                    email=result[3],
                    created_at=result[4],
                    is_active=result[5],
                    is_admin=result[6],
                    is_verified=result[7],
                    is_authenticated=result[8],
                )
                return (
                    jsonify(
                        {
                            "status": "success",
                            "message": "User logged in successfully",
                            "data": logged_in_user.to_dict(),
                            "access_token": create_access_token(
                                identity=logged_in_user.username
                            ),
                        }
                    ),
                    200,
                )

            else:
                return (
                    jsonify(
                        {
                            "status": "error",
                            "message": "Incorrect password",
                            "data": None,
                            "access_token": None,
                        }
                    ),
                    401,
                )
        else:
            return (
                jsonify(
                    {
                        "status": "error",
                        "message": "Unknown username",
                        "data": None,
                        "access_token": None,
                    }
                ),
                401,
            )

    except Exception as e:
        return (
            jsonify(
                {
                    "status": "error",
                    "message": str(e),
                    "data": None,
                    "access_token": None,
                }
            ),
            500,
        )

    finally:
        conn.close()


def register_user(user: User):
    try:
        conn = connection()
        cursor = conn.cursor()

        cursor.execute(
            """
                        SELECT * FROM users WHERE username = %s or email = %s
                            """,
            (user.username, user.email),
        )

        result = cursor.fetchone()

        if result:
            if result[1] == user.username:
                return (
                    jsonify(
                        {
                            "status": "error",
                            "message": "Username already exists",
                            "data": None,
                        }
                    ),
                    409,
                )
            else:
                return (
                    jsonify(
                        {
                            "status": "error",
                            "message": "Email already exists",
                            "data": None,
                        }
                    ),
                    409,
                )

        else:
            cursor.execute(
                """
                            INSERT INTO users (id, username, password, email, first_name, last_name, created_at, is_active, is_admin, is_verified, is_authenticated)
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                                """,
                (
                    uuid.uuid4(),
                    user.username,
                    bcrypt.generate_password_hash(user.password),
                    user.email,
                    user.first_name,
                    user.last_name,
                    datetime.datetime.now(),
                    user.is_active,
                    user.is_admin,
                    user.is_verified,
                    user.is_authenticated,
                ),
            )

            conn.commit()

            return (
                jsonify(
                    {
                        "status": "success",
                        "message": "User registered successfully",
                        "data": None,
                    }
                ),
                201,
            )

    except Exception as e:
        return jsonify({"status": "error", "message": str(e), "data": None}), 500

    finally:
        conn.close()
