class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        k =[]

        for i in nums:
            if i in d.keys():
                d[i]=d[i]+1
            else:
                d[i]=1
        for i in range(0, len(nums)):
            j = target - nums[i]
            if j in d.keys():
                if j==nums[i]:
                    if d.get(j)>1:
                        k.append(i)
                        k.append(j)
                        break
                else:
                    k.append(i)
                    k.append(j)
                    break
        for i in range(0, len(nums)):
            if k[1]==nums[i] and k[0]!=i:
                k[1]=i
                k.sort()
                break
        return k


        
