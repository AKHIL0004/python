nums = [12,-7,5,64,-14]
print("original numbers in the list1:",nums)
new_nums = list(filter(lambda x: x>0,nums))
print("output: ",new_nums)
nums = [12,14,-95,3]
print("original numbers in the list2:",nums)
new_nums = list(filter(lambda x: x>0,nums))
print("output: ",new_nums)