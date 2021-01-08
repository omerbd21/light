from fastapi import APIRouter
from classes import Node
import paramiko

router = APIRouter()


@router.post("/install/", tags=["install"])
async def install_ansible(node: Node):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=node.hostname, username='root', key_filename='C:\\Users\\omerb\\.ssh\\id_rsa')
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
