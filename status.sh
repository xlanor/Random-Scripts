#!/bin/bash
# Script to check status


shopt -s nocasematch

i=0
while [[ "$i" -ne 1 ]]
do
	echo -en '\n'
	echo "----------------------------------------------------------------------"
	echo "What do you want to check?(gunicorn | celery | flower | mongo | exit)" 
	echo "----------------------------------------------------------------------"
	read answer
	if [[ "$answer" =~ "gunicorn" ]]
	then
		gunicornsgsiteout="$(ps aux | grep "--ignore-case" gunicorn | grep "--ignore-case" singapore | grep 9000)"
		gunicornsgapiout="$(ps aux | grep "--ignore-case" gunicorn | grep "--ignore-case" singapore | grep 9500)"
		gunicornmysiteout="$(ps aux | grep "--ignore-case" gunicorn | grep "--ignore-case" malaysia | grep 19000)"
		gunicornmyapiout="$(ps aux | grep "--ignore-case" gunicorn | grep "--ignore-case" malaysia | grep 19500)"
		echo "Gunicorn processes: "
		echo -en '\n'
		echo "Singapore site: "
		echo "${gunicornsgsiteout}"
		echo -en '\n'
		echo "Singapore site API: "
		echo "${gunicornsgapiout}"
		echo -en '\n'
		echo "Malaysia site: "
		echo "${gunicornmysiteout}"
		echo -en '\n'
		echo "Malaysia site API: "
		echo "${gunicornmyapiout}"

	elif [[ "$answer" =~ "celery" ]]
	then
		celerysgout="$(ps aux | grep "--ignore-case" celery | grep "--ignore-case" singapore | grep -v singapore_api)"
		celerysgapiout="$(ps aux | grep "--ignore-case" celery | grep "--ignore-case" singapore_api)"
		celerymyout="$(ps aux | grep "--ignore-case" celery | grep "--ignore-case" malaysia | grep -v malaysia_api)"
		celerymyapiout="$(ps aux | grep "--ignore-case" celery | grep "--ignore-case" malaysia_api)"

		echo "Celery Processes: "
		echo -en '\n'
		echo "Singapore celery: "
		echo "${celerysgout}"
		echo -en '\n'
		echo "Singapore API celery: "
		echo "${celerysgapiout}"
		echo -en '\n'
		echo "Malaysia celery: "
		echo "${celerymyout}"
		echo -en '\n'
		echo "Malaysia API celery: "
		echo "${celerymyapiout}"

	elif [[ "$answer" =~ "flower" ]]
	then
		flowerout="$(ps aux | grep "--ignore-case" flower)"
		echo "Flower Processes: "
		echo -en '\n'
		echo "${flowerout}"

	elif [[ "$answer" =~ "mongo" ]]
	then
		mongoout="$(ps aux | grep "--ignore-case" mongod | grep -v mongod-malaysia)"
		mongomyout="$(ps aux | grep "--ignore-case" mongod-malaysia)"
		echo "MongoDB Processes: "
		echo -en '\n'
		echo "Singapore Monogd: "
		echo "${mongoout}"
		echo "Malaysia Mongod "
		echo "${mongomyout}"

	elif [[ "$answer" =~ "exit" ]] 
	then
		let "i++"
		echo "Goodbye, cruel world"
	else
		echo "Not really sure what you want me to do, can you try again?"
	fi
done