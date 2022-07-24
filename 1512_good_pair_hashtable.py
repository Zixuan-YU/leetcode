## Solution based on two loops
## 68% runtime, 56% memory
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if nums[i]==nums[j] and i<j:
                    count+=1
        return count
      
## Solution based on handshake gathering      
## https://leetcode.com/problems/number-of-good-pairs/discuss/1457646/java-story-based-0ms-single-pass-easy-to-understand-simple-hashmap
## 60% runtime, 50% memory
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        cnt = 0
        hashmap = {}
        for i in nums:
            if i in hashmap:
                cnt += hashmap[i]
                hashmap[i] += 1
            else:
                hashmap[i] = 1

        return cnt

  class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dic = Counter(nums)
        ans = 0
        for k in dic:
            if dic[k] > 1:
                ans += dic[k]*(dic[k]-1)//2
        return ans
