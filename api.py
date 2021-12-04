__author__ = 'poggersbutnot | Karim'
__version__ = '3.2.3'
import requests, sys, os, random, json, time, string, urllib, warnings
if not(requests.get('https://raw.githubusercontent.com/poggersbutnot/PG3D-Python-API/main/Info/version.info').text.rstrip('\n') == vars()['__version__']):
    warnings.warn('This API has an Update! https://github.com/poggersbutnot/PG3D-Python-API/')

urls = {
    'PB': 'https://secure.pixelgunserver.com/pixelgun3d-config/PixelBookSettings/PixelBookSettings_',
    'LB': 'https://secure.pixelgunserver.com/pixelgun3d-config/lobbyNews/LobbyNews_',
    'BAN': 'https://secure.pixelgunserver.com/pixelgun3d-config/getBanList.php',
    'CNFG': 'https://cfg.pixelgun3d.com/config.json',
    'BAL': 'https://secure.pixelgunserver.com/pixelgun3d-config/balance/balance_test.json',
    'PROM': 'https://secure.pixelgunserver.com/pixelgun3d-config/PromoActions/promo_actions_',
    'AD': 'https://secure.pixelgunserver.com/pixelgun3d-config/advert-v2/advert-',
    'CB': 'https://secure.pixelgunserver.com/pixelgun3d-config/chestBonus/chest_bonus_',
    'OS': 'https://secure.pixelgunserver.com/pixelgun3d-config/BuffSettings1031/BuffSettings_',
    'BS': 'https://secure.pixelgunserver.com/pixelgun3d-config/BuffSettings1050/BuffSettings_',
    'RC2': 'https://secure.pixelgunserver.com/pixelgun3d-config/ratingConfig_V2/rating_',
    'GEO': 'https://geoip.lightmap.ru/get_geo_info.php',
    'MS': 'https://secure.pixelgunserver.com/mapstats/mapstat.json',
    'ABC': 'https://secure.pixelgunserver.com/pixelgun3d-config/ABTests/abTestAdvert/abtestconfig_',
    'BRA': 'https://secure.pixelgunserver.com/pixelgun3d-config/daysOfValor/days_of_valor_',
    'ST': 'https://pixelgun-cl-stat.pixelgunserver.com/event_stat_add_pl.php'
    
}

def strictEquals(object1, types, enter):
    return (type(object1)==type(types) and object1 == enter)

def deleteNonAscii(string):
    return ''.join([i if ord(i) < 128 else ' ' for i in  string.decode('cp1250')])[2:]

def quoteJson(object1: dict, object2: dict):
    return urllib.parse.quote(json.dumps([object1,object2]))

def replaceNullBytes(content: bytes):
    return content.replace(b'\x00', b'')

def replaceAndroid(ostype: str):
    return ostype.replace('android', 'androd')

def counterReplaceAndroid(ostype: str):
    return ostype.replace('androd', 'android')

def removeAmazon(ostype: str):
    return ostype.replace('amazon', 'androd')

def strictOsTypes():
    return ['android', 'test', 'amazon']

def getOsTypes():
    return ['android', 'ios', 'test', 'amazon']
if (len(sys.argv) == 2):
    OS = sys.argv[1]
else:
    OS = random.choice(getOsTypes()) ; print('You have not selected an osType... It has been automatically configured to ostype ' +
                                             OS) ;
    print('REM To select an OS Type: (' + ', '.join(getOsTypes()) + '). Do: \ncd ' + sys.argv[0].replace(os.path.basename(__file__), '') + '\n' + sys.argv[0][:2] + '\npython ' + os.path.basename(__file__) + ' <ostype>')

if (OS not in getOsTypes()):
    randomOS = random.choice(getOsTypes()) ; print('You inputed: ' + sys.argv[1] + '. The Actual OS Types Are: ' +
                                                   '(' + ', '.join(getOsTypes()).replace('androd', 'android') + ')') ; print('Setting OS to ' + randomOS)
    OS = randomOS

blockedThreadedOs = replaceAndroid(random.choice(strictOsTypes()))

print('%s %s' % ('Script Launched!', requests.get('https://raw.githubusercontent.com/poggersbutnot/PG3D-Python-API/main/Info/updates.info').text.rstrip('\n')))

def getMaxFriendCount():
    print('Running ' + sys._getframe().f_code.co_name) ; return requests.get(urls['PB'] + replaceAndroid(OS) + '.json').json()['MaxFriendCount']

def getOldMaxClanMembers():
     print('Running ' + sys._getframe().f_code.co_name) ; return requests.get(urls['PB'] + replaceAndroid(OS) + '.json').json()['MaxMemberClanCount']

def getBlockedPackages():
    print('Running ' + sys._getframe().f_code.co_name)
    if (OS == 'ios') or (OS=='amazon'):
        randomOs = replaceAndroid(random.choice(strictOsTypes()))
        print('This feature is not availible for ' + OS + '... Replacing to osType ' +
              randomOs)
        return requests.get(urls['PB'] + randomOs + '.json').json()['JoinBaseResponseOn']
    else:
         return requests.get(urls['PB'] + replaceAndroid(OS) + '.json').json()['JoinBaseResponseOn']

def getFpsIds(alert=True):
    if alert is True:
        print('Running ' + sys._getframe().f_code.co_name)
    if (OS == 'ios') or (OS=='amazon'):
        randomOs = removeAmazon(counterReplaceAndroid(blockedThreadedOs))
        print('This feature is not availible for ' + OS + '... Replacing to osType ' +
              counterReplaceAndroid(randomOs))
        return requests.get(urls['PB'] + replaceAndroid(randomOs) + '.json').json()['EnableFpsCounterIds']
    else:
         return requests.get(urls['PB'] + replaceAndroid(OS) + '.json').json()['EnableFpsCounterIds']

def getLoggedIds(alert=True):
    if alert is True:
        print('Running ' + sys._getframe().f_code.co_name)
    return requests.get(urls['PB'] + replaceAndroid(OS) + '.json').json()['EnableLogForIDs']

def getWebsocketLoggedIds(alert=True):
    if alert is True:
        print('Running ' + sys._getframe().f_code.co_name)
    if (OS == 'ios') or (OS=='amazon'):
        randomOs = removeAmazon(counterReplaceAndroid(blockedThreadedOs))
        print('This feature is not availible for ' + OS + '... Replacing to osType ' +
              counterReplaceAndroid(randomOs))
        return requests.get(urls['PB'] + replaceAndroid(randomOs) + '.json').json()['EnableWebSocketLogForIDs']
    else:
         return requests.get(urls['PB'] + replaceAndroid(OS) + '.json').json()['EnableWebSocketLogForIDs']

def getIsLoggedIdsBanned():
    print('Running ' + sys._getframe().f_code.co_name)
    pushed = []
    for i in range(len(getLoggedIds(False))):
        if requests.post(urls['BAN'], data = {
             'type_device': int(random.random() * 15//1),
             'id': getLoggedIds(False)[i]
            }).text == '1':
            pushed.append(getLoggedIds(False)[i] + ' is Banned')
        else:
             pushed.append(getLoggedIds(False)[i] + ' is not Banned')
        print(str(round((i + 1) * 100 / len(getLoggedIds(False)))) + ' % completed')
    string = ""
    for i in range(len(pushed)):
        string += pushed[i] + '\n'
    return string[:-1]

def getIsFpsIdsBanned():
    print('Running ' + sys._getframe().f_code.co_name)
    pushed = []
    for i in range(len(getFpsIds(False))):
        if requests.post(urls['BAN'], data = {
             'type_device': int(random.random() * 15//1),
             'id': getFpsIds(False)[i]
            }).text == '1':
            pushed.append(getFpsIds(False)[i] + ' is Banned')
        else:
             pushed.append(getFpsIds(False)[i] + ' is not Banned')
        print(str(round((i + 1) * 100 / len(getFpsIds(False)))) + ' % completed')
    string = ""
    for i in range(len(pushed)):
        string += pushed[i] + '\n'
    return string[:-1]

def getLatestVersion():
    print('Running ' + sys._getframe().f_code.co_name)
    response = requests.get(urls['CNFG']).json()
    if not(response == []):
        return response[0]
    else:
        return None

def getIsWebsocketLoggedIdsBanned():
    print('Running ' + sys._getframe().f_code.co_name)
    pushed = []
    for i in range(len(getWebsocketLoggedIds(False))):
        if requests.post(urls['BAN'], data = {
             'type_device': int(random.random() * 15//1),
             'id': getWebsocketLoggedIds(False)[i]
            }).text == '1':
            pushed.append(getWebsocketLoggedIds(False)[i] + ' is Banned')
        else:
             pushed.append(getWebsocketLoggedIds(False)[i] + ' is not Banned')
        print(str(round((i + 1) * 100 / len(getWebsocketLoggedIds(False)))) + ' % completed')
    string = ""
    for i in range(len(pushed)):
        string += pushed[i] + '\n'
    return string[:-1]

def getOldLobbyNews():
    print('Running ' + sys._getframe().f_code.co_name)
    return requests.get(urls['LB'] + replaceAndroid(OS) + '.json').json()

def getBalanceData():
    print('Running ' + sys._getframe().f_code.co_name) ; return requests.get(urls['BAL']).json()

def getWeaponPromotionData():
    print('Running ' + sys._getframe().f_code.co_name) ; return requests.get(urls['PROM'] + OS + '.json').json()

def getWeaponExtraPromotionData():
    print('Running ' + sys._getframe().f_code.co_name) ; return requests.get(urls['PROM'] + 'test.php').json()

def getDisabledDevices():
    print('Running ' + sys._getframe().f_code.co_name) ; return requests.get(urls['AD'] + OS + '.json').json()["interstitials"]["disableDevices"]

def getCheaterThresholdData():
     print('Running ' + sys._getframe().f_code.co_name) ; return requests.get(urls['AD'] + OS + '.json').json()["cheater"]

def isBanned(userid: str):
    print('Running ' + sys._getframe().f_code.co_name)
    response = requests.post(urls['BAN'], data = {
        'type_device': int(random.random() * 15//1),
        'id': userid
        }).text
    if strictEquals(response, chr(32), '1'):
        return True
    else:
        return False

def freeCurrencyTypeRotation():
     print('Running ' + sys._getframe().f_code.co_name) ; return requests.get(urls['AD'] + OS + '.json').json()["points"]["chestInLobby"]["rewardCurrencies-v4"]

def getStartingSandboxItems():
     print('Running ' + sys._getframe().f_code.co_name) ; return requests.get(urls['CB'] + 'test.json').json()["bonuses"][0]["items"]

def getBuffOldWeaponsData(payedUser: bool = True):
    print('Running ' + sys._getframe().f_code.co_name)
    if (payedUser is True):
        return requests.get(urls['OS'] + OS + '_paying.json').json()
    else:
        return requests.get(urls['OS'] + OS + '.json').json()

def getBuffWeaponsData(payedUser: bool = True):
    print('Running ' + sys._getframe().f_code.co_name)
    if (payedUser is True):
        return requests.get(urls['BS'] + OS + '_paying.json').json()
    else:
        return requests.get(urls['BS'] + OS + '.json').json()

def getLocationInfo():
     print('Running ' + sys._getframe().f_code.co_name) ; return requests.get(urls['GEO']).json()

def getTrophieLadderStages():
    print('Running ' + sys._getframe().f_code.co_name) ; return requests.get(urls['RC2'] + OS + '.json').json()["A"]["ALL"]["Rating"]

def getPenaltyLeave():
    print('Running ' + sys._getframe().f_code.co_name) ; return requests.get(urls['RC2'] + OS + '.json').json()["A"]["Penalty"]

def getBanDurations():
    print('Running ' + sys._getframe().f_code.co_name) ; return requests.get(urls['RC2'] + OS + '.json').json()["B"]["Ban"]

def getMapData():
    print('Running ' + sys._getframe().f_code.co_name) ; return requests.get(urls['MS']).json()

def decodeAuth(content: bytes):
    print('Running ' + sys._getframe().f_code.co_name)
    n = replaceNullBytes(content)
    for l in range(257):
        f = bytes([(c+l)%256 for c in n])
        if b'token' in f:
            return deleteNonAscii(f)
        elif b'model' in f:
            return deleteNonAscii(f)
        elif b'1403' in f:
            return deleteNonAscii(f)

def getBrawlData():
    print('Running ' + sys._getframe().f_code.co_name) ; return requests.get(urls['BRA'] + OS + '.json').json()

def updateLog(ids: int, dev: str = '1', ver: str = '', keys: str = '9999',
         gems: str = '9999', killRates: float = 100.0, coins: str = '9999'):
    print('Running ' + sys._getframe().f_code.co_name) ; timer = round(time.time())
    params = quoteJson({"cmid": 51, "eid": 3, "uid": ids, "dev": dev, "c": "SGP", "p": 0, "v": ver,
                        "r": 7, "cid": "21084402", "t": timer, "reg": timer, "pl": 1,
                        "ip1": 20, "ip2": 120135, "ip3": 6, "ip4": 30335, "sp1": "0 0:32:15",
                        "jp1": {"Primary": 10001, "Backup": 1001, "Melee": 9001, "Specil": 333001,
                                "Sniper": 67001, "Premium": 695001},
                        "jp2": {"cr": 45, "keys": keys, "gems": gems, "cps": 0, "c_s": 0, "w_s": 0,
                                "e_s": 1, "coins": coins}, "ip5": 0, "ip6": 10, "sp2": "Soldier", "sp3": "Newbie",
                        "jo": {"Killrates": {"total": killRates, "br": 1}}},
                       {"cmid": 401, "eid": 1, "uid": ids, "dev": dev, "c": "SGP", "p": 0, "v": ver,
                        "r": 7, "cid": "21084402", "t": timer, "reg": timer, "pl": 1,
                        "ip1": 20, "ip2": 120135, "ip3": 6, "ip4": 30335, "ip5": 20,
                        "sp1": 'poggersbutnot',
                        "sp2": "poggersbutnot",
                        "sp3": "{'Killrates':{'total':" + str(killRates) + "}}",
                        "jp1": {"cr": 45, "keys": keys, "gems": gems, "cps": 0, "c_s": 0, "w_s": 0,
                                "e_s": 1, "coins": coins},
                        "jp2": {"Primary": 10001, "Backup": 1001, "Melee": 9001, "Specil": 333001,
                                "Sniper": 67001, "Premium": 695001}, "ip6": 0, "sp4": "Soldier"})
    g = requests.post(urls['ST'], params='muid=' + str(ids) + '&events=' + params)
    o = 'Status '
    if 'ok' in g.text:
        return o + g.text.lstrip('\n')
    else:
        return o + g.text.lstrip('\n')
