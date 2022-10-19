def run():
    
    dict = {}
    for i in range(1,5):
        dict[i] = i * 2

    print(dict)

    dict2 = {i: i * 2 for i in range(1,5)}
    print(dict2)
    
    
    countries = ['col', 'mex', 'bol', 'pe']
    population = {}
    
    import random
    
    for country in countries:
        population[country] = random.randint(10,10000)
    
    print(population)
    
    
    countries2 = ['usa', 'arg', 'bra', 'vnz']
    population2 = {country2: random.randint(10,10000) for country2 in countries2}
    
    print(population2)
    
    names = ['Bryan', 'Juan', 'Cesar', 'Santiago']
    ages = ['26', '24', '30', '21']
    print(list(zip(names,ages)))
    
    new_dict = {name: age for (name,age) in zip(names,ages)} 
    print(new_dict)

    # Condicionales 
    
    countries3 = ['usa', 'arg', 'bra', 'vnz']
    population3 = {country2: random.randint(10,100) for country2 in countries2}
    print(population3)
    
            # Elemento nuevo/ ciclo de los elementos nuevos de los items del dicc anterior solo si la popul del nuevo diccionario es mayor a 50
    result = {country4:population4 for (country4,population4) in population3.items() if population4 > 50}
    print(result)
    
    text = 'Hola, soy Bryan Avendaño'
    unique = { c: c.upper() for c in text if c in 'aeiou'}
    print(unique)
    
    
if __name__ == '__main__':
    run()
