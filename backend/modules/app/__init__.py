# modules/app/__init__.py

from flask import Flask, send_from_directory, jsonify
from flask_cors import CORS # Allow cross-origin for frontend
import os
from settings.config import Config

from modules.database_ops.routes import register_routes # REST API Routes

def create_app():
    app = Flask(
        __name__,
        static_folder=os.path.abspath(os.path.join(os.path.dirname(__file__), '../../frontend/build')),
        static_url_path='/'
    )
    
    CORS(app)
    register_routes(app)

    @app.route("/api/model", methods=["GET"])
    def get_model():
        return jsonify({"model": Config.DEFAULT_MODEL})

    # React static files serving and catch-all route
    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def serve_react_app(path):
        if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
            return send_from_directory(app.static_folder, path)
        else:
            return send_from_directory(app.static_folder, 'index.html')

    return app