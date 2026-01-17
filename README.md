# React2Shell (CVE-2025-55182) 

## Description

PoC for exploiting RCE vulnerability in React Server Components in a Next.js application.

## Installation

In order for the following commands to work, make sure you have both Docker and Docker Compose installed on your machine. To install these tools, please refer to the official [documentation](https://docs.docker.com/get-started/get-docker/).


```bash
docker compose up --build -d
```

## Usage

To start the attacker's interactive shell, run the following command:

```bash
docker exec -it attacker ./attack.py
```

Then, enter the command you want to execute on the vulnerable server. To exit, type `exit`.

```
~ ❯ docker exec -it attacker ./attack.py
Enter command to execute (or 'exit' to quit): whoami
-------------------- COMMAND OUTPUT --------------------
root
--------------------------------------------------------
```

Can you find the `flag` hidden inside the server?
