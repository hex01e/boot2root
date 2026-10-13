# Boot2Root Walkthroughs

This repository documents a small Boot2Root-style challenge focused on privilege escalation and exploitation on a vulnerable Linux VM. It includes two walkthroughs, screenshots, and a few helper scripts used during the challenge.

## Project Overview

The target machine in this project is a deliberately vulnerable Linux system, often referred to as a Boot2Root lab. The goal is to:

- enumerate exposed services,
- identify weak or leaked credentials,
- exploit a web application or service misconfiguration,
- gain a shell as an unprivileged user,
- escalate privileges to root.

The writeups in this repo capture two different approaches to reaching the same end goal.

## Repository Structure

```text
.
├── README.md
├── writeup1              # Detailed walkthrough of the web-based foothold and privilege escalation
├── writeup2              # Alternative method using the Dirty COW local privilege escalation
├── screenshots/          # Visual evidence captured during the challenge
├── scripts/
│   ├── fun.c             # Small C helper that prints a hidden password-like string
│   ├── turtle            # Binary/helper artifact associated with the turtle challenge
│   └── turtle.py         # Python parser that renders turtle movement commands into a graph
└── .git/                 # Repository metadata
```

## Walkthroughs

### Method 1: Web Enumeration and Shell Access

The first writeup focuses on:

- host discovery and port scanning,
- FTP/SSH/HTTP/IMAP service enumeration,
- discovery of exposed credentials in forum content,
- use of leaked webmail credentials,
- access to phpMyAdmin with database root credentials,
- file upload via SQL `INTO OUTFILE`,
- creation of a web shell,
- privilege escalation to root.

This method demonstrates how poor credential handling and insecure application behavior can quickly lead to full compromise.

### Method 2: Local Privilege Escalation via Dirty COW

The second writeup documents a kernel-level escalation route:

- checking the system kernel version,
- identifying the vulnerability as Dirty COW (CVE-2016-5195),
- compiling a local exploit,
- exploiting the race condition to modify `/etc/passwd`,
- switching to a root-equivalent user,
- confirming successful privilege escalation.

This path shows how a known kernel bug can be used for local root access when a user already has shell access.

## Scripts

### `scripts/fun.c`

A tiny C program that prints a hidden string character by character. It appears to be a simple challenge or puzzle helper that demonstrates a lightweight password/flag-style exercise.

### `scripts/turtle.py`

A Python script that parses turtle movement instructions and plots the resulting path using `matplotlib`. This is useful for turning textual movement commands into a visual path diagram.

### `scripts/turtle`

A compiled or helper artifact related to the turtle challenge. This file is likely used alongside the Python script or as a generated binary artifact from the challenge environment.

## Suggested Workflow

1. Start with `writeup1` for the full exploitation flow.
2. Review `writeup2` for the alternative local privilege escalation path.
3. Use the screenshots to correlate the described steps with the visible evidence.
4. Inspect the scripts in `scripts/` if you want to understand the supporting challenge components.

## Notes

This repository is primarily educational and demonstrates practical offensive security techniques in a CTF/lab context. It is intended for learning, documentation, and walkthrough capture rather than production use.

## License

No explicit license file is included in this repository, so the project should be treated as a personal educational archive unless another license is added later.
