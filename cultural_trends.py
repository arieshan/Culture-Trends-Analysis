
from cityCode_process import CityProcess
from lda import LDAProcess
from rating import Rating
import numpy as np
import matplotlib.pyplot as plt


city = CityProcess()
rate = Rating()
cities = city.loadData()
lda = LDAProcess()
lda.loadData()
n_groups = 5
res1 = rate.rate("topic/topic0.txt")
res2 = rate.rate("topic/topic1.txt")
res3 = rate.rate("topic/topic2.txt")
res4 = rate.rate("topic/topic3.txt")
res5 = rate.rate("topic/topic4.txt")
res6 = rate.rate("topic/topic5.txt")
res7 = rate.rate("topic/topic6.txt")
res8 = rate.rate("topic/topic7.txt")
res9 = rate.rate("topic/topic8.txt")
res10 = rate.rate("topic/topic9.txt")

fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.15
opacity = 0.4

res11 = []
res11.append(res1[0])
res11.append(res2[0])
res11.append(res3[0])
res11.append(res4[0])
res11.append(res5[0])

res12 = []
res12.append(res1[1])
res12.append(res2[1])
res12.append(res3[1])
res12.append(res4[1])
res12.append(res5[1])

res13 = []
res13.append(res1[2])
res13.append(res2[2])
res13.append(res3[2])
res13.append(res4[2])
res13.append(res5[2])

res14 = []
res14.append(res1[3])
res14.append(res2[3])
res14.append(res3[3])
res14.append(res4[3])
res14.append(res5[3])

res15 = []
res15.append(res1[4])
res15.append(res2[4])
res15.append(res3[4])
res15.append(res4[4])
res15.append(res5[4])

rects1 = plt.bar(index, res11, bar_width, alpha=opacity, color='b',label= 'feature')
index = index + bar_width 
rects2 = plt.bar(index, res12, bar_width, alpha=opacity, color='r',label= 'service') 
index = index + bar_width 
rects3 = plt.bar(index, res13, bar_width, alpha=opacity, color='y',label= 'food')
index = index + bar_width  
rects4 = plt.bar(index, res14, bar_width, alpha=opacity, color='purple',label= 'surrounding') 
index = index + bar_width 
rects5 = plt.bar(index, res15, bar_width, alpha=opacity, color='black',label= 'price') 

"""
index = index + bar_width 
rects5 = plt.bar(index, res6, bar_width, alpha=opacity, color='black',label= cities[5]) 
index = index + bar_width 
rects5 = plt.bar(index, res7, bar_width, alpha=opacity, color='black',label= cities[6]) 
index = index + bar_width 
rects5 = plt.bar(index, res8, bar_width, alpha=opacity, color='black',label= cities[7]) 
index = index + bar_width 
rects5 = plt.bar(index, res9, bar_width, alpha=opacity, color='black',label= cities[8]) 
index = index + bar_width 
rects5 = plt.bar(index, res10, bar_width, alpha=opacity, color='black',label= cities[9]) 
"""

plt.xlabel('City')  
plt.ylabel('frequency')  
plt.title('frequency by group')  
plt.xticks(index - 2 * bar_width, (cities))  
plt.ylim(0,60)  
plt.legend()  
   
plt.tight_layout()  
plt.show()  
