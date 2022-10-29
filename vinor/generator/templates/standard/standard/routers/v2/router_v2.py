from fastapi import APIRouter
from standard.routers.v2 import root_route, items_route


router_v2 = APIRouter(prefix="/v2")
router_v2.include_router(root_route.router, tags=["V2 - Root"])
router_v2.include_router(items_route.router, prefix="/items", tags=["V2 - Item"])
