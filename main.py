from fastapi import FastAPI
from routers.libros import router as libros_router

app = FastAPI()
app.include_router(libros_router)



     
            