def Max_ (List_1):

  for n in range (len (List_1)-1, 0, -1):
    for i in range (n):
      if List_1[i]>List_1[i+1]:
        Temp_=List_1[i]
        List_1[i]= List_1[i+1]
        List_1[i+1]= Temp_
  Index_= len(List_1)-1
  Higher_1= List_1[Index_]
  return Higher_1

List_= []
print ("Buenas tardes caballero, por favor introduzca 2 números para probar la funcion solicitada")
Number_= int (input ("Primer número por favor: \n"))
List_.insert(0, Number_)
Number_1= int (input ("Segundo número por favor: \n"))
List_.insert(1, Number_1)
Higher_= Max_ (List_)
print ("Caballero, el número mayor es: ", Higher_)