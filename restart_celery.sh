#!/bin/bash
# Script to restart celery and gunicorn.

# Force a while loop,

# Case Insensetive
shopt -s nocasematch

i=0
while [[ "$i" -ne 1 ]]
do
	echo "Which process do you want to kill?(SG/MY)"
	read answer
	if [[ "$answer" =~ "SG" ]]
	then
		cd '/synagie'
		echo 'Moved into syn folder'
		echo "Do you want to kill celery and it's API? (Y/N)"
		read celeryanswer
			if [[ "$celeryanswer"  =~ "Y" ]]
			then 
				#kills celery
				pkill -f '/usr/bin/python3 /usr/local/bin/celery -A synagie.celery worker -f /log/synagie/celery/synagie_celery.log' -9
				echo "Celery Killed"
				#kills celery API
				pkill -f '/usr/bin/python3 /usr/local/bin/celery -A synagie_api.celery worker -f /log/synagie_api/celery/synagie_api_celery.log' -9
				echo "Celery API Killed"
				#brings up celery SG
				nohup celery -A synagie.celery worker -f /log/synagie/celery/synagie_celery.log > /dev/null 2>&1 &
				echo "Celery Singapore restarted"
				#brings up Celery SG API
				nohup celery -A synagie_api.celery worker -f /log/synagie_api/celery/synagie_api_celery.log > /dev/null 2>&1 &
				echo "Celery Singapore API restarted"

			fi
			#kills gunicorn
			pkill -f '/usr/bin/python3 /usr/local/bin/gunicorn -w 4 -b 127.0.0.1:9000 --timeout 1000 synagie:app singapore' -9 
			echo "Gunicorn SG killed"
			#starts gunicorn
			nohup gunicorn -w 4 -b 127.0.0.1:9000 --timeout 1000 synagie:app singapore > /dev/null 2>&1 &
			echo "Gunicorn SG started"
			i=$((i+1))

	elif [[ "$answer" =~ "MY" ]]
	then
		cd '/synagie'
                echo 'Moved into syn folder'
                echo "Do you want to kill celery and it's API? (Y/N)"
                read celeryanswer
			if [[ "$celeryanswer" =~ "Y" ]]
			then
				#kills celery kills celery
                                pkill -f '/usr/bin/python3 /usr/local/bin/celery -A synagie.celery worker -f /log/synagie/celery/synagie_celery_malaysia.log --malaysia' -9
                                echo "Celery MY Killed"
                                #kills celery API
                                pkill -f '/usr/bin/python3 /usr/local/bin/celery -A synagie_api.celery worker -f /log/synagie_api/celery/synagie_api_celery_malaysia.log --malaysia' -9
                                echo "Celery MY API Killed"
                                #brings up celery MY
                                nohup celery -A synagie.celery worker -f /log/synagie/celery/synagie_celery_malaysia.log --malaysia > /dev/null 2>&1 &
                                echo "Celery Malaysia restarted"
                                #brings up Celery MY API
                                nohup celery -A synagie_api.celery worker -f /log/synagie_api/celery/synagie_api_celery_malaysia.log --malaysia > /dev/null 2>&1 &
                                echo "Celery Malaysia API restarted"
			fi
			#kills gunicorn Malaysia
			pkill -f '/usr/bin/python3 /usr/local/bin/gunicorn -w 4 -b 127.0.0.1:19000 --timeout 500 synagie:app malaysia' -9
			echo "Gunicorn malaysia killed"
			nohup gunicorn -w 4 -b 127.0.0.1:19000 --timeout 500 synagie:app malaysia > /dev/null 2>&1 &
			echo "Gunicorn Malaysia restarted"
			i=$((i+1))
	fi
done
