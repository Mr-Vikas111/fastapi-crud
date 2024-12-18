import sys
import os

# sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from fastapi import FastAPI
import apis

app = FastAPI()

app.include_router(apis.router)