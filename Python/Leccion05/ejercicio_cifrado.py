cifrada = "Aqxzxobjmp nmo bi kmoqb x ixp 5 ab ix qxoab"
corr = 3


alfabeto = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

#cada letra dentro del mensaje original se reemplaza por la letra que este "corr" veces en el alfabeto. 
#minúsculas
#sin tildes

def descifrada():
    mensaje = ""

    for i in cifrada: 
        if i in alfabeto:
            pos_letra = alfabeto.index(i)
            nueva_pos = (pos_letra+corr)% len(alfabeto)
            mensaje += alfabeto[nueva_pos]
        else: 
            mensaje += i
    return mensaje
        
descifrada = descifrada()
print(descifrada)

