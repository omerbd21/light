from fastapi import FastAPI
from api import install_ansible, router
app = FastAPI()
app.include_router(router)


@app.get("/")
def read_root():
    return {"hello": "world"}
