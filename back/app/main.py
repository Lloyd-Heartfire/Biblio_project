from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import init_db

# Importation des router défini dans chacun de mes modules
from routes.book_route   import router as book_router
from routes.user_route   import router as user_router
from routes.author_route import router as author_router
from routes.serie_route  import router as serie_router
from routes.image_route  import router as image_router

app = FastAPI(title="Projet_Bibliothèque")

app.add_middleware(
  CORSMiddleware,
  allow_origins=["http://localhost:3000"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

@app.on_event("startup")
def on_startup():
    init_db()

app.include_router(book_router)
app.include_router(user_router)
app.include_router(author_router)
app.include_router(serie_router)
app.include_router(image_router)