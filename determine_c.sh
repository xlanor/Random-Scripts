#!/bin/bash
# Script to determine if celery is down and restart + send mail
shopt -s expand_aliases
source ~/.bashrc
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PHP="/usr/bin/php"
#gets the last 2 lines from the log
celery1="$(tail -n 1 /log/synagie/celery/synagie_celery.log)"
celery2="$(tail -n 2 /log/synagie/celery/synagie_celery.log | head -1)"
celeryapi1="$(tail -n 1 /log/synagie_api/celery/synagie_api_celery.log)"
celeryapi2="$(tail -n 2 /log/synagie_api/celery/synagie_api_celery.log | head -1)"
mycelery1="$(tail -n 1 /log/synagie/celery/synagie_celery_malaysia.log)"
mycelery2="$(tail -n 2 /log/synagie/celery/synagie_celery_malaysia.log | head -1)"
myceleryapi1="$(tail -n 1 /log/synagie_api/celery/synagie_api_celery_malaysia.log)"
myceleryapi2="$(tail -n 2 /log/synagie_api/celery/synagie_api_celery_malaysia.log | head -1)"

#matches to check if exitcode 70
pattern="exitcode 70"
if [[ $celery1 =~ $pattern ]] || [[ $celery2 =~ $pattern ]];then
	# if present, kill celery Singapore and sleep for 20
	pkill -f '/usr/bin/python3 /usr/local/bin/celery -A synagie.celery worker -f /log/synagie/celery/synagie_celery.log' -9
	echo -e '\nCelery Singapore killed' >> /log/synagie/celery/synagie_celery.log
	#for debugging
	echo Celery Singapore Killed
	echo Beginning 20sec pause to ensure that celery is completely killed...
	#end for debugging
	sleep 20
	cd $DIR

	#reboot celery
	nohup celery -A synagie.celery worker -f /log/synagie/celery/synagie_celery.log > /dev/null 2>&1 &
	echo -e '\nCelery Singapore restarted' >> /log/synagie/celery/synagie_celery.log
	#for debugging
	echo 'Celery Singapore restarted'
	#end for debugging
	cd '/wordpress/jk_scripts/celery_bash'
	#Singapore site is the argument we pass in to php that will be used in the body of the mail
	$PHP /wordpress/jk_scripts/celery_bash/celery_email.php 'Singapore Site'
	echo 'Notification mail sent'
fi

if [[ $celeryapi1 =~ $pattern ]] || [[ $celeryapi2 =~ $pattern ]]; then
	#if present, kill celery Singapore API and sleepfor 20
	pkill -f '/usr/bin/python3 /usr/local/bin/celery -A synagie_api.celery worker -f /log/synagie_api/celery/synagie_api_celery.log' -9
	echo -e '\nCelery Singapore API killed' >> /log/synagie_api/celery/synagie_api_celery.log
	# for debugging
	echo Celery Singapore API killed
	echo Beginning 20sec pause to ensure that celery is completely killed...
	#end for debugging
	sleep 20
	cd $DIR

	#reboot celery
	nohup celery -A synagie_api.celery worker -f /log/synagie_api/celery/synagie_api_celery.log > /dev/null 2>&1 &
	echo -e '\nCelery Singapore API Restarted' >> /log/synagie_api/celery/synagie_api_celery.log
	#for debugging
	echo Celery Singapore API Started
	#end for debugging
	cd '/wordpress/jk_scripts/celery_bash'
	$PHP /wordpress/jk_scripts/celery_bash/celery_email.php 'Singapore API'
	echo 'Notification mail sent'
fi

if [[ $mycelery1 =~ $pattern ]] || [[ $mycelery2 =~ $pattern ]]; then
	#if present, kill celery Singapore API and sleepfor 20
	pkill -f '/usr/bin/python3 /usr/local/bin/celery -A synagie.celery worker -f /log/synagie/celery/synagie_celery_malaysia.log --malaysia' -9
	echo -e '\nCelery Malaysia Killed' >> /log/synagie/celery/synagie_celery_malaysia.log
	#for debugging
	echo Celery Malaysia killed
	echo Beginning 20sec pause to ensure that celery is completely killed...
	#end for debugging
	sleep 20
	cd $DIR

	#reboot celery
	nohup celery -A synagie.celery worker -f /log/synagie/celery/synagie_celery_malaysia.log --malaysia > /dev/null 2>&1 &
	echo -e '\nCelery Malaysia Restarted' >> /log/synagie/celery/synagie_celery_malaysia.log
	#for debugging
	echo Celery Malaysia Started
	#end for debugging
	cd '/wordpress/jk_scripts/celery_bash'
	$PHP /wordpress/jk_scripts/celery_bash/celery_email.php 'Malaysia Site'
	echo 'Notification mail sent'
fi

if [[ $myceleryapi1 =~ $pattern ]] || [[ $myceleryapi2 =~ $pattern ]]; then
	#if present, kill celery Singapore API and sleepfor 20
	pkill -f '/usr/bin/python3 /usr/local/bin/celery -A synagie_api.celery worker -f /log/synagie_api/celery/synagie_api_celery_malaysia.log --malaysia' -9
	echo -e '\nCelery Malaysia API killed' >> /log/synagie_api/celery/synagie_api_celery_malaysia.log
	#for debugging
	echo Celery Malaysia API killed
	echo Beginning 20sec pause to ensure that celery is completely killed...
	#end for debugging
	sleep 20
	cd $DIR

	#reboot celery
	nohup celery -A synagie_api.celery worker -f /log/synagie_api/celery/synagie_api_celery_malaysia.log --malaysia > /dev/null 2>&1 &
	echo -e '\nCelery Malaysia API restarted' >> /log/synagie_api/celery/synagie_api_celery_malaysia.log
	#for debugging
	echo Celery Malaysia API Started
	#end for debugging
	cd '/wordpress/jk_scripts/celery_bash'
	$PHP /wordpress/jk_scripts/celery_bash/celery_email.php 'Malaysia API'
	echo 'Notification mail sent'
fi


