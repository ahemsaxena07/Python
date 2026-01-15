#obtain a list of tuples, where each tuple contains a number from one list and a string from another
nums = [10, 20, 30, 40, 50, 60, 70, 80]
strs = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
lst = map(lambda n, y: f"{n}" + y, nums, strs)
print(list(lst))

#concise way
h = map(lambda n, y: f"{n}{y}", nums, strs)  #we can also use str(n) + y
print(list(h))