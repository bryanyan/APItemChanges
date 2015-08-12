from api import RiotAPI

def main():
	api = RiotAPI("b428aebe-05e5-4353-b569-980bcbeaa394", "na")
	response = api.getSummoner("byliza", "summoner")
	print response

if __name__ == "__main__":
	main()

