# GitLab-User-Enumeration
Python 3 Script for Enumerating Users on GitLab

This code is an enhanced version of GitLab User Enum in Python 3](https://github.com/dpgg101/GitLabUserEnum/tree/main)

## Motivation
The Academy Lab server occasionally experiences instability and is unable to handle a high volume of simultaneous connections. As a result, running the original script sometimes led to connection losses and uncaught Python errors, which would cause the script to terminate unexpectedly.

To address this issue, I implemented an incremental delay mechanism: when a connection fails, the script will now wait for a gradually increasing interval before retrying the request, continuing this process until a successful connection is re-established. Additionally, for better monitoring and usability, I have added a progress counter to provide real-time feedback on the script’s execution.

## Usage 
```
python3 git_userenum.py -u http://somesite.com -w /usr/share/seclists/Usernames/xato-net-10-million-usernames-dup.txt
```

additional flags: 
`-v` -> verbose 
`--delay` -> set the initial starting delay time (default is 5s)
`--output` -> saves the output to a file
