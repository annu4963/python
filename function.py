# def user_info():
#     name=input("Enter your name")
#     address=input("Enter your address")
#     phone=input("Enter your phone no")
#     email=input("Enter your email address")
#     return f"The name is {name}\nThe address is {address}\nThe phone no is {phone}\nThe email is {email}"
#
# print(user_info())

# def fact(n):
#     if n==1:
#         return 1
#     else:
#         return n*fact(n-1)
#
# print(fact(5))

# nested function
# def students():
#     def name(new_name):
#         return "Ram"
#     return name
#
# result = students()
# print(result('Ram'))

# def add(x,y):
#     return x+y
#
# print(add(10,20))

# lambda is single line expression for function define
# add=lambda x,y:x+y
# print(add(10,20))

# use of decorator
# def zero_check(any_function):
#     def inner(x,y):
#         if y==0:
#             return"Y can't be zero"
#         else:
#             return(any_function(x,y))
#     return inner
# def hundred_check(any_function):
#     def inner(x,y):
#         if y>=100:
#             return"Y can't be 100 or greater than 100"
#         else:
#             return(any_function(x,y))
#     return inner
#
# @hundred_check
# @zero_check
# def add(x,y):
#     return x+y
#
# print(add(100,0))

