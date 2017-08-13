import json

from itertools import islice
from operator import itemgetter
from collections import defaultdict
from review_process import ReviewProcess

class CityProcess:
    #def _init_(self):
        #self.review = reviews
        #self.cityCode = cityCode
    def loadData(self):
        cityMap = {}
        city = {}
        cityCode = defaultdict(list)
        review = ReviewProcess()
        with open("yelp_academic_dataset_review.json") as myfile:
            first1000 = list(islice(myfile, 100000))
        
        for line in first1000:
            line = json.loads(line)
            #if line['business_id'] not in cityMap:
            cityMap[line['business_id']] = cityMap.get(line['business_id'], 0) + 1
        
        with open("yelp_academic_dataset_business.json") as myfile:
            first1000 = list(islice(myfile, 100000))

        for line in first1000:
            line = json.loads(line)
            if line['business_id'] in cityMap:
                city[line['city']] = city.get(line['city'], 0) + cityMap.get(line['business_id'])
                if cityCode.get(line['city']) != None:
                    cityCode.get(line['city']).append(line['business_id'])
                else:
                    cityCode[line['city']] = [line['business_id']]
                    cityCode.get(line['city']).append(line['business_id'])

        sortByValue = sorted(city.items(), key = itemgetter(1), reverse = True)

        res = dict(sortByValue[0:10])
        index = 0
        ret = []
        for key in res.keys():          
            review.loadData(cityCode.get(key), index)
            ret.append(key)
            index = index + 1
        return ret

