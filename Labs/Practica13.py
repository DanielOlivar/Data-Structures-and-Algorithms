from io import open 
archivo=open("acciones.txt","w")
archivo.write("\nCLAVE, NOMBRE, PRECIO\n======================\n")
archivo.write("SUNW,Sun Micro Systems,135.00\nC&A,Computer And Associates,34.00")
archivo.write("DUKE,Duke Corporation,12.375\nABStk,Absolute Tracking,20.875")
archivo.write("JSVCo,Java Services Co.,24.00\nMAs,Multiple Associations,80.125")
archivo.write("BWInc,British Workshops Inc.,6.25\nGMEnt,General Marketing Enterprises,52.50")
archivo.write("PMLtd,Protection Methodologies Ltd.,201.875\nJavaDevs,Java Developers Corp.,13.50")
archivo.close()
archivo = open("acciones.txt", "r")
for archivo in archivo.readlines():
    print (archivo)
archivo.close() 