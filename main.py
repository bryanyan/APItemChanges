from api import RiotAPI

def main():
	api = RiotAPI("b428aebe-05e5-4353-b569-980bcbeaa394", "na")
	response = api.getMatch("match", "1852548676")
	print response

if __name__ == "__main__":
	main()

