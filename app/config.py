import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')

load_dotenv(dotenv_path)

sqlalchemy_database_url = os.getenv("SQLALCHEMY_DATABASE_URL")