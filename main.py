from api import RiotAPI
import json
from pprint import pprint

def main():
    winRates = {}
    itemRates = {}
    gameID = [getGameIds('5.11'), getGameIds('5.14')]
    for patch in gameID:
        for game in gameID[patch]:
            gameData = getGameInfo(game)
            #dosomething with gameData




if __name__ == "__main__":
    main()

def getGameIds(patch):
    with open('AP_ITEM_DATASET/' + patch + '/RANKED_SOLO/NA.json') as data_file:    
        data = json.load(data_file)
    # pprint(data)
    return data

def getGameInfo(id):
    api = RiotAPI("b428aebe-05e5-4353-b569-980bcbeaa394", "na")
    response = api.getMatch("match", id)
    pprint(response)
    return response

getGameInfo(getGameIds('5.11')[0])
