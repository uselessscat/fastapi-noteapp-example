import time

from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from fastapi import Request, Response


class TimeRequestsMiddleware(BaseHTTPMiddleware):
    '''
    This middleware adds the time it takes for the endpoint to generate results
    '''
    async def dispatch(
        self,
        request: Request,
        call_next: RequestResponseEndpoint
    ) -> Response:
        start_time = time.time()

        response = await call_next(request)

        process_time = time.time() - start_time

        response.headers['X-Process-Time'] = str(process_time)

        return response
