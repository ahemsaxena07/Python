dictn = {
    'empl1':{
        'first name': 'ahem',
        'last name': 'saxena',
        'age': 19,
        'grade': 'highly-skilled',
    },
    'empl2':{
        'first name': 'xyz',
        'last name': 'zyx',
        'age': 23,
        'grade': 'skilled',
    },
    'empl3':{
        'first name': 'abc',
        'last name': 'cba',
        'age': 33,
        'grade': 'highly-skilled',
    },
    'empl4':{
        'first name': 'fgh',
        'last name': 'hgf',
        'age': 30,
        'grade': 'semi-skilled',
    }
}
print(list(filter(lambda n: n == ['grades']['highly-skilled'], dictn.items())))