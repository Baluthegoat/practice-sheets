#def find_missing_number(nums):
    #n = len(nums)
    #total_sum = n*(n+1) // 2
   # array_sum = sum(nums)
  #  missing_num = total_sum - array_sum
 #   return missing_num

#input_nums = [3,0,1]
#missing_number = missing_number(input_nums)
#print(missing_num)

def find_missing_number(nums):
    n = len(nums)
    total_sum = n*(n+1) / 2
    array_sum = sum(nums)
    missing_num = total_sum - array_sum
    

input_nums = [3, 0, 1]
missing_number = find_missing_number(input_nums)
print(missing_num)

 