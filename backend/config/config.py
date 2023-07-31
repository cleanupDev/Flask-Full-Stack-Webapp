import pyodbc
import mysql.connector as mysql
from dotenv import dotenv_values
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from azure.core.exceptions import ResourceNotFoundError
import os


class Config:
    SECRET_KEY = "default_secret_key"
    DEBUG = False
    DB_HOST = "localhost"
    DB_USER = "default_user"
    DB_PASSWORD = "default_password"
    DB_NAME = "default_db"
    HOST = "localhost"
    PORT = 5001
    CORS_ORIGINS = ["http://localhost:3000", "http://localhost:5000"]


class DevelopmentConfig(Config):
    DEBUG = True
    DB_HOST = dotenv_values("backend/config/backend.env").get("DB_HOST")
    DB_USER = dotenv_values("backend/config/backend.env").get("DB_USER")
    DB_PASSWORD = dotenv_values("backend/config/backend.env").get("DB_PASSWORD")
    DB_NAME = dotenv_values("backend/config/backend.env").get("DB_NAME")
    HOST = dotenv_values("backend/config/backend.env").get("HOST")
    PORT = dotenv_values("backend/config/backend.env").get("PORT")
    # CORS_ORIGINS = dotenv_values("backend/config/backend.env").get("CORS_ORIGINS")
    
    def connection(self):
        try:
            return mysql.connect(
                host=self.DB_HOST,
                user=self.DB_USER,
                password=self.DB_PASSWORD,
                database=self.DB_NAME,
            )
        except Exception as e:
            raise Exception("Error connecting to database: " + str(e))


class ProductionConfig(Config):
    SECRET_KEY = os.environ.get("SECRET_KEY")

    def connection(self):
        try:
            credential = DefaultAzureCredential()

            key_vault_url = os.environ.get(
                "KEY_VAULT_URL", Exception("Environment variable not set")
            )
            secret_client = SecretClient(vault_url=key_vault_url, credential=credential)

            connection_string = secret_client.get_secret("CONNECTION_STRING").value

            conn = pyodbc.connect(connection_string, autocommit=True, timeout=30)

            return conn

        except ResourceNotFoundError:
            raise Exception("Connection string not found in key vault")

        except Exception as e:
            raise Exception("Error connecting to database: " + str(e))


def get_config(environment=os.environ.get("ENVIRONMENT", "development")):
    if environment == "production":
        return ProductionConfig()
    else:
        return DevelopmentConfig()
