#obtain a list of students who obtained more than 40 marks in the exam.
dictn = {
    'ahem': 95,
    'xys': 23,
    'abc': 89,
    'hbf': 38,
    'hd4': 70
}
lst = filter(lambda n: dictn[n] > 40, dictn.keys())
print(list(lst))

# if we want both names and marks
lst2 = filter(lambda item: item[1] > 40, dictn.items())
print(list(lst2))