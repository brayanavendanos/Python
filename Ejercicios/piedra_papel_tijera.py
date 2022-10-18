import random 
options = ('piedra', 'papel', 'tijera')


print("""
      [ 🤖 Bienvenido al juego Piedra, Papel o tijera 🤖]
                  >>> Ingresa una opción <<<
      """)
user_option = input('>>> piedra, papel o tijera => ').lower()

if not user_option in options:
    print('Esa opción no es valida')
    
computer_option = random.choice(options)

print('User option => ', user_option)
print('Computer option => ', computer_option)

if user_option == computer_option:
    print('Empate!')
elif user_option == 'piedra':
    if computer_option == 'tijera':
        print('Piedra gana a tijera')
        print('¡User gana!')
        