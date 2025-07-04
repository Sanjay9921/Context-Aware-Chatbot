# modules/database_ops/routes/__init__.py

from .rag_routes import rag_blueprint

def register_routes(app):
    app.register_blueprint(rag_blueprint, url_prefix="/api")