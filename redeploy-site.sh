#!/bin/bash

MY_CONTAINER='myportfolio'


# make sure script stops when a command fails
set -eu

# move into project folder
cd mlh-portfolio

echo "Fetching latest changes from remote repo and updating current working directory"
# fetch the latest changes from remote repo on github and set current local directory to match changes from branch
git fetch && git reset origin/main --hard

# check if production container is running before stopping it
echo "Checking for any running production containers"
# ensure container variable is not empty
# limits docker ps output to container names only, match exact container name and count the number of matches
if [[ -n "$MY_CONTAINER" && $(docker ps --format '{{.Names}}' | grep -w "$MY_CONTAINER" | wc -l) -gt 0 ]]; then
    echo "Stopping running container: $MY_CONTAINER"
    docker stop "$MY_CONTAINER"
fi


echo "Building portfolio production image and starting its container"
# build docker image in docker-compose.prod.yml and start its container
docker compose -f docker-compose.prod.yml up -d --build


