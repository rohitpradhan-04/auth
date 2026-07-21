import os

from dotenv import load_dotenv

load_dotenv()


class Constants:
    db_host = os.getenv('DATABASE_HOST')
    db_user = os.getenv('DATABASE_USER')
    db_password = os.getenv('DATABASE_PASSWORD')
    db_port = os.getenv('DATABASE_PORT')
    db_name = os.getenv('DATABASE_NAME')

    secret = os.getenv('SECRETE')
