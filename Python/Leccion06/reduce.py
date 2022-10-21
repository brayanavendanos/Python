import functools 

numbers = [1, 2, 3, 4]

def acumulador(cont, obj):
    print('counter', cont)
    print('item', obj)
    return cont + obj

result = functools.reduce(lambda counter, item: counter + item, numbers)

result_function = functools.reduce(acumulador,numbers)

print(result)