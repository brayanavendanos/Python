# Tablas de multiplicar

def run():
    for i in range(11):
        print(f'Esta es la tabla del {i}')
        for j in range(10):
            print(f'{i} x {j} = {i*j}')


if __name__ == '__main__':
    run()