from typing import Optional, MutableMapping, Any

import os
import logging

from pydantic import BaseSettings

from app.utils.strings import get_app_version


class Settings(BaseSettings):
    ''' App settings. '''

    project_name: str = 'notes-api'
    project_version: str = get_app_version()

    environment: str = 'production'
    debug: bool = False

    # default connection is sqlite in memory
    database_uri: Optional[str] = 'sqlite:///?check_same_thread=false'


class DevSettingsBuilder():
    ''' Settings builder intended to be used in development environment '''
    @classmethod
    def build(cls) -> Settings:
        ''' Create a Settings instance configured for development '''
        return Settings(
            environment='development',
            debug=True
        )


class Environment():
    @staticmethod
    def select() -> Settings:
        env_vars: MutableMapping[Any, Any] = os.environ

        settings_class = None

        # if environment is setted to development
        if env_vars.get('environment') == 'development':
            settings_class = DevSettingsBuilder
        else:
            # TODO: Add production environment
            settings_class = DevSettingsBuilder

        settings = settings_class().build()

        # don't say i've not told you
        if 'sqlite://' in (settings.database_uri or ''):
            logging.warning('Using default Sqlite3 database in memory')

        return settings
