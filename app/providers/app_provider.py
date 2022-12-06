from fastapi.middleware.cors import CORSMiddleware

from app.providers.database import db
from config.config import settings


def register(app):
    app.debug = settings.DEBUG
    app.title = settings.NAME

    add_global_middleware(app)

    # This hook ensures that a connection is opened to handle any queries
    # generated by the request.
    # @app.on_event("startup")
    # def startup():
    #     db.connect()

    # This hook ensures that the connection is closed when we've finished
    # processing the request.
    @app.on_event("shutdown")
    def shutdown():
        if not db.is_closed():
            db.close()


def add_global_middleware(app):
    """
    注册全局中间件
    """
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
