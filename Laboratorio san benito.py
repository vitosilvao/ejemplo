
import statistics
import funciones_laboratorio_san_benito as fl

pacientes=[]
listado_glucosa=[]
cont_normal=0
cont_paciente=0
cont_alterado=0
cont_riesgozo=0

while(True):
    print("Laboratorio San Benito")
    print("Menu")
    print("1.- Registrar muestra de los pacientes")
    print("2.- Listar los pacientes atendidos")
    print("3.- Resumen estadistico de las muestras")

    opc=int(input("Ingrese una opcion: "))
    
   


    if (opc==1):
        rut=""
        edad=0
        nivel_glucosa=0
        tipo_sangre=""

        fl.agregar(rut, edad, nivel_glucosa, tipo_sangre)
  


        # ``rut=int(input("ingrese el rut del cliente: "))
        # edad=int(input("ingrese la edad: "))
        # nivel_glucosa=int(input("ingrese el nivel de glucosa: "))
        # listado_glucosa.append(nivel_glucosa)
        
        # if (nivel_glucosa<100):
        #     estado_glucosa=("Nivel normal de glucosa")
        #     cont_normal=cont_normal+1
        # if (nivel_glucosa>=100 and nivel_glucosa<=125):
        #     estado_glucosa=("Nivel de glucosa alterado")
        #     cont_alterado=cont_alterado+1
        # if (nivel_glucosa>=126):
        #     estado_glucosa=("Nivel de glucosa riesgoso, se necesitan realizar mas pruebas")
        #     cont_riesgozo=cont_riesgozo+1
        
        # tipo_sangre=input("ingrese el tipo de sangre (A, B, AB, O): ").upper()
        

        # paciente={
        # "Rut:\n": rut , 
        # "Edad": edad,
        # "Nivel de glucosa": nivel_glucosa, 
        # "Estado de glucosa": estado_glucosa,
        # "tipo de sangre": tipo_sangre
        # }
        
        # pacientes.append(paciente)
        cont_paciente=cont_paciente+1
        nivel_glucosa_max=max(listado_glucosa)
        prom_glucosa=statistics.mean(listado_glucosa)
            
            
            

    if (opc==2):

        

        print(pacientes)
    
    if (opc==3):
        print("RESUMEN")
        print(f"Cantidad de muestras: {cont_paciente} ")
        print(f"Cantidad muestras riesgozas: {cont_riesgozo}")
        print(f"Nivel mayor registrado: {nivel_glucosa_max}")
        print(f"El promedio de nivel glucosa es: {prom_glucosa}")

        pass