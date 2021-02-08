from typing import Optional
from uuid import uuid4, UUID

from fastapi import Request, Response
from starlette.middleware.base import (
    BaseHTTPMiddleware,
    RequestResponseEndpoint
)


class IdentifyRequestsMiddleware(BaseHTTPMiddleware):
    REQUEST_UUID_HEADER: str = 'X-Request-UUID'

    async def dispatch(
        self,
        request: Request,
        call_next: RequestResponseEndpoint
    ) -> Response:
        request_id: Optional[str] = request.headers.get(
            self.REQUEST_UUID_HEADER,
            None
        )

        if request_id is None:
            request_id: str = str(uuid4())
        else:
            try:
                UUID(request_id)
            except ValueError:
                # TODO: must allow invalid uuid?
                request_id: str = str(uuid4())

        request.state.request_uuid: str = request_id

        response = await call_next(request)

        # bypass the request's uuid to next services/client
        response.headers[self.REQUEST_UUID_HEADER] = request_id

        return response
