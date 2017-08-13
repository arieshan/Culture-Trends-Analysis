
import json

from itertools import islice
file0 = open("0.txt", "a")
file1 = open("1.txt", "a")
file2 = open("2.txt", "a")
file3 = open("3.txt", "a")
file4 = open("4.txt", "a")
file5 = open("5.txt", "a")
file6 = open("6.txt", "a")
file7 = open("7.txt", "a")
file8 = open("8.txt", "a")
file9 = open("9.txt", "a")

class ReviewProcess:

    def zero(self, review):
        file0.write(json.dumps(review) + '\n')
    
    def one(self, review):
        file1.write(json.dumps(review) + '\n')

    def two(self, review):
        file2.write(json.dumps(review) + '\n')

    def three(self, review):
        file3.write(json.dumps(review) + '\n')

    def four(self, review):
        file4.write(json.dumps(review) + '\n')   

    def five(self, review):
        file5.write(json.dumps(review) + '\n')  

    def six(self, review):
        file6.write(json.dumps(review) + '\n')  

    def seven(self, review):
        file7.write(json.dumps(review) + '\n') 

    def eight(self, review):
        file8.write(json.dumps(review) + '\n') 

    def nine(self, review):
        file9.write(json.dumps(review) + '\n')   
    
    def option(self, index, review):
        options = {0 : self.zero,
                1 : self.one,
                2 : self.two,
                3 : self.three,
                4 : self.four,
                5 : self.five,
                6 : self.six,
                7 : self.seven,
                8 : self.eight,
                9 : self.nine,
        }
        options[index](review)

    def loadData(self, cityCode, index):
        with open("yelp_academic_dataset_review.json") as myfile:
            first1000 = list(islice(myfile, 100000))
        for line in first1000:
            line = json.loads(line)
            if line['business_id'] in cityCode:             
                self.option(index, line['text'])

