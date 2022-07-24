 
##### Solution1
### 70 percentile runtime
### 35 percentile memory
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}
        max_index = 0
        n = len(nums)
        if n == 1:
            return nums[0]
        
        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
                if hashmap[i] > n/2:
                    print(hashmap)
                    return i
            else:
                hashmap[i] = 1
 
##### Solution2
##### Boyer-Moore Voting Algorithm
##### Youtube link:https://www.youtube.com/watch?v=n5QY3x_GNDg

### 78 percentile runtime
### 89 percentile memory

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None
        
        for i in nums:
            if count == 0:
                candidate = i
            count += (1 if i == candidate else -1)
                
        return candidate
