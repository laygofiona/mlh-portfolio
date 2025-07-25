#!/bin/bash

MY_CONTAINER='my_portfolio'

# make sure script stops when a command fails
set -eu

# move into project folder
cd mlh-portfolio

echo "Fetching latest changes from remote repo and updating current working directory"
# fetch the latest changes from remote repo on github and set current local directory to match changes from branch
git fetch && git reset origin/main --hard

# check if production container is running before stopping it
echo "Checking for any running production containers"
if [$(docker ps | grep -ic "$MY_CONTAINER") -gt 0]; then
	echo "Stopping running container: $MY_CONTAINER"
	# there is a running container so stop it
	docker stop $MY_CONTAINER
fi

echo "Building portfolio production image and starting its container"
# build docker image in docker-compose.prod.yml and start its container
docker compose -f docker-compose.prod.yml up -d --build


