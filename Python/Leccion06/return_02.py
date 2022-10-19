def find_volume(length = 1, width = 1 , depth = 1):
    return length * width * depth, width, 'prueba'

result1 = find_volume(10,20,3)
result_2 = find_volume(width=10)
result, width, text = find_volume(width = 10)

print(result1)
print(result1[1])
print(result_2)

print(result)
print(width)
print(text)


