# Random-Scripts
## Taxscript.py
* A terminal python3 script written to calculate taxes based on the values as of 170928.
* Written to help someone in CryptoSGSpam chat

## commision.py
* A terminal python3 script to extract data from xls file and calculate ( and return values ).
* Using foo.xls

## examscore.py
* A terminal python3 script to calculate exam score based on input.

## email_crypto_price.php
* A php script run as cronjob to check crypto prices for LTC and ETH
* Written for a friend going on holiday.
* Once it hits a certain price point it **will send an email every 5 minutes**
* run as cronjob.

## determine_c.sh
* Celery has been exiting quietly with an exit code of 70 recently
* We are unable to determine why yet. This bash script is a stop gap measure while we work on resolving it
* This bash script scans the celery logs if the last 2 lines contain the word "Exit code 70"
* If so, it uses pkill to kill the relevant celery worker and then restart it with nohup.
* It also activates a php script to send a mail to inform us that it went down at this timing.
