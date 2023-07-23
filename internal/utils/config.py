import os
from dotenv import load_dotenv
load_dotenv()

APP_NAME = os.environ.get("APP_NAME", "mailer")

DB_HOST = os.environ.get("DB_HOST", "default_db_host")
DB_DATABASE = os.environ.get("DB_DATABASE", "default_db_database")
DB_USERNAME = os.environ.get("DB_USERNAME", "default_db_username")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "default_db_password")

SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_DATABASE}'
SQLALCHEMY_TRACK_MODIFICATIONS = False

MAIL_SERVER = os.environ.get("MAIL_SERVER", "default_mail_server")
MAIL_PORT = os.environ.get("MAIL_PORT", 587)
MAIL_USERNAME = os.environ.get("MAIL_USERNAME", "default_mail_username")
MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD", "default_mail_password")
MAIL_USE_TLS = os.environ.get("MAIL_USE_TLS", "True")
MAIL_USE_SSL = os.environ.get("MAIL_USE_SSL", "False")
MAIL_SENDER = os.environ.get("MAIL_SENDER", "notification@jublia.com")
