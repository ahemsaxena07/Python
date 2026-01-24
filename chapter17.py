# #namespaces

# # def fun():
# #     a = 45
# #     global b
# #     b = 6.28
# #     print(a,b,s)
# # a = 20
# # b = 3.14
# # s = 'Aabra ka daabra'
# # fun()
# # print(a,b,s)

# # lst = ['a', 'b', 's']
# # for var in lst:
# #     print(globals()[var])

# def fun1():
#     y = 20
#     print(x,y)
#     print(len(str(x)))
#     def fun2():
#         z = 30
#         print(x,y,z)
#         print(len(str(x)))

#     fun2()
# x = 10
# print(len(str(x)))
# fun1()

def fun1():
    a = 20
    print(a)
    print(id(a))

    def fun2():
        a = 40
        print(a)
        print(id(a))
    fun2()
fun1()