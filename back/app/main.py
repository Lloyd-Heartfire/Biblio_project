from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database.database import init_db, create_tables
from app.routes import book_route, user_route, author_route, image_route, serie_route
import uvicorn

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