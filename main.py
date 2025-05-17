from presentation.dataCollector import dataCollector

while True:
    print("-----------------------------------------------")
    print("1. Registrarse\n2. Iniciar Sesión\n0. Salir")
    op=input("Digite una opcion: ")
    print("-----------------------------------------------")
    match op:
        case "1":
            dc=dataCollector(True)
            dc.registration()
        case "2":
            dc=dataCollector(False)
            dc.login()
        case "0":
            print("\nFIN")
            break
        case _:
            print("\nIngreso no valido")
    
    

