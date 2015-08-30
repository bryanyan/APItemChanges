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
            "challenger", "overall"]

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

    for index in xrange(8):
        temp = copy.deepcopy(initialize)
        tiers[index] = temp

#########################################
#fix efficiency
#########################################

    league_api = 0

    while (i <= 10001):
        try:
            if league_api == 2800:
                league_api = 0
                time.sleep(10)
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
            league_api += 1
            for key in league.keys():
                medal = league[key][0]['tier']
                for identity in tDict:
                    if key == identity:
                        tDict[identity][1] = medal

            bans = []
            oppbans = []
            for t1ban in data['teams'][0]['bans']:
                bans.append(t1ban['championId'])
            for t2ban in data['teams'][1]['bans']:
                oppbans.append(t2ban['championId'])

            for banned in bans:
                tiers[7][str(banned)]['bans'] += 1
            for obanned in oppbans:
                tiers[7][str(obanned)]['bans'] += 1

            for player in data['participants']:
                for playerID in tDict:
                    if player['participantId'] == tDict[playerID][0]:
                        value = str(player['championId'])
                        if tDict[playerID][1] == 'BRONZE':
                            tiers[0][value]['pick'] += 1
                            tiers[0][value]['assists'] += player['stats']['assists']
                            tiers[0][value]['kills'] += player['stats']['kills']
                            tiers[0][value]['deaths'] += player['stats']['deaths']
                            tiers[0][value]['totalDamageDealtToChampions'] += player['stats']['totalDamageDealtToChampions']
                            tiers[0][value]['magicDamageDealtToChampions'] += player['stats']['magicDamageDealtToChampions']
                            tiers[0][value]['goldEarned'] += player['stats']['goldEarned']
                            tiers[0][value]['neutralMinionsKilled'] += player['stats']['neutralMinionsKilled']
                            tiers[0][value]['duration'] += data['matchDuration']
                            if player['stats']['winner'] == True:
                                tiers[0][value]['wins'] += 1
                        elif tDict[playerID][1] == 'SILVER': 
                            tiers[1][value]['pick'] += 1
                            tiers[1][value]['assists'] += player['stats']['assists']
                            tiers[1][value]['kills'] += player['stats']['kills']
                            tiers[1][value]['deaths'] += player['stats']['deaths']
                            tiers[1][value]['totalDamageDealtToChampions'] += player['stats']['totalDamageDealtToChampions']
                            tiers[1][value]['magicDamageDealtToChampions'] += player['stats']['magicDamageDealtToChampions']
                            tiers[1][value]['goldEarned'] += player['stats']['goldEarned']
                            tiers[1][value]['neutralMinionsKilled'] += player['stats']['neutralMinionsKilled']
                            tiers[1][value]['duration'] += data['matchDuration']
                            if player['stats']['winner'] == True:
                                tiers[1][value]['wins'] += 1
                        elif tDict[playerID][1] == 'GOLD': 
                            tiers[2][value]['pick'] += 1
                            tiers[2][value]['assists'] += player['stats']['assists']
                            tiers[2][value]['kills'] += player['stats']['kills']
                            tiers[2][value]['deaths'] += player['stats']['deaths']
                            tiers[2][value]['totalDamageDealtToChampions'] += player['stats']['totalDamageDealtToChampions']
                            tiers[2][value]['magicDamageDealtToChampions'] += player['stats']['magicDamageDealtToChampions']
                            tiers[2][value]['goldEarned'] += player['stats']['goldEarned']
                            tiers[2][value]['neutralMinionsKilled'] += player['stats']['neutralMinionsKilled']
                            tiers[2][value]['duration'] += data['matchDuration']
                            if player['stats']['winner'] == True:
                                tiers[2][value]['wins'] += 1
                        elif tDict[playerID][1] == 'PLATINUM': 
                            tiers[3][value]['pick'] += 1
                            tiers[3][value]['assists'] += player['stats']['assists']
                            tiers[3][value]['kills'] += player['stats']['kills']
                            tiers[3][value]['deaths'] += player['stats']['deaths']
                            tiers[3][value]['totalDamageDealtToChampions'] += player['stats']['totalDamageDealtToChampions']
                            tiers[3][value]['magicDamageDealtToChampions'] += player['stats']['magicDamageDealtToChampions']
                            tiers[3][value]['goldEarned'] += player['stats']['goldEarned']
                            tiers[3][value]['neutralMinionsKilled'] += player['stats']['neutralMinionsKilled']
                            tiers[3][value]['duration'] += data['matchDuration']
                            if player['stats']['winner'] == True:
                                tiers[3][value]['wins'] += 1
                        elif tDict[playerID][1] == 'DIAMOND': 
                            tiers[4][value]['pick'] += 1
                            tiers[4][value]['assists'] += player['stats']['assists']
                            tiers[4][value]['kills'] += player['stats']['kills']
                            tiers[4][value]['deaths'] += player['stats']['deaths']
                            tiers[4][value]['totalDamageDealtToChampions'] += player['stats']['totalDamageDealtToChampions']
                            tiers[4][value]['magicDamageDealtToChampions'] += player['stats']['magicDamageDealtToChampions']
                            tiers[4][value]['goldEarned'] += player['stats']['goldEarned']
                            tiers[4][value]['neutralMinionsKilled'] += player['stats']['neutralMinionsKilled']
                            tiers[4][value]['duration'] += data['matchDuration']
                            if player['stats']['winner'] == True:
                                tiers[4][value]['wins'] += 1
                        elif tDict[playerID][1] == 'MASTER': 
                            tiers[5][value]['pick'] += 1
                            tiers[5][value]['assists'] += player['stats']['assists']
                            tiers[5][value]['kills'] += player['stats']['kills']
                            tiers[5][value]['deaths'] += player['stats']['deaths']
                            tiers[5][value]['totalDamageDealtToChampions'] += player['stats']['totalDamageDealtToChampions']
                            tiers[5][value]['magicDamageDealtToChampions'] += player['stats']['magicDamageDealtToChampions']
                            tiers[5][value]['goldEarned'] += player['stats']['goldEarned']
                            tiers[5][value]['neutralMinionsKilled'] += player['stats']['neutralMinionsKilled']
                            tiers[5][value]['duration'] += data['matchDuration']
                            if player['stats']['winner'] == True:
                                tiers[5][value]['wins'] += 1
                        elif tDict[playerID][1] == 'CHALLENGER': 
                            tiers[6][value]['pick'] += 1
                            tiers[6][value]['assists'] += player['stats']['assists']
                            tiers[6][value]['kills'] += player['stats']['kills']
                            tiers[6][value]['deaths'] += player['stats']['deaths']
                            tiers[6][value]['totalDamageDealtToChampions'] += player['stats']['totalDamageDealtToChampions']
                            tiers[6][value]['magicDamageDealtToChampions'] += player['stats']['magicDamageDealtToChampions']
                            tiers[6][value]['goldEarned'] += player['stats']['goldEarned']
                            tiers[6][value]['neutralMinionsKilled'] += player['stats']['neutralMinionsKilled']
                            tiers[6][value]['duration'] += data['matchDuration']
                            if player['stats']['winner'] == True:
                                tiers[6][value]['wins'] += 1
                        tiers[7][value]['pick'] += 1
                        tiers[7][value]['assists'] += player['stats']['assists']
                        tiers[7][value]['kills'] += player['stats']['kills']
                        tiers[7][value]['deaths'] += player['stats']['deaths']
                        tiers[7][value]['totalDamageDealtToChampions'] += player['stats']['totalDamageDealtToChampions']
                        tiers[7][value]['magicDamageDealtToChampions'] += player['stats']['magicDamageDealtToChampions']
                        tiers[7][value]['goldEarned'] += player['stats']['goldEarned']
                        tiers[7][value]['neutralMinionsKilled'] += player['stats']['neutralMinionsKilled']
                        tiers[7][value]['duration'] += data['matchDuration']
                        if player['stats']['winner'] == True:
                            tiers[7][value]['wins'] += 1
            i += 1
        except:
            i += 1

    for champkey in champions:
        with io.open('5.11NA%sOVERALL.json' %(champions[champkey]['name']), 'w', encoding='utf-8') as fout:
            fout.write(unicode(json.dumps(tiers[7][str(champions[champkey]['key'])], ensure_ascii=False)))

        with io.open('5.11NA%sBRONZE.json' %(champions[champkey]['name']), 'w', encoding='utf-8') as fout:
            fout.write(unicode(json.dumps(tiers[0][str(champions[champkey]['key'])], ensure_ascii=False)))

        with io.open('5.11NA%sSILVER.json' %(champions[champkey]['name']), 'w', encoding='utf-8') as fout:
            fout.write(unicode(json.dumps(tiers[1][str(champions[champkey]['key'])], ensure_ascii=False)))

        with io.open('5.11NA%sGOLD.json' %(champions[champkey]['name']), 'w', encoding='utf-8') as fout:
            fout.write(unicode(json.dumps(tiers[2][str(champions[champkey]['key'])], ensure_ascii=False)))

        with io.open('5.11NA%sPLATINUM.json' %(champions[champkey]['name']), 'w', encoding='utf-8') as fout:
            fout.write(unicode(json.dumps(tiers[3][str(champions[champkey]['key'])], ensure_ascii=False)))

        with io.open('5.11NA%sDIAMOND.json' %(champions[champkey]['name']), 'w', encoding='utf-8') as fout:
            fout.write(unicode(json.dumps(tiers[4][str(champions[champkey]['key'])], ensure_ascii=False)))

        with io.open('5.11NA%sMASTER.json' %(champions[champkey]['name']), 'w', encoding='utf-8') as fout:
            fout.write(unicode(json.dumps(tiers[5][str(champions[champkey]['key'])], ensure_ascii=False)))

        with io.open('5.11NA%sCHALLENGER.json' %(champions[champkey]['name']), 'w', encoding='utf-8') as fout:
            fout.write(unicode(json.dumps(tiers[6][str(champions[champkey]['key'])], ensure_ascii=False)))

#if __name__ == "__main__":
    #main()

#def hardcode():
    #data = getGameInfo(getGameIds('5.11')[2])
    #with io.open('gameNumber3.json', 'w', encoding='utf-8') as fout:
        #fout.write(unicode(json.dumps(data, ensure_ascii=False)))

parse()
