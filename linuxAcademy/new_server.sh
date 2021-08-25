#!/bin/bash

read -p "Server ID: " ID
read -p "Temp Pass: " OLD_PASS
read -p "Key file: (default: id_rsa: " KEY_FILE

KEY_FILE=${KEY_FILE:-'id_rsa'}
PUB="${KEY_FILE}.pub"
ID=${ID}

username = 'user_id'
PASS='P@$$w0rd'

SERVER="$username$ID.mylabserver.com"


# remove old server identity from known_hosts. LA reuses hostnames and get an error
if ssh-keyscan -t ecdsa $SERVER;then
    # ssh-keyscan -t ecdsa $SERVER >> ~/.ssh/known_hosts
    ssh-keygen -R $SERVER
    echo "$SERVER Known host updated"
else
    echo "No host found for $SERVER"
fi

# Use expect script to run ssh-copy-id to copy key and change the temp password
if [[ $? -eq 0 ]];then
    copy_key_to_server.exp $SERVER $OLD_PASS $PASS $PUB
    # sleep 10s
fi

# create shortcut for ease of use when sshing later
if [[ $? -eq 0 ]]; then

if grep -q LA_$ID ~/.ssh/config;then
    echo "SSH Shortcut already exists"
else
    cat >> ~/.ssh/config <<EOL

Host LA_${ID}
    HostName ${SERVER}
    User cloud_user
    IdentityFile ~/.ssh/${KEY_FILE}
EOL
    echo "New host Added to shortcut as LA_$ID"
fi
else
    echo "Expect script failed"
fi

# open ssh connection to the new machine
if [[ $? -eq 0 ]];then
    ssh "LA_$ID"
else
    echo "Something went wrong with ssh connection"
fi
