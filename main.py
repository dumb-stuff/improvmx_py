import requests
import aiohttp
import json
class WrongPatternToken(Exception):
	pass

class NoToken(Exception):
	pass

class TokenError(Exception):
	pass

class NoPermission(Exception):
	pass

class ServerError(Exception):
	pass
url = "https://api.improvmx.com/v3/"
tokenauth = ''
class SetUp(object):
	def __init__(self,token=None):
		if len(tokenauth) !=35 or len(tokenauth) == 0:
			print("Adding token")
			if token is None or len(token) == 0 or len(token) != 35:
				raise WrongPatternToken("You have wrong token or You did\'nt enter token.")
			else:
				tokenauth = token
		else:
			print("You already setup token!")
class Account(object):
	def __init__(self):
		if len(tokenauth) != 35:
			raise NoToken("We don\'t see any token that you input! You can do that by do call SetUp function")
		self.token = tokenauth
	def GetAccountDetail(self):
		r = requests.get(f"{url}account",headers={"Authorization":f"Basic api:{self.token}"})
		CheckResponse(r)
	def GetWhiteLabelDomain(self):
		r = requests.get(f"{url}account/whitelabels",headers={"Authorization":f"Basic api:{self.token}"})
		CheckResponse(r)
class Domains(object):
	def __init__(self):
		if len(tokenauth) != 35:
			raise NoToken("We don\'t see any token that you input! You can do that by call SetUp function!")
		self.token = tokenauth
		def ListDomains(self,query:str="",is_active:bool="",limit=50,page=1):
			r = requests.get(f"{url}domains?q={query}&is_active={is_active}&limit={limit}&page={page}",headers={"Authorization":f"Basic api:{self.token}"})
			CheckResponse(r)
		def AddDomain(self,domain:str,notify_email:str="",whitelabel:str=""):
			r = requests.post(f"{url}domains?domain={domain}&notification_email={notify_email}&whitelabel={whitelabel}",headers={"Authorization":f"Basic api:{self.token}"})
			CheckResponse(r)
		def DomainDetail(self,domain):
			r = requests.get(f"{url}domains/{domain}",headers={"Authorization":f"Basic api:{self.token}"})
			CheckResponse(r)
		def EditDomain(self,domain,notify_email:str="",whitelabel:str=""):
			r = requests.put(f"{url}domains/{domain}?",headers=dict)
class CheckResponse(object):
	def __init__(self,r):
		if r.status_code == 401:
			tokenauth = ''
			raise TokenError("Your token is unusable! Please set new token again.")
		if r.status_code == 403:
			raise NoPermission("You don\'t have enough permission to do this. You may need to subscribe pro or organization plan!")
		if r.status_code == 500:
			raise ServerError("Oops! The ImprovMX server is died or down or there\'s bug! Please try again later!")
		return json.loads(r.content.decode())