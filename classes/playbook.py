from pydantic import BaseModel


class Playbook(BaseModel):
    name: str
    playbook_path: str
    inventory_path: str
    master: str
    project_name: str
