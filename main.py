from api import RiotAPI
import io, json
import time
from pprint import pprint
import copy

API_KEY = "637897ec-2820-4790-bf2c-984f1e0bf98f"

def getGameIds(patch):
    with open('AP_ITEM_DATASET/' + patch + '/RANKED_SOLO/EUW.json') as data_file:    
        data = json.load(data_file)
    # pprint(data)
    return data

def getGameInfo(id):
    api = RiotAPI(API_KEY, "euw")
    response = api.getMatch("match", id)
    #pprint(response)
    return response

def getLeagueInfo(id):
    api = RiotAPI(API_KEY, "na")
    response = api.getLeague("league", id)
    return response

def main():
    patches = ['5.11', '5.14']
    count = 0
    gameID = [getGameIds(patches[1])]
    
    for patch in gameID:
        gameNumber = 0
        for game in patch:
            gameNumber += 1
            count += 1
            if (count == 2800):
                count = 0
                time.sleep(10)
            try:
                gameData = getGameInfo(game)
                with io.open('EUWgameNumber%d.json' %(gameNumber), 'w', encoding='utf-8') as fout:
                    fout.write(unicode(json.dumps(gameData, ensure_ascii=False)))
            except:
                continue

def parse():
    i = 1
    tiers = ["bronze", "silver", "gold", "plat", "diamond", "master", 
            "challenger"]

    with open('champions.json') as champFile:
        champions = json.load(champFile)

    initialize = {}
    for champ in champions:
        initialize[champions[champ]['key']] = {
                        "pick": 0,
                        "wins": 0, 
                        "bans": 0, 
                        "totalDamageDealtToChampions": 0, 
                        "magicDamageDealtToChampions": 0,
                        "goldEarned": 0,
                        "duration": 0,
                        "kills": 0,
                        "deaths": 0,
                        "assists": 0,
                        "neutralMinionsKilled": 0,
                        "name": champ
                        }

    for index in xrange(7):
        temp = copy.deepcopy(initialize)
        tiers[index] = temp

#########################################
#fix efficiency
#########################################

    #while (i < 10002):
    #try:
    with open('FULL_GAMES_JSON/5.11/NA/gameNumber%d.json' %(i)) as data_file:
        data = json.load(data_file)
    requestString = ""
    tDict = {}
    for participant in data['participantIdentities']:
        requestString += str(participant['player']['summonerId'])
        tDict[str(participant['player']['summonerId'])] = [participant['participantId'], None] 
        requestString += ","
    requestString = requestString[:-1]
    league = getLeagueInfo(requestString)
    for key in league.keys():
        medal = league[key][0]['tier']
        for identity in tDict:
            if key == identity:
                tDict[identity][1] = medal
    
    for player in data['participants']:
        for playerID in tDict:
            if player['participantId'] == tDict[playerID][0]:
                if tDict[playerID][1] == 'BRONZE':
                    tiers[0][str(player['championId'])]['pick'] += 1
                if tDict[playerID][1] == 'SILVER': 
                    tiers[1]
                if tDict[playerID][1] == 'GOLD': 
                    tiers[2]
                if tDict[playerID][1] == 'PLATINUM': 
                    tiers[3]
                if tDict[playerID][1] == 'DIAMOND': 
                    tiers[4]
                if tDict[playerID][1] == 'MASTER': 
                    tiers[5]
                if tDict[playerID][1] == 'CHALLENGER': 
                    tiers[6]


    #except:
        #continue

    #with io.open('NAdata.json', 'w', encoding='utf-8') as fout:
        #fout.write(unicode(json.dumps(NAdata, ensure_ascii=False)))

#if __name__ == "__main__":
    #main()

#def hardcode():
    #data = getGameInfo(getGameIds('5.11')[2])
    #with io.open('gameNumber3.json', 'w', encoding='utf-8') as fout:
        #fout.write(unicode(json.dumps(data, ensure_ascii=False)))


parse()
