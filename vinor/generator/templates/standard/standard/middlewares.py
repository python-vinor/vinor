from starlette.middleware import Middleware
from starlette.middleware.gzip import GZipMiddleware
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.trustedhost import TrustedHostMiddleware
from starlette.middleware.base import BaseHTTPMiddleware

allow_origins = [
    "http://127.0.0.1:4200",
    "http://localhost:4200",
    "http://127.0.0.1:3000",
    "http://localhost:3000",
]

trusted_hosts = [
    'example.com',
    '*.example.com',
    '127.0.0.1',
    'localhost',
]


# Custom middleware for react-admin js
class ReactAdminHeaderMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        response = await call_next(request)
        response.headers['X-Total-Count'] = str(50)
        return response


ROUTES_MIDDLEWARE = [
    Middleware(ReactAdminHeaderMiddleware),
    Middleware(GZipMiddleware, minimum_size=1000),
    Middleware(CORSMiddleware, allow_origins=allow_origins, allow_credentials=True, allow_methods=["*"],
               allow_headers=["*"], expose_headers=["X-Total-Count"]),
    Middleware(TrustedHostMiddleware, allowed_hosts=trusted_hosts),
]
