# React2Shell (CVE-2025-55182) 

## Description

PoC for exploiting RCE vulnerability in React Server Components in a Next.js application.

[![POC](https://img.youtube.com/vi/GT_C01eUUTg/0.jpg)](https://www.youtube.com/watch?v=GT_C01eUUTg)

## Installation

> *NOTE: In order for the following commands to work, make sure you have both `Docker` and `Docker Compose` installed on your machine. To install these tools, please refer to the official [documentation](https://docs.docker.com/get-started/get-docker/).*

To start the infrastructure, use the command below:

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
