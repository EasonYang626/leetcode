from typing import List
# 思路：排序 + 双指针
#  使用四个指针(a<b<c<d)。固定最小的a和b在左边，c=b+1,d=_size-1 移动两个指针包夹求解。
#  保存使得nums[a]+nums[b]+nums[c]+nums[d]==target的解。偏大时d左移，偏小时c右移。c和d相
#  遇时，表示以当前的a和b为最小值的解已经全部求得。b++,进入下一轮循环b循环，当b循环结束后。
#  a++，进入下一轮a循环。 即(a在最外层循环，里面嵌套b循环，再嵌套双指针c,d包夹求解)。
class Solution:  
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # /*定义一个返回值*/
        result = []
        # /*当数组为null或元素小于4个时，直接返回*/
        if(not nums or len(nums) < 4):
            return result
        
        # /*对数组进行从小到大排序*/
        nums.sort()
        # /*数组长度*/
        length=len(nums)
        # /*定义4个指针k，i，j，h  k从0开始遍历，i从k+1开始遍历，留下j和h，j指向i+1，h指向数组最大值*/
        for k in range(length - 3):
            # /*当k的值与前面的值相等时忽略*/
            if(k > 0 and nums[k]==nums[k-1]):
                continue
            
            # /*获取当前最小值，如果最小值比目标值大，说明后面越来越大的值根本没戏*/
            min1=nums[k]+nums[k+1]+nums[k+2]+nums[k+3]
            if(min1>target):
                break
            # 直接break跳出for循环 后续的for循环也不可能有解了 返回值 因为k对应的值越来越大
            # 四数和越来越大
            # 相当于直接return 
            
            # /*获取当前最大值，如果最大值比目标值小，说明后面越来越小的值根本没戏，忽略*/
            max1=nums[k]+nums[length-1]+nums[length-2]+nums[length-3]
            if(max1<target):
                continue
            # 这里用的是 continue 跳出当前循环 k++
            # 因为后面 k对应的值还在增大 未必始终小于目标值
            
            # /*第二层循环i，初始值指向k+1*/
            for i in range(k + 1 , length - 2):
                # /*当i的值与前面的值相等时忽略*/
                if(i>k+1 and nums[i]==nums[i-1]):
                    continue
                
                # /*定义指针j指向i+1*/
                j=i+1
                # /*定义指针h指向数组末尾*/
                h=length-1
                # /*获取当前最小值，如果最小值比目标值大，说明后面越来越大的值根本没戏，忽略*/
                min=nums[k]+nums[i]+nums[j]+nums[j+1]
                if(min>target):
                    break
                
                # /*获取当前最大值，如果最大值比目标值小，说明后面越来越小的值根本没戏，忽略*/
                max=nums[k]+nums[i]+nums[h]+nums[h-1]
                if(max<target):
                    continue
                
                # /*开始j指针和h指针的表演，计算当前和，如果等于目标值，j++并去重，h--并去重，
                # 当当前和大于目标值时h--，当当前和小于目标值时j++*/
                while (j<h):
                    curr=nums[k]+nums[i]+nums[j]+nums[h]
                    if(curr==target):
                        result.append([nums[k],nums[i],nums[j],nums[h]])
                        j = j + 1
                        while(j<h and nums[j]==nums[j-1]):
                            j = j + 1
                        
                        h = h -1
                        while(j<h and i<h and nums[h]==nums[h+1]):
                            h = h - 1
                        
                    elif(curr>target):
                        h = h - 1
                    else:
                        j = j + 1
                                
        return result
        
