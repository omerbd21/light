from fastapi import APIRouter, Response, status
from classes import Node
import paramiko
from settings import PRIVATE_KEY

router = APIRouter()


@router.post("/install", tags=["install"])
async def install_ansible(node: Node, response: Response):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(hostname=node.hostname, username='root', key_filename=PRIVATE_KEY)
        stdin, stdout, stderr = ssh.exec_command("yum install -y epel-release")
        for line in stdout.read().splitlines():
            print(line)
        stdin, stdout, stderr = ssh.exec_command("yum update -y")
        for line in stdout.read().splitlines():
            print(line)
        stdin, stdout, stderr = ssh.exec_command("yum install -y ansible")
        for line in stdout.read().splitlines():
            print(line)
        ssh.close()
        return {"status": "200 OK"}
    except TimeoutError:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"status": "404 The hostname/ip in the request can't be accessed"}
