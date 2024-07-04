pacientes=[]
listado_glucosa=[]

def agregar(rut, edad, nivel_glucosa, listado_glucosa):
    rut=int(input("ingrese el rut del cliente: "))
    edad=int(input("ingrese la edad: "))
    nivel_glucosa=int(input("ingrese el nivel de glucosa: "))
    listado_glucosa.append(nivel_glucosa)
        
    if (nivel_glucosa<100):
            estado_glucosa=("Nivel normal de glucosa")
            cont_normal=cont_normal+1
    if (nivel_glucosa>=100 and nivel_glucosa<=125):
            estado_glucosa=("Nivel de glucosa alterado")
            cont_alterado=cont_alterado+1
    if (nivel_glucosa>=126):
            estado_glucosa=("Nivel de glucosa riesgoso, se necesitan realizar mas pruebas")
            cont_riesgozo=cont_riesgozo+1
        
    tipo_sangre=input("ingrese el tipo de sangre (A, B, AB, O): ").upper()
        

    paciente={ 
        "Rut:\n": rut , 
        "Edad": edad,
        "Nivel de glucosa": nivel_glucosa, 
        "Estado de glucosa": estado_glucosa,
        "tipo de sangre": tipo_sangre
        }
    pacientes.append(paciente)