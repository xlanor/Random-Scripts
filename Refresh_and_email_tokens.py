#!/usr/bin/env python3
#
# ===========Script Description=============
# Auto-refreshes tokens for lazada merchants.
# Only for merchants that exists in our db
# Last update - Mar 29 by Jing Kai.


import config.synagie_api_prod as config_file
import MySQLdb,json,smtplib,traceback
from contextlib import closing
import initial_lazada_sdk as lazOps

class getRecords:
	def __init__(self):
		self.__DB_CONFIG = {
		  'host': config_file.SERVER,
		  'db': config_file.DATABASE,
		  'user': config_file.USERNAME,
		  'passwd': config_file.PASSWORD
		}

	def getLazadaRecords(self):
		return_array = []
		with closing(MySQLdb.connect(**self.__DB_CONFIG)) as conn:
			conn.autocommit(True)
			with closing(conn.cursor()) as cur:
				"""
				ACHTUNG! Note that our db was not designed for this in the first place, originally. 
				Because of other marketplaces.
				The "access_token" field in our database is actually the refresh_token for lazada, and
				the credentials is the access token.
				¯\\_(ツ)_/¯ 
				"""
				cur.execute("""SELECT user_id, credentials,access_token 
								FROM UserChannel 
								WHERE channel_id = %s 
								AND access_token <> %s""",(1,'',))
				if cur.rowcount > 0:
					list_of_users = cur.fetchall()
					for user in list_of_users:
						return_array.append({"id":user[0],"access_token":user[1],"refresh_token":user[2]})
		return return_array

	def updateDb(self,user_id,new_access_token,new_refresh_token):
		with closing(MySQLdb.connect(**self.__DB_CONFIG)) as conn:
			conn.autocommit(True)
			with closing(conn.cursor()) as cur:
				# Because the db design was flipped, access token is actually refresh token
				cur.execute("""UPDATE UserChannel 
								SET credentials = %s, access_token = %s 
								WHERE account = %s""",(new_access_token,new_refresh_token,user_id,))
				return "Updated Details for {}".format(user_id)


class refreshTokens(getRecords):
	def __init__(self):
		getRecords.__init__(self)
		self.__list_of_users = getRecords.getLazadaRecords(self)
		print ("Retrieved List of Users")

	def send_refresh_token(self):
		response_array = []
		for user in self.__list_of_users:
			client = lazOps.LazopClient('https://api.lazada.com/rest','<app_key>','<app_secret_key>')
			requestObj = lazOps.LazopRequest('/auth/token/refresh')
			requestObj.add_api_param('refresh_token',user['refresh_token']);
			response = client.execute(requestObj)
			response_dict = json.loads(response.text)
			print(response_dict)
			if "code" in response_dict and response_dict["code"] == "0":
				return_message = getRecords.updateDb(self,user["id"],response_dict["access_token"],response_dict["refresh_token"])
				response_array.append({"id":user["id"],"message":return_message})
				print("{} completed refresh".format(user["id"]))
			else:
				response_array.append({"id":user["id"],"message":json.dumps(response_dict)})
				print("{} failed refresh".format(user["id"]))
			
		return response_array

class sendMail:
	def __init__(self):
		self.__smtpHost = config_file.SMTP_HOST
		self.__smtpMail = config_file.SMTP_EMAIL
		self.__smtpMailPw = config_file.SMTP_PASSWORD
		self.__recipients = ['receipient@email.com','recipient2@email.com']

	def send_non_exception_mail(self,result_array):
		if len(result_array) > 0:
			message = ("From: %s\r\nTo: %s\r\nMIME-Version: 1.0\r\nContent-Type: text/html\r\nSubject: %s\r\n\r\n"  
				  % (self.__smtpMail, ", ".join([]),"Lazada Merchant Refresh Result"))
			body = ""
			for result in result_array:
				body += result["message"]
				body += "\n"
			message += body
			smtpObj = smtplib.SMTP_SSL(self.__smtpHost,465)
			smtpObj.login(self.__smtpMail, self.__smtpMailPw)
			for recipient in self.__recipients:
				smtpObj.sendmail(self.__smtpMail, recipient, message)
			smtpObj.close() 

	def send_exception_mail(self,traceback_string):
		message = ("From: %s\r\nTo: %s\r\nMIME-Version: 1.0\r\nContent-Type: text/html\r\nSubject: %s\r\n\r\n"  
				  % (self.__smtpMail, ", ".join([]),"Lazada Merchant Refresh Error"))
		smtpObj = smtplib.SMTP_SSL(self.__smtpHost,465)
		smtpObj.login(self.__smtpMail, self.__smtpMailPw)
		message += traceback_string
		for recipient in self.__recipients:
			smtpObj.sendmail(self.__smtpMail, recipient,message)
		smtpObj.close() 

if __name__ == "__main__":
	try:
		refreshResult = refreshTokens().send_refresh_token()
		sendMail().send_non_exception_mail(refreshResult)
	except:
		sendMail().send_exception_mail(traceback.format_exec())
