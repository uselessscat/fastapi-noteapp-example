import pytest


class TestApp():
    def test_app_creation_no_settings(self):
        from app.bootstrap import AppBuilder
        from app.exceptions.definitions import AppBootstrappingError

        with pytest.raises(AppBootstrappingError):
            AppBuilder(settings=None).build()

    def test_app_creation_development(self):
        from fastapi import FastAPI

        from app.config import DevSettingsBuilder
        from app.bootstrap import AppBuilder

        settings = DevSettingsBuilder.build()
        app: FastAPI = AppBuilder(settings=settings).build()

        assert isinstance(app, FastAPI)
        assert app.title == settings.project_name
        assert app.debug is True

    def test_app_creation_environment(self):
        raise NotImplementedError()
