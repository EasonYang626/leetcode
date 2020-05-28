from typing import List

class Solution:   
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrace(num, res):            
            if res == []:
                res.append([num])
                return
            temp_res = [] 
            while res != []:
                sub_res = res.pop()
                length = len(sub_res)                             
                for i in range(length + 1):
                    temp = sub_res.copy()
                    temp.insert(i, num)                   
                    temp_res.append(temp)
            for i in temp_res:
                # 去重
                if i not in res:
                    res.append(i)
            # res = copy.deepcopy(temp_res)
           
        for i in nums:
            backtrace(i, res)
        # 去重
        # new_res = []
        # for i in res:
        #     if i not in new_res:
        #         new_res.append(i)
        return res
            