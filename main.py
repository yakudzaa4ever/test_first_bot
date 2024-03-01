# class User:
#     def __init__(self, id, name, lastname, age, email):
#         self.id = id
#         self.name = name
#         self.lastname = lastname
#         self.age = age
#         self.email = email
#
#
# users = (1, 'Toxir', 'Toxirov', 28, 'toxir@gmail.com')
#
# user = User(*users)
# print(user)

# ---------------------------------------------
#
# from collections import namedtuple
#
# User = namedtuple('User', 'id name lastname age email')
#
# users = [
#     (1, 'Toxir', 'Toxirov', 28, 'toxir@gmail.com'),
#     (2, 'Sobir', 'Toxirov', 28, 'toxir@gmail.com'),
#     (3, 'Toxir', 'Toxirov', 28, 'toxir@gmail.com'),
# ]
#
# for user in users:
#     us = User(*user)
#     print(*us)

from collections import namedtuple

Cars = namedtuple('car', 'name color speed cost sigim boshqaruv')

car = ('Malibu', 'Red', '300 km/h', 2000, 4, 'Avtomat')

for  cars in car:
    ca = Cars(*car)
    print(*ca)