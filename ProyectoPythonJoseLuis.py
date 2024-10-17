import json #importamos el json 
import requests #importamos el request (solicitud http)
class CuentaBancaria(): #creamos la clase Cuenta Bancaria, con sus atributos dentro y el constructor
    def __init__(self, nombre, DNI, IBAN, saldo):
        self.nombre = nombre
        self.DNI = DNI
        self.IBAN = IBAN
        self.saldo = saldo
    def diccionario(self): #funcion creada para pasar la lista a diccionario, que devuelve los atributos de la clase cuenta bancaria
        return{
            "Nombre": self.nombre,
            "DNI": self.DNI,
            "IBAN": self.IBAN,
            "Saldo": self.saldo
        }
        
    
def crearCuenta(cuenta): #funcion crear cuenta
    cuentas.append(cuenta) # añadimos el objeto cuenta a la lista de cuentas donde se almacenan las cuentas Bancarias
    if (cuentas != None): #comprobamos que la lista no esté vacía y mandamos un mensaje de confirmación
        print("La cuenta se ha creado correctamente")
    else: #si no se mete de forma correcta el objeto, se saca un mensaje de error
        print("No se ha creado la cuenta")
def cuentasDisponibles(cuentas): #funcion cuentasDisponibles
    for cuenta in cuentas: #recorremos la lista con el fin de mostrar todos los datos de la misma
        print(f"Titular: {cuenta.nombre}, DNI: {cuenta.DNI}, IBAN: {cuenta.IBAN}, saldo: {cuenta.saldo}")
        #usamos la f para poder mostrar y concatenar string e int
def ficheroJSON(listaCuentas): #funcion JSON
    listadoDiccionario = [cuenta.diccionario() for cuenta in listaCuentas] #pasamos la lista a un tipo diccionario con el fin de poder almacenar la información en el archivo
    with open('ficheroJSON', 'w') as archivo: #creamos el fichero, con el nombre ficheroJSON en tipo escritura
        json.dump(listadoDiccionario, archivo) #añadimos la lista del diccionario al fichero
    print("Se ha almacenado la informacion en el archivo") # mensaje de éxito

def buscarCuenta(titular, listadoCuentas): #funcion buscar cuenta por nombre del titular
    for cuentas in listadoCuentas: #recorremos la lista
        if cuentas.nombre == titular: # si el nombre que ha introducido el usuario es igual que algún titular de alguna cuenta de la lista
            print(f"Titular: {cuentas.nombre}, DNI: {cuentas.DNI}, IBAN: {cuentas.IBAN}, saldo: {cuentas.saldo}") #imprimimos la informacion de la cuenta

def sacarDinero(IBAN, listadoCuentas): #funcion sacar dinero
    for cuentas in listadoCuentas: #recorremos la lista
        if cuentas.IBAN == IBAN: #si el IBAN que ha introducido el usuario es igual que algún IBAN de alguna cuenta de la lista
            try: #añadimos un try para añadir una excepción, en este caso ValueError, que hace que si introducimos un valor que no sea un número cuando es indicado, salta el error
                dinero = int(input("Introduce la cantidad de dinero que quieras sacar: ")) #pedimos la cantidad de dinero que quiere sacar el usuario
                if (dinero > cuentas.saldo): #si la cantidad de dinero introducido por el usuario es mayor que el saldo de la cuenta
                    print("No hay tanto dinero en la cuenta. Selecicone otra cantidad") #mensaje de error
                else: #sino
                    cuentas.saldo -= dinero #actualizamos la nueva cantidad de dinero
                    print("Se ha sacado el dinero") #mensaje de éxito
            except ValueError: #excepción
                print("Introduce un número válido") 
            return 
        else:
            print("No hay una cuenta con ese IBAN")

def ingresarDinero(IBAN,listadoCuentas): #funcion ingresar dinero y hacemos el mismo método que la función anterior
    for cuentas in listadoCuentas:
        if cuentas.IBAN == IBAN:
            try: 
                dinero = int(input("Introduce la cantidad de dinero que quieras ingresar: "))
                if(dinero < 0): #comprobamos que la cantidad de dinero introducida sea positiva
                    print("La cantidad de dinero debe de ser positiva")
                else:
                    cuentas.saldo += dinero #ingresamos el dinero sumando la cantidad de dinero que introduce el usuario al saldo de la cuenta 
                    print("Dinero ingresado")
            except ValueError:
                print("Intoduce un formato de número válido")
        else: 
            print("El número de IBAN no existe como cuenta")

def accederPaginaBanco(): #funcion acceder página del banco
    url = 'https://www.bbva.es/personas.html' #ponemos la dirección URL y la guardamos en una variable
    respuesta = requests.get(url) #realizamos una petición get a la dirección URL y guardamos la respuesta en una variable
    if(respuesta.status_code == 200): #si la petición es aceptada, nos saltará el código 200, que se encarga de que el servidor nos devuelta los datos solicitados
        print("Se ha conectado de forma correcta \n") # mensaje de éxito
        print("Servidor: ")
        print(respuesta.text) #imprimimos la respuesta del servidor
    else: #si el servidor no devuelve los datos solicitados
        print("Error") #imprimimos un mensaje de error
    

opcion = -1 #inicializamos la variable opcion
cuentas = [] #creacion de una lista en donde se almacenarán las cuentas
while (opcion != 0): # hacemos un while para que haya un bucle hasta que el usuario decida salir
    print("\n1. ABRIR UNA CUENTA BANCARIA \n2. VER LAS CUENTAS DISPONIBLES \n3. ALMACENAR LAS CUENTAS BANCARIAS EN UN FICHERO JSON \n4. BUSCAR CUENTA BANCARIA POR TITULAR \n5. INGRESAR O SACAR DINERO DE LA CUENTA \n6. ORDENAR CUENTAS POR SALDO \n7. ACCEDER PÁGINA BANCO \n0. SALIR") #creacion del menú
    opcion = int(input("Introduce la opcion: "))
    match opcion: #hacemos un match, para separar las distintas opciones
        case 1: #caso 1
            print("Has seleccionado abrir una cuenta bancaria")
            #leemos las variables que se piden para crear una cuenta bancaria
            nombre = input("Introduce el nombre del titular:")
            DNI = input("Introduce el DNI del titular: ")
            IBAN = input("Introduce el número de cuenta: ")
            saldo = int(input("Introduce el saldo de la cuenta: "))
            cuenta = CuentaBancaria(nombre,DNI,IBAN,saldo) #introducimos las variables creadas dentro de un objeto de la clase Cuenta Bancaria
            crearCuenta(cuenta) #pasamos el objeto a la funcion crearCuenta
        case 2: #caso 2
            print("Cuentas disponibles: ")
            cuentasDisponibles(cuentas) #llamamos a la funcion encargadad de mostrar las cuentas,  pasando la lista cuentas
        case 3: #caso 3
            ficheroJSON(cuentas) #llamamos a la funcion para crear el fichero JSON, pasando la lista
        case 4: #caso 4
            titular = input("Introduce el nombre del titular: ") #pedimos al usuario el nombre del titular de la cuenta
            buscarCuenta(titular, cuentas) #llamamos a la función, pasando el nombre del titular y la lista
        case 5: #caso 5
            IBAN = input("Introduce el número de cuenta: ") #introduce el usuario el número de IBAN
            opcion1 = int(input("Introduce 1 si quiere sacar dinero y 2 si quiere ingresar dinero: ")) #damos opción al usuario a sacar o ingresar dinero
            if (opcion1 == 1):
                sacarDinero(IBAN, cuentas) #llamamos a la función sacar dinero, pasando la lista y el número de IBAN introducido por el usuario
            elif (opcion1 == 2):
                ingresarDinero(IBAN, cuentas) #llamamos a la función ingresar dinero, pasando la lista y el número de IBAN introducido por el usuario
        case 6: #caso 6
            cuentasOrdenadas = sorted(cuentas, key=lambda cuenta: cuenta.saldo)  # Ordena las cuentas por saldo, usando un lambda, con la función sorted
            print("Cuentas ordenadas por saldo:\n")
            for cuenta in cuentasOrdenadas: #recorremos la lista una vez ordenada
                print(f"Titular: {cuenta.nombre}, DNI: {cuenta.DNI}, IBAN: {cuenta.IBAN}, Saldo: {cuenta.saldo}") #imprimimos la lista ordenada 
        case 7: #caso 7
            accederPaginaBanco(); #llamamos a la funcion

