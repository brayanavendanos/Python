import utils

data = [
        {
            'Country': 'Colombia',
            'Population': 500,
            'area' : '25km'
        },
        {
            'Country': 'Bolivia',
            'Population': 300
        }
    ]

def run(): 
    keys, values = utils.get_population()

    print(keys,values)

    country = input('Type Country : ').capitalize()

    result = utils.population_by_country(data,country)
    print(result)

if __name__ == '__main__':
    run()