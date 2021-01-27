from fastapi import FastAPI

from app.config import Settings, Environment
from app.exceptions.definitions import AppBootstrappingError


class AppBuilder():
    ''' Application builder. This class keeps the logic of app
    bootstrapping '''

    def __init__(self, *, settings: Settings):
        ''' Create a builder instance with specified configuration '''
        if settings is None:
            raise AppBootstrappingError('Must provide a valid Settings object')

        self.settings = settings

    @classmethod
    def with_environment_settings(cls) -> 'AppBuilder':
        ''' Create a builder instance with configuration gathered from env '''
        return cls(settings=Environment.select())

    def _instance_app(self) -> FastAPI:
        return FastAPI(
            title=self.settings.project_name,
            version=self.settings.project_version,
            debug=self.settings.debug
        )

    def _register_exception_handlers(self, app: FastAPI) -> None:
        pass

    def _register_models(self, app: FastAPI) -> None:
        pass

    def _register_routes(self, app: FastAPI) -> None:
        pass

    def _register_middlewares(self, app: FastAPI) -> None:
        pass

    def build(self) -> FastAPI:
        try:
            app = self._instance_app()

            self._register_exception_handlers(app)
            self._register_models(app)
            self._register_middlewares(app)
            self._register_routes(app)

            return app
        except Exception as e:
            import logging

            logging.critical('App failed to start')
            raise AppBootstrappingError(str(e))
