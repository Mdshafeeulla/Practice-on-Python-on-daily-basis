class Solution(object):
    def armstrong(self,num):
        power = len(num)
        int_num = int(num)
        nums = 0
        for i in num:
            nums += int(i) ** power
        if nums == int_num:
            print("The given number is an armstrong")
        else:
            print("The given number is not an armstrong")
arm_Solution = Solution()
arm_Solution.armstrong("153")
