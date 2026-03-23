"""
suppose there are two lists- one contains questions and another contains lists of 4
 possible answers for each question. Write a program to generate a list that contains 
 lists of question and its 4 possible answers.
"""
lst1 = ['what is your friends name? ', "your favourite colors? ", 'your favourite places? ']
lst2 = [['ahem', 'x', 'y', 'z'], ['red', 'yellow', 'green', 'blue'], ['delhi', 'san fransisco', 'new york', 'bangalore']]
lst = [[k, v] for k,v in zip(lst1, lst2)]
for k, v in lst: #for clean interface
    print(k, v, sep = ":")
print(lst) #for list