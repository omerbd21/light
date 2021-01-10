from scp import SCPClient
from fastapi import APIRouter, Response, status
from classes import Playbook
import paramiko
from settings import PRIVATE_KEY

router = APIRouter()


@router.put("/run_playbook/", tags=["playbook"])
async def run_playbook(playbook: Playbook, response: Response):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(hostname=playbook.master, username='root', key_filename=PRIVATE_KEY)
        stdin, stdout, stderr = ssh.exec_command("mkdir -p /opt/" + playbook.project_name)
        for line in stdout.read().splitlines():
            print(line)
        scp = SCPClient(ssh.get_transport())
        scp.put(playbook.playbook_path, remote_path="/opt/" + playbook.project_name + "/" + playbook.name)
        scp.put(playbook.inventory_path, remote_path="/opt/" + playbook.project_name + "/inventory_" + playbook.name)
        stdin, stdout, stderr = ssh.exec_command("ansible-playbook -i /opt/" + playbook.project_name +
                                                 "/inventory_" + playbook.name + " /opt/"
                                                 + playbook.project_name + "/" + playbook.name)
        for line in stdout.read().splitlines():
            print(line)
        ssh.close()
        return {"status": "200 OK"}
    except TimeoutError:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"status": "404 The hostname/ip in the request can't be accessed"}
