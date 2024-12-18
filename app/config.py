import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access environment variables
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME =  os.getenv("DB_NAME")
DB_SERVER =  os.getenv("DB_SERVER")
DB_PORT=os.getenv("DB_PORT")
DEBUG = os.getenv("DEBUG")
TESTING = os.getenv("TESTING")
GOOGLE_APPLICATION_CREDENTIALS=os.getenv("GOOGLE_APPLICATION_CREDENTIALS")