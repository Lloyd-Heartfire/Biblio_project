from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database.database import init_db, create_tables
from app.routes import book_route, user_route, author_route, image_route, serie_route
import uvicorn

# Importation des router défini dans chacun de mes modules
# from routes.book_route   import router as book_router
# from routes.user_route   import router as user_router
# from routes.author_route import router as author_router
# from routes.serie_route  import router as serie_router
# from routes.image_route  import router as image_router

app = FastAPI(title="Projet_Bibliothèque")

app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

@app.on_event("startup")
def on_startup():
    init_db()
    create_tables()

app.include_router(book_route.router)
app.include_router(user_route.router)
app.include_router(author_route.router)
app.include_router(serie_route.router)
app.include_router(image_route.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)