import os

# ------------- V A R I A B L E S    &    T Y P E S --------------------
varChar = 'c' # int = 3, byte = 3 en binario
varString = "hola"  # String character
varNumber = 12 # number

# SUBTYPES OF number
varInteger = 10 # 2147483647 MAX_VALUE -2147483647 MIN_VALUE  int32 bit 2^32
varLong = 10 # INT64 MAX VALUE 9,223,372,036,854,775,807 2^64 
# bit = 1 | 0 
varDouble = 2.098877969569568
varFloat = 2.1
varByte = 10001000 # 8 bits
bit = 1 | 0 

varBoolean = False

# print(varString)
# Base10: 1234567890 10
# base16: 0123456789ABCDFG
# BASE2 o BINARIO: 01

# Algebraic operators
# +     = sum
# -     = substraction
# *     = multiplication
# /     = regular division
# //    = integer division

TAX = 0.18

# def tax(precio):
#     return precio * TAX 

# print("EL PRECIO ES: " + str(2))

# print("2" + str(4)) #Concat strings
# print(2 + 4)

# varString = "2"

# print(int(varString) + 4)

# ---------------------- F U N C T I O N S ---------------------------------
#  def keyword as it name says, defines the start of a function
# CONTANT_LALALA = 9
# hola_luis() snake case
# holaLuis()  camel case

# def holaLuis():
#     x = "hola"
#     return x

# print(holaLuis())

# Variables locales
# def sumOfTwoNumbers(num1, num2):
#     local = 10
#     print(local)
#     return num1 + num2

# print(sumOfTwoNumbers(1 , 1))
# print(local) # No existe este valor en el context global

# Variables globales
# globalVar = 10

# def multiplybyTen(num1):
#     return num1 * globalVar

# def divideByTen(num1): # integer division
#     return num1 // 5


# print(multiplybyTen(10)) # 100
# print(divideByTen(100)) # 10

# def createDictionary():
#     mapa = {
#         'LUIS' : 'Hola me llamo luis', 
#         'SILVANA' : 'Hola me llamo silvana'
#         }
#     return mapa

# dictionary = createDictionary()

# def printPATHVar():
#     value = os.environ.get('ARAM')
#     print(value)

# printPATHVar()

# Hello

# aGREGE OTRA COSA