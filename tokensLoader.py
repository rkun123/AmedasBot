import os
import json
#Tokens define
class Loader:
    def __init__(self):
        tokensFile = open(os.path.dirname(os.path.abspath(__file__)) + "/tokens.json")
        self.rawTokens = json.load(tokensFile)
    
    def load(self):
        res = {}
        res["TOKEN"] = self.rawTokens["token"]
        res["TOKEN_SECRET"] = self.rawTokens["token_secret"]
        res["CONSUMER"] = self.rawTokens["consumer"]
        res["CONSUMER_SECRET"] = self.rawTokens["consumer_secret"]
        return res

