import json
from typing import List, Optional
import interactor
import datetime as dt
import time

startTime = dt.datetime.now()

version = "1.0.11"
with open("devConfig.json", "r") as f:

    data = json.load(f)

    TOKEN = data["TOKEN"]
    HYPIXEL_API_KEY = data["HYPIXEL_API_KEY"]
    allowedChannels = data["allowedChannels"]
    linkFilter = data["linkFilter"]
    names = data["names"]
    loggingChannel = data["logging_channel"]
    swearIgnoredCategories = data["swearIgnoredCategories"]
    spamIgnoredCategories = data["spamIgnoredCategories"]
    nickChannel = data["nickChannel"]
    reportChannel = data["reportChannel"]
    mutedRole = data["mutedRole"]
    tradeBanRole = data["tradeBanRole"]
    silentVcRole = data["silentVcRole"]
    verifiedRole = data["verifiedRole"]
    modRole = data["modRole"]
    owner = data["owner"]
    confidenceThreshold = data["confidenceThreshold"]
    botCmdChannels = data["botCmdChannels"]
    sbBotCmdChannels = data["sbBotCmdChannels"]
    allowedWords = data["allowedWords"]
    hyRequestsMade = 0

with open("reallyBadWords.txt", "r") as f:
    blacklist0 = f.read().split("\n")

with open("maybeBadWords.txt", "r") as f:
    blacklist1 = f.read().split("\n")

afkConn = interactor.create_connection("afkDatabase.db")
tradeBanConn = interactor.create_connection("tradeBanned.db")
linkedAccountsConn = interactor.create_connection("linkedAccounts.db")

def getApiKey() -> str:
    return HYPIXEL_API_KEY

def getAllowedChannels() -> List[int]:
    return allowedChannels

def getLinkFilter() -> List[str]:
    return linkFilter

def getNames() -> List[str]:
    return names

def getLoggingChannel() -> Optional[int]:
    return loggingChannel

def getSwearIgnoredCategories() -> List[int]:
    return swearIgnoredCategories

def getSpamIgnoredCategories() -> List[int]:
    return spamIgnoredCategories

def getNickChannel() -> Optional[int]:
    return nickChannel

def getReportChannel() -> Optional[int]:
    return reportChannel

def getMutedRole() -> Optional[int]:
    return mutedRole

def getTradeBanRole() -> Optional[int]:
    return tradeBanRole

def getSilentVcRole() -> Optional[int]:
    return silentVcRole

def getVerifiedRole() -> Optional[int]:
    return verifiedRole

def getModRole() -> Optional[int]:
    return modRole

def getOwner() -> Optional[int]:
    return owner

def getConfidenceThreshold() -> int:
    return confidenceThreshold

def getBotCmdChannels() -> List[int]:
    return botCmdChannels

def getSbBotCmdChannels() -> List[int]:
    return sbBotCmdChannels

def getAllowedWords() -> List[str]:
    return allowedWords

def getBlacklist0() -> List[str]:
    return blacklist0

def getBlacklist1() -> List[str]:
    return blacklist1

def getHyRequestsMade() -> int:
    global hyRequestsMade
    return hyRequestsMade

def addHyRequestsMade() -> int:
    global hyRequestsMade
    hyRequestsMade += 1
    return hyRequestsMade

def setHyRequestsMade(n) -> None:
    global hyRequestsMade
    hyRequestsMade = n

def setStartTime(time:dt.datetime) -> None:
    global startTime
    startTime = time
