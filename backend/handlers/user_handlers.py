from models import User
from flask import jsonify
from flask_jwt_extended import create_access_token
import uuid
import datetime
import logging
from backend.handlers import bcrypt, connection


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
                    first_name=result[4],
                    last_name=result[5],
                    created_at=result[6],
                    is_active=result[7],
                    is_admin=result[8],
                    is_verified=result[9],
                )

                logging.debug("User logged in successfully")

                return (
                    jsonify(
                        {
                            "status": "success",
                            "message": "User logged in successfully",
                            "data": logged_in_user.to_dict(),
                            "access_token": create_access_token(
                                identity=logged_in_user.id
                            ),
                        }
                    ),
                    200,
                )

            else:
                logging.debug("Incorrect password")
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
            logging.debug("Unknown username")
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
        logging.error(str(e))
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
            logging.debug("Username or email already exists")
            if result[1] == user.username:
                logging.debug("Username already exists")
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
                logging.debug("Email already exists")
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
            logging.debug("Inserting user into database")
            cursor.execute(
                """
                            INSERT INTO users (id, username, password, email, first_name, last_name, created_at, is_active, is_admin, is_verified)
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                                """,
                (
                    str(uuid.uuid4()),
                    user.username,
                    bcrypt.generate_password_hash(user.password),
                    user.email,
                    user.first_name,
                    user.last_name,
                    datetime.datetime.now(),
                    user.is_active,
                    user.is_admin,
                    user.is_verified,
                ),
            )

            conn.commit()

            logging.debug("User registered successfully")
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
        logging.error(str(e))
        return jsonify({"status": "error", "message": str(e), "data": None}), 500

    finally:
        conn.close()


def get_user_by_id(user_id: str):
    try:
        logging.debug(f"Retrieving fresh userdata from database for {user_id}")
        conn = connection()
        cursor = conn.cursor()

        cursor.execute(
            """
                        SELECT * FROM users WHERE id = %s
                            """,
            (user_id,),
        )

        result = cursor.fetchone()

        if result:
            logging.debug("User retrieved successfully")
            return (
                jsonify(
                    {
                        "status": "success",
                        "message": "User retrieved successfully",
                        "data": User(
                            id=result[0],
                            username=result[1],
                            # ? password=result[2],
                            email=result[3],
                            first_name=result[4],
                            last_name=result[5],
                            created_at=result[6],
                            is_active=result[7],
                            is_admin=result[8],
                            is_verified=result[9],
                        ).to_dict(),
                    }
                ),
                200,
            )

        else:
            logging.error("User not found")
            return (
                jsonify(
                    {
                        "status": "error",
                        "message": "User not found",
                        "data": None,
                    }
                ),
                404,
            )

    except Exception as e:
        logging.error(str(e))
        return jsonify({"status": "error", "message": str(e), "data": None}), 500

    finally:
        conn.close()
