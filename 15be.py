lst = ['malayalam', 'drawing', 'mandamalamadnam', '1234321']
so = filter(lambda n: n == n[::-1], lst)
print(list(so))