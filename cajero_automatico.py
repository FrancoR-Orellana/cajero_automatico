""" 1)      Escribir un programa que permita validar el ingreso a un sistema. 
Se deberá solicitar el ingreso por teclado de nombre de usuario y contraseña. 
Será valido como nombre de usuario “admin” y como contraseña “1234”. 
Si el ingreso es correcto deberá mostrar por pantalla el mensaje “Ingreso exitoso”.

Opcional 1: permitir como usuario valido también su propio nombre y su propia contraseña.

Opcional 2: solamente permitir el ingreso incorrecto de los datos 3 veces, luego de ello,
 no permitir más ingresos y mostrar por pantalla “Cuenta bloqueada”.

 2)      Mostrar por pantalla el siguiente menú:

CAJERO AUTOMATICO

ISPC

Listado de opciones:

1)      Ingreso de dinero

2)      Extracción de dinero

3)      Consulta de salto

4)      Salir

Ingrese su selección: _

El programa deberá mostrar luego del ingreso de cada opción “Usted ha seleccionado la opción x”, por ejemplo,
 en el caso de ingresar un 1, deberá mostrar por pantalla “Usted ha seleccionado la opción 1” y así sucesivamente. 
 Al seleccionar la opción 4 se debe terminar la ejecución del programa. 

 3)      Deberá continuar con el ejercicio 2 y escribir la lógica del cajero automático de la siguiente manera.

a.       Su saldo inicial será de $10000.

b.       Al seleccionar la opción 1 se pedirá al usuario que ingrese un importe por teclado el cual se sumará a su
 saldo inicial.

c.       De la misma manera al seleccionar la opción 2, se solicitará un importe por teclado el cual se restará
 al saldo inicial.

d.       Con la opción 3 se consultará su saldo actual.

e.       En todo momento se deberá contralar que no se pueda extraer dinero, si no se cuentan con fondos suficientes.

4)      Deberá en un solo programa unir el logueo del sistema con los ejercicios 2 y 3. Esto quiere decir que,
 si el ingreso al sistema es exitoso, se mostrará el menú del cajero automático y el usuario podrá comenzar a operar.

Opcional 3: Puede incluir parte de la lógica del programa en una o más funciones."""

#funciones

#acceso del usuario
def comprobar_usuario(a):
 	if(a == usuario_admin[0]):
 		return usuario_admin
 	elif(a == usuario_yo[0]):
 		return usuario_yo
 	else:
 		print('Ingrese un usuario registrado')
 		return None

def comprobar_contraseña(lista, contraseña):
 	if(contraseña == lista[1]):
 		return 'Ingreso exitoso'
 	else:
 		print('Contraseña incorrecta')
 		return None

 #menu de opciones

def desplegar_menu():
 	menu_opciones = ['1) Ingreso de dinero', '2) Extracción de dinero', '3) Consulta de saldo', '4) Salir']
 	for i in menu_opciones:
 		print(i)

def validar_opcion():
	desplegar_menu()
	seleccion_usuario = int(input('Selecciones el numero de la opcion deseada: '))
	if(seleccion_usuario == 1  or seleccion_usuario == 2 or seleccion_usuario == 3 or seleccion_usuario == 4):
		print('Usted a seleccionado la opcion ', seleccion_usuario)
		return seleccion_usuario
	else:
		print('Seleccione una opcion valida')
		return validar_opcion()

#acciones del usuario

def agregar_dinero(lista):
	monto_ingreso = int(input('Ingrese el monto que desea depositar: '))

	lista[2] += monto_ingreso
	repeticion(acciones_usuario, usuario_logueado)


def sacar_dinero(lista):
	monto_extracion = int(input('Ingrese el monto que desea retirar: '))

	if(lista[2] > monto_extracion):
		lista[2] -= monto_extracion
		repeticion(acciones_usuario, usuario_logueado)
	else:
		print('Puede extraer un maximo de: ', lista[2])
		return sacar_dinero(lista)

def consultar_saldo(lista):
	print('Usted posee un saldo de ', lista[2])
	repeticion(acciones_usuario, usuario_logueado)

def acciones_usuario(lista):
	opcion_usuario = validar_opcion()

	if(opcion_usuario == 1):
		agregar_dinero(lista)
	elif(opcion_usuario == 2):
		sacar_dinero(lista)
	elif(opcion_usuario == 3):
		consultar_saldo(lista)
	else:
		print('Gracias por usar nuestro servicio!')

#se da la opcion de realizar mas acciones sin salir del login

def repeticion(funcion, lista):
	continuar = input('Desea realizar mas acciones? Si o No: ')
	if(continuar.lower() == 'si' or continuar.lower() == 'no'):
		if(continuar == 'si'):
			return funcion(lista)
		else:
			print('Gracias por usar nuestro servicio!')
	else:
		print('Seleccione una opcion valida')
		return repeticion(funcion, lista)





#cuerpo principal

#variables y listas predefinidas
usuario_admin = ['admin', '1234', 10000]
usuario_yo = ['franco', '4321', 12000]
contador_errores = 0




#proceso de validacion

while contador_errores < 3:
	usuario_temporal = input('Ingrese su usuario: ')
	contraseña_usuario = input('Ingrese su contraseña: ')
	usuario_logueado = comprobar_usuario(usuario_temporal.lower())

	if(usuario_logueado):
		validar_contraseña = comprobar_contraseña(usuario_logueado, contraseña_usuario)
		if(validar_contraseña):
			print(validar_contraseña)
			contador_errores = 4
		else:
			contador_errores += 1

	else:
		contador_errores += 1



if(contador_errores != 3):
	#opciones para usuario logueado
	acciones_usuario(usuario_logueado)


else:
	print('Cuenta bloqueada bloqueada!')

