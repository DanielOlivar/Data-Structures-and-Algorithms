def formaArreglo(tamano): #Crea arreglo del tamaño que se le indico en parentesis
    Arr=[None]*tamano #none es valor numero, nulo guarda cualquier valor mas adelante y cero es literalmente el cero, es la tabla hash
    return Arr #regresa arr a map

def obtenerLlaveNumerica(llave):
    hash=0
    for char in str(llave):
        hash+=ord(char)
    return hash

def H(llaveN):
    return llaveN%5

def agregar(llave,valor,map,tamano): 
    llave_hash=H(obtenerLlaveNumerica(llave)) #
    ParllaveValor=[llave,valor]
    if map[llave_hash] is None: #Si esta vacio aqui agregar� algun elemento
        map[llave_hash]=list([ParllaveValor])
        return True
    else: #Entra en acci�n cuando hay una colision
        for par in map[llave_hash]:
            if par[0]==llave:
                par[1]=valor
                return True
        for j in range(tamano):
            llaveh=(llave_hash+j)%13
            if (llaveh==len(map)):
                print("Tabla llena",llave_hash)
                break
            else:
                if map[llaveh] is None:
                    map[llaveh]=list([ParllaveValor])
                    return True

def buscar(llave,tamano):
    llave_hash=H(obtenerLlaveNumerica(llave))
    if map[llave_hash] is not None:
        for par in map[llave_hash]:
            if par[0]==llave:
                return par[1]
            else:
                for j in range(tamano):
                    llaveh=(llave_hash+j)%13
                    if (llaveh==len(map)):
                        break
                    for par1 in map[llaveh]:
                        if par1[0]==llave:
                            return par1[1]
    return None

map=formaArreglo(10); #Empieza programa, llama a la funcion

agregar("Hola9","12213299",map,10)
agregar("Hola4",12213214,map,10)
agregar("Hola1",1221321,map,10)
agregar("Hola2",1221322,map,10)
agregar("Hola3",1221323,map,10)
agregar("Hola5",1221325,map,10)
agregar("Hola6",1221326,map,10)
agregar("Hola7",1221327,map,10)
agregar("Hola8",1221328,map,10)
agregar("Hola10",1221310,map,10)

print(map)

print("\nLLAVE DE  1: ",buscar("Hola9",10))