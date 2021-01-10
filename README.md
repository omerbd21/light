# light
light is a REST API to control an Ansible master.
## What does it do?
The API can add an ansible master or run a playbook on nodes.

## How does it work?
The API was written in Python with the FastAPI framework.

## Requirements
All of your nodes & master must be available for passwordless SSH
All of the nodes & master must be of linux and the RedHat family OS
## Notes
This is part of a bigger project, which is why it is currently only an API without a UI.
Later on, it will be integrated with multiple APIs to create a web application.

<b>Omer Ben David, January 2021<b>
