from typing import Optional, Any

from fastapi import FastAPI, APIRouter, Request
from fastapi import Depends

router = APIRouter()


@router.get('/status')
async def status():
    return {
        'result': 'Running!'
    }


@router.api_route(
    '/echo/{text:path}',
    methods=[
        'GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'OPTIONS'
    ]
)
async def echo(request: Request):
    if True:
        return {
            'result': {
                'client': f'{request.client.host}:{request.client.port}',
                'method':  request.method,
                'url': {
                    'full': request.url._url,
                    'scheme': request.url.scheme,
                    'netloc': request.url.netloc,
                    'path': request.url.path,
                    'query': request.url.query,
                    'fragment': request.url.fragment,
                    'username': request.url.username,
                    'password': request.url.password,
                    'hostname': request.url.hostname,
                    'port': request.url.port,
                },
                'headers': request.headers,
                'cookies': request.cookies,
                'path': request.path_params,
                'query': request.query_params,
                'raw_body': await request.body(),
                'state': request.state
            }
        }
    else:
        return {
            'message': 'Echo endpoint is only available in DEBUG mode'
        }
