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

## PRUEBAS

#--------------
# INSTANCIA 1
#--------------

# Base variables
cifrada = "Eg ikhwnz yzg zñlív zñ Pvwgk"
corr = 5

try:
    # Caso 1: no existe la variable.
    try:
        descifrada
    except:
        raise NotImplementedError("No declaraste una variable llamada descifrada.",)
    
    # Caso 2: el código se ejecuta con errores
    try:
        exec(_i)
    except:
        raise RuntimeError("Tu código produce un error al ejecutarse.")
    
    # Caso 3: el código modifica los parametros del problema
    try:
        assert cifrada == "Eg ikhwnz yzg zñlív zñ Pvwgk"
        assert corr == 5
    except:
        raise AssertionError("Tu código no debe modificar los datos del problema.")
    
    # Caso 4: no es de tipo str.
    assert type(descifrada) == str, f"Tu variable descifrada no es de tipo {str._name_}."

    # Caso 5: el código no utiliza las variables cifrada y corr
    assert _i.find("cifrada") >= 0, "Tu código no utiliza la variable cifrada."
    assert _i.find("corr") >= 0, "Tu código no utiliza la variable corr."

    # Caso 6: la respuesta es correcta
    assert descifrada == 'El nombre del espía es Pablo', "Tu respuesta es incorrecta."
    
except:
    # Restaurar variables base originales
    cifrada = "Aqxzxobjmp nmo bi kmoqb x ixp 5 ab ix qxoab"
    corr = 3
    raise
    
finally:
    # Restaurar variables base originales
    cifrada = "Aqxzxobjmp nmo bi kmoqb x ixp 5 ab ix qxoab"
    corr = 3

# Mensaje de felicitaciones
print("Felicidades, realizaste este ejercicio correctamente.")
