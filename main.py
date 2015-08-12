from api import RiotAPI
import json
from pprint import pprint

API_KEY = "b428aebe-05e5-4353-b569-980bcbeaa394"

def getGameIds(patch):
    with open('AP_ITEM_DATASET/' + patch + '/RANKED_SOLO/NA.json') as data_file:    
        data = json.load(data_file)
    # pprint(data)
    return data

def getGameInfo(id):
    api = RiotAPI(API_KEY, "na")
    response = api.getMatch("match", id)
    pprint(response)
    return response

def main():
    patches = ['5.11', '5.14']
    winRates = {}
    itemRates = {}
    gameID = [getGameIds(patches[0]), getGameIds(patches[1])]
    for patch in gameID:
        for game in patch:
            gameData = getGameInfo(game)
            #dosomething with gameData


if __name__ == "__main__":
    main()




getGameInfo(getGameIds('5.11')[0])
