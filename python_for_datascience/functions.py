###############################################
# FONKSİYONLAR (FUNCTIONS)
###############################################

#######################
# Fonksiyon Tanımlama
#######################
def calculate(x):
    print(x * 2)


calculate(5)

# İki argümanlı/parametreli bir fonksiyon tanımlama


def summer(arg1, arg2):
    """
    Sum of two numbers
    :param arg1: int, float
    :param arg2: int, float
    :return: int, float
    """
    print(arg1 + arg2)


summer(7, 8)
summer(arg2=8, arg1=7)

#######################
# Fonksiyonların Statement/Body Bölümü
#######################

# def function_name(parameters/arguments):
#     statements (function body)


def multiplication(a, b):
    c = a * b
    print(c)


multiplication(10, 9)

# girilen değerleri bir liste içinde saklayacak fonksiyon

list_store = []


def add_element(a, b):
    c = a * b
    list_store.append(c)
    print(list_store)


add_element(1, 8)
add_element(18, 8)
add_element(180, 10)


#######################
# Ön Tanımlı Argümanlar/Parametreler (Default Parameters/Arguments)
#######################

def divide(a, b=1):
    print(a / b)


divide(10)


def say_hi(string="Merhaba"):
    print(string)
    print("Hi")
    print("Hello")


say_hi()
say_hi("mrb")


#######################
# Return: Fonksiyon Çıktılarını Girdi Olarak Kullanmak
######################

def calculate(varm, moisture, charge):
    return (varm + moisture) / charge


calculate(98, 12, 78) * 10

a = calculate(98, 12, 78)


def calculate(varm, moisture, charge):
    varm = varm * 2
    moisture = moisture * 2
    charge = charge * 2
    output = (varm + moisture) / charge
    return varm, moisture, charge, output


type(calculate(98, 12, 78))

varma, moisturea, chargea, outputa = calculate(98, 12, 78)


#######################
# Fonksiyon İçerisinden Fonksiyon Çağırmak
######################

def calculate(varm, moisture, charge):
    return int((varm + moisture) / charge)


calculate(90, 12, 12) * 10


def standardization(a, p):
    return a * 10 / 100 * p * p


standardization(45, 1)


def all_calculation(varm, moisture, charge, p):
    a = calculate(varm, moisture, charge)
    b = standardization(a, p)
    print(b * 10)


all_calculation(1, 7, 5, 12)
