def run():

    numbers = []
    for element in range(1,11):
        numbers.append(element * 2)
        
    print(numbers)

    numbers_v2 = [element * 2 for element in range(1,11)]
    print(numbers_v2)
    
    
    numbers2 = []
    for i in range(1,11):
        if i % 2 == 0:
            numbers2.append(i * 2)
            
    print(numbers2)
    
    numbersv2 = [i * 2 for i in range(1,11) if i % 2 == 0]
    print(numbersv2)

    
if __name__ == '__main__':
    run()





