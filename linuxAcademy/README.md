## Automates process to login via ssh from local computer to your Linux Academy VM's

### Not sure if this works any more since LA and a cloud Guru merger

Interaction with new VM was written in Expect programming language to automate the process of finishing the creation of VM and adding ssh key. 

Here is the book I used to learn Expect: 
[Explore Expect](https://www.amazon.com/_/dp/1565920902?tag=oreilly20-20)

1. Define LA username and password in new_server.sh

### LA reuses hostnames which causes identity issues
- Handles if old server identity is already in known_hosts for local computer

