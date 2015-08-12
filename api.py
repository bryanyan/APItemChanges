import requests
import constants as const

class RiotAPI(object):

	def __init__(self, api_key, region):
		self.api_key = api_key
		self.region = region

	def _request(self, apiUrl, params={}):
		args = {"api_key": self.api_key}
		for key, value in params.items():
			if key not in args:
				args[key] = value
		response = requests.get(const.URL['base'].format(
				proxy=self.region,region=self.region,url=apiUrl),params=args)
		return response.json()

	def getSummoner(self, username, apiVersion):
		apiUrl = const.URL['summoner'].format(
				 version=const.API_VERSIONS[apiVersion],username=username)
		return self._request(apiUrl)
