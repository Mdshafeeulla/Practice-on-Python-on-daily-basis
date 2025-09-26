class Solution(object):
    def leap_year(self,year):
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            # IF are not taking year % 400 then the logic will be wrong and gonna be showing 1900 as leap year which
            #  is not,So and it is not multiple of 4 also
            print(f"The given year {year} is a leap year")
        else:
            print(f"The given year is not leap  year")

New_Solution = Solution()
New_Solution.leap_year(1900)
