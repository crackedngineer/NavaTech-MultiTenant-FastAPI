from fastapi import FastAPI
from app.api.organisation import routes as OrgRoutes
from app.api.auth import routes as AuthRoutes

app = FastAPI(
    title="MultiTenant FastAPI",
    description="🚀 RestAPI using FastAPI",
    version="0.1.0",
)

app.include_router(
    OrgRoutes,
    tags=["organisation"],
    prefix="/v1",
)

app.include_router(
    AuthRoutes,
    tags=["authentication"],
    prefix="/v1",
)
