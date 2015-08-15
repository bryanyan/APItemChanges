from api import RiotAPI
import io, json
import time
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
    count = 0
    gameID = [getGameIds(patches[0]), getGameIds(patches[1])]
    
    for patch in gameID:
        gameNumber = 360
        for game in patch[359:]:
            gameNumber += 1
            count += 1
            gameData = getGameInfo(game)
            with io.open('gameNumber%d.json' %(gameNumber), 'w', encoding='utf-8') as fout:
                fout.write(unicode(json.dumps(gameData, ensure_ascii=False)))
            if (count == 8):
                count = 0
                time.sleep(10)

if __name__ == "__main__":
    main()

#def hardcode():
    #data = getGameInfo(getGameIds('5.11')[2])
    #with io.open('gameNumber3.json', 'w', encoding='utf-8') as fout:
        #fout.write(unicode(json.dumps(data, ensure_ascii=False)))
