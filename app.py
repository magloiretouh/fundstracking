from config import app
from models import *
from routes import register_routes
from flask import Flask, request, jsonify
from sqlalchemy.exc import IntegrityError

# Register the blueprints using the imported function
register_routes(app)

if __name__ == '__main__':
    app.run()