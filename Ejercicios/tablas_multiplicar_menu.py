def run():
    menu = """
    [[Tablas de multiplicar 🔢]]
<<Que tabla de multiplicar desea consultar: >>
    
    Tabla del número: """
    i = int(input(menu))
    print(f'Esta es la tabla del {i}')
    for j in range(10):
        print(f'{i} x {j} = {i*j}')    
    pass


if __name__ == "__main__":
    run()