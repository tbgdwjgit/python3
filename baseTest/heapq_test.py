__author__ = 'Test-YLL'

import heapq

nums = [1,8,2,23,7,-4,18,23,42,37,2]
print(heapq.nlargest(1,nums))
print(heapq.nlargest(11,nums))#大到小
print(heapq.nsmallest(1,nums))
print(heapq.nsmallest(11,nums))#小到大
