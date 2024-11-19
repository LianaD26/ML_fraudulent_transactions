from fastapi import FastAPI
from app.routes.predictions import router as prediction_router

app = FastAPI()
# registrar rutas
app.include_router(prediction_router, prefix='/api', tags=["Predictions"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)