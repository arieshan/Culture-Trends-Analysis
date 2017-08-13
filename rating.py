
from operator import itemgetter
import numpy as np

class Rating: 
    
    def rate(self, path):
        feature = self.loadData("feature.txt")
        service = self.loadData("service.txt")
        quality = self.loadData("Foods.txt")
        surrouding = self.loadData("surrounding.txt")
        price = self.loadData("price.txt")
        res = {}
        #print(path)
        with open(path, 'r') as f:
            topic = f.readlines()

        for line in topic:
            words = line.strip().split(" ")
            dic = {}
            for word in words:
                if word == "":
                    continue
                word = word.lower()
                #print(word)
                if word in feature:
                    dic["f"] = dic.get("f", 0) + 1
                    #print(1)
                if word in service:
                    dic["s"] = dic.get("s", 0) + 1
                    #print(2)
                if word in quality:
                    dic["q"] = dic.get("q", 0) + 1
                    #print(3)
                if word in surrouding:
                    dic["surr"] = dic.get("surr", 0) + 1
                    #print(4)
                if word in price:
                    dic["p"] = dic.get("p", 0) + 1
                    #print(5)
            sortByValue = sorted(dic.items(), key = itemgetter(1), reverse = True)
            temp = dict(sortByValue[0:1])
            for key in temp.keys():
                res[key] = res.get(key, 0) + 1
            
        ret = np.zeros(5, dtype = int)
        for key in res.keys():
            if key == "f":
                ret[0] = ret[0] + res.get(key)
                #print(1)
            if key == "s":
                ret[1] = ret[1] + res.get(key)
                #print(2)
            if key == "q": 
                ret[2] = ret[2] + res.get(key)
                #print(3)
            if key == "surr":
                ret[3] = ret[3] + res.get(key)
                #print(4)
            if key == "p":
                ret[4] = ret[4] + res.get(key)
        return ret

    def loadData(self, path):
        with open(path, 'r') as f:
            docs = f.readlines()
        mset = set()
        for line in docs:
            words = line.strip().split('\t')
            for word in words:
                mset.add(word.lower())
        return mset
