ruta = "datosok.txt"
with open(ruta, mode = "a", encoding = "utf-8") as fichero:
       
    for i in range(10):
    
      
        print("Escriba su cedula: ")
        Cedula = input()
        print("Escriba su nombre: ")
        Nombre = input()
        print("Escriba sus apellidos: ")
        Apellidos = input()
        print("Escriba su Edad")
        Edad = input()
        print("Desea guardar sus datos? Y/N")
        Guardar = input()
        
        if Guardar == "Y":

            fichero.write("Cedula   ")
            fichero.write("Nombres   ")
            fichero.write("Apellidos   ")
            fichero.write("Edad   ")
            fichero.write("\n")
            fichero.write(Cedula)
            fichero.write("   ,")
            fichero.write(Nombre)
            fichero.write("   ,")
            fichero.write(Apellidos)
            fichero.write("   ,")
            fichero.write(Edad)
            fichero.write("\n")
            fichero.write("\n")
            
            print("Los datos se han guardado correctamente,\nDesea guardar mas datos?")
            print("Y/N?")
            Otra = input()
            
            if Otra == "Y":    
                i = 0
            else:
                break
            
        else:
            print("Salio Correctamente.")
            break
            
    
    