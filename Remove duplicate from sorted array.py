class new_Solution(object):
    def removeDuplicates(self,nums):
        num = list(set(nums))
        print(len(num))
        new_list = num
        for i in range(len(num),len(nums)):
            new_list.append('_')

        print(new_list)
new_solution_dup = new_Solution()
new_solution_dup.removeDuplicates([0,0,1,1,1,2,2,3,3,4])