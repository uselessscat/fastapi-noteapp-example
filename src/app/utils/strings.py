from typing import Dict


def build_postgres_dsn(uri_components: Dict[str, str]) -> str:
    return '{driver}://{user}:{password}@{host}:{port}/{database_name}'.format(
        driver='postgresql',
        user=uri_components.get('user'),
        password=uri_components.get('password'),
        host=uri_components.get('host'),
        port=uri_components.get('port'),
        database_name=uri_components.get('name'),
    )
