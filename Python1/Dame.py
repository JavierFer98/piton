
def dame(texto):
    for caracter in texto:
        print("Dame una" +caracter)
        print("'"+ caracter + "'")
        
def medio(texto):
    print("El caracter que esta en medio es: ",
           texto[len(texto)//2])
        
def aMayuscula(texto):
    mayus=""
    for caracter in texto:
        if 'a' <= caracter <='z':
            location = ord(caracter) - ord('a')
            newascii = location + ord('A')
            caracter = chr(newascii)
            mayusc = mayus + caracter
    return mayusc

__version__ = '1.0'

dame("Piratas del Caribe")
medio("Piratas del Caribe")
print(aMayuscula("Piratas del Caribe"))
            
    