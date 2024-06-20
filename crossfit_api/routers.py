from fastapi import APIRouter
from crossfit_api.atleta.controller import router as atleta
from crossfit_api.categorias.controller import router as categorias
from crossfit_api.centro_treinamento.controller import router as centro_treinamento

api_router = APIRouter()
api_router.include_router(atleta, prefix='/atletas', tags=['atletas'])
api_router.include_router(categorias, prefix='/categorias', tags=['categorias'])
api_router.include_router(centro_treinamento, prefix='/centros_treinamento', tags=['centros_treinamento'])