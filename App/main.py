from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from sqlalchemy.exc import SQLAlchemyError
import logging

from .database import Base, engine
from .routers import voters, candidates, votes

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Crear la base de datos
try:
    Base.metadata.create_all(bind=engine)
except SQLAlchemyError as e:
    logger.error(f"Error al crear las tablas de la base de datos: {e}")

# Crear instancia de la app
app = FastAPI(title="Voting System API")

# Registrar routers
app.include_router(voters.router)
app.include_router(candidates.router)
app.include_router(votes.router)

# Manejador para errores de validación
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    logger.warning(f"Error de validación: {exc}")
    return JSONResponse(
        status_code=422,
        content={"detail": exc.errors(), "body": exc.body},
    )

# Manejador para errores de base de datos
@app.exception_handler(SQLAlchemyError)
async def sqlalchemy_exception_handler(request: Request, exc: SQLAlchemyError):
    logger.error(f"Error de base de datos: {exc}")
    return JSONResponse(
        status_code=500,
        content={"detail": "Error interno al acceder a la base de datos."},
    )

# Manejador general para errores no controlados
@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    logger.error(f"Error inesperado: {exc}")
    return JSONResponse(
        status_code=500,
        content={"detail": "Ocurrió un error interno inesperado."},
    )

