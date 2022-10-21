def increment(x):
    return x + 1

increment_v2 = lambda x : x + 1 


def high_ord_func(x, func):
    return x + func(x)

high_ord_func_v2 = lambda x, func: x + func(x)

result = high_ord_func(2,increment)
# 2 + ( 2 + 1)
print(result)

result = high_ord_func_v2(4, increment_v2)
print(result)
result2 = high_ord_func_v2(6, lambda x : x **2) # Se pueden añadir los lambda directamente cómo función
print(result2)
result2 = high_ord_func_v2(8, lambda x : x * 2)
print(result2)
