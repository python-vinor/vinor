from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from standard.models.db import init_db
from standard.configs.app import appConfigs
from standard.routers.v1.router_v1 import router_v1
from standard.routers.v2.router_v2 import router_v2
from standard.middlewares import ROUTES_MIDDLEWARE


app = FastAPI(
    title="Standard API",
    description="Opensource Portfolio Application",
    version="0.0.1",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Github",
        "url": "https://github.com/ethanvu-dev/standard",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
    middleware=ROUTES_MIDDLEWARE,
)
app.mount(appConfigs.STATICS_ROUTE, StaticFiles(directory=appConfigs.STATICS_DIRECTORY), name="static")


@app.on_event("startup")
async def startup_event():
    init_db()


@app.on_event("shutdown")
def shutdown_event():
    with open("app.log", mode="a") as log:
        log.write("Application shutdown")


# Register APIs
app.include_router(router_v1)
app.include_router(router_v2)
