class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #hashmap = {}
        lst = []
       #for i in range(len(nums)):
           # hashmap[nums[i]] = i
        for i in range(len(nums)):
            remain = -nums[i]
            for j in range(i+1, len(nums)):
                remain2 = remain - nums[j]
                for k in range(j+1, len(nums)):
                    temp = [nums[i],nums[j],nums[k]]
                    if remain2 == nums[k] and sorted(temp) not in lst:
                        lst.append(sorted(temp))
        return lst
                
                
        
