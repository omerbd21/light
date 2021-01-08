from fastapi import APIRouter
from classes import Node

router = APIRouter()


@router.post("/install/", tags=["install"])
async def install_ansible(node: Node):
    return node
