from fastapi import FastAPI, APIRouter
from mangum import Mangum
from starlette.middleware.cors import CORSMiddleware
from app.routers import messages
from app.utils.telegram_utils import set_telegram_webhook

origins = ["*"]
router = APIRouter()

app = FastAPI(
    title="Prueba Técnica Backend Developer",
    description='Documentación Prueba Técnica Backend Developer',
    version="0.0.1",
    openapi_url=f"/openapi.json"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@router.get("/")
def read_root():
    return {"status": "ok"}


@app.on_event("startup")
def startup():
    set_telegram_webhook()


app.include_router(router, prefix='')
app.include_router(messages.router, prefix='/messages')
