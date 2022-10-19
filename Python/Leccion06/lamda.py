def increment(x):
    return x + 1

increment_l = lambda x : x ** 2

result_l = increment_l(2)
print(result_l)

result2 = increment(25)
print(result2)
result = increment(5)
print(result)
print(increment(20))

                #recibe 2 parametros=> retorna
full_name = lambda name, last_name, edad, : f'Full name: {name.title()} {last_name.title()} tiene {edad} años'

fullname = full_name('El Bryan', 'Avendaño', 26)
print(fullname)

