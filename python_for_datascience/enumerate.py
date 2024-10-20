#######################
# Enumerate: Otomatik Counter/Indexer ile for loop
#######################

students = ["John", "Mark", "Venessa", "Mariam"]

for student in students:
    print(student)

for index, student in enumerate(students):
    print(index, student)

A = []
B = []

for index, student in enumerate(students):
    if index % 2 == 0:
        A.append(student)
    else:
        B.append(student)

#######################
# Uygulama
#######################
# divide_students fonksiyonu yazılsın.
# Çift indexte yer alan öğrenciler bir listeye,
# Tek indexte yer alan öğrenciler başka bir listeye alınsın.
# Fakat bu iki liste tek bir liste olarak return olsun.

students = ["John", "Mark", "Venessa", "Mariam"]


def divide_student(students):
    groups = [[], []]
    for index, student in enumerate(students):
        if index % 2 == 0:
            groups[0].append(student)
        else:
            groups[1].append(student)
        print(groups)
    return groups


st = divide_student(students)

#######################
# alternating fonksiyonunun enumerate ile yazılması
#######################


def alternating_with_enumerate(string):
    new_string = ""
    for i, letter in enumerate(string):
        if i % 2 == 0:
            new_string += letter.upper()
        else:
            new_string += letter.lower()
    print(new_string)


alternating_with_enumerate("hi my name is john and i am learning python")

#######################
# Zip
#######################

students = ["John", "Mark", "Venessa", "Mariam"]

departments = ["mathematics", "statistics", "physics", "astronomy"]

ages = [23, 30, 26, 22]

list(zip(students, departments, ages))

###############################################
# lambda, map, filter, reduce
###############################################


def summer(a, b):
    return a + b


summer(1, 3) * 9


new_sum = lambda a, b: a + b


new_sum(4, 5)

# map
salaries = [1000, 2000, 3000, 4000, 5000]


def new_salary(x):
    return x * 20 / 100 + x


new_salary(5000)

for salary in salaries:
    print(new_salary(salary))

list(map(new_salary, salaries))


# del new_sum
list(map(lambda x: x * 20 / 100 + x, salaries))
list(map(lambda x: x ** 2, salaries))

# FILTER
list_store = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list(filter(lambda x: x % 2 == 0, list_store))

# REDUCE
from functools import reduce
list_store = [1, 2, 3, 4]
reduce(lambda a, b: a + b, list_store)