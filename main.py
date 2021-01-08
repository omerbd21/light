from fastapi import FastAPI
from api import router, playbook_router
app = FastAPI()
app.include_router(router)
app.include_router(playbook_router)


@app.get("/")
def read_root():
    return {"hello": "world"}
