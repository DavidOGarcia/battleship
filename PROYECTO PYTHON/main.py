from usuario import Usuario
from random import randint
from os import system, name
from time import sleep
from barco import Barco
from colocar_barco import colocar_sub
from colocar_barco import colocar_fragata_v
from colocar_barco import colocar_fragata_h
from colocar_barco import colocar_v_buque
from colocar_barco import colocar_h_buque

def mapa(mar):
   """Función para crear la matriz 10x10
   Recibe por parámetros una lista vacía."""
   for i in range(10):
      mar.append([])
      for j in range(10):
         mar[i].append("O")
   return mar
#-------------------------------------------------------

barco = Barco(0,1)

def screen_clear():
   """Función para borrar lo que está escrito en la pantalla"""
   if name == 'nt':
      _ = system('cls')
   
   else:
      _ = system('clear')

#FUNCION PARA MOSTRAR LA MATRIZ 10X10 DE MANERA ORDENADA
def mostrar_mapa(m):
   """Función para ordenar visualmente el mapa de juego
   Recibe por parámetros una matriz"""
   print(" ")
   print("C | 1 2 3 4 5 6 7 8 9 10| F")
   n = 1
   for linea in m:
      print(" ", end = " ")
      print("|", end = " ")
      for elemento in linea:
         print(elemento,end = " ")
      print("|",n)
      n +=1

#FUNCION PARA MOSTRAR UNA MATRIZ EN DONDE SE VEA LA POSICION DE LOS BARCOS
def mostrar_m_fantasma(m_f):
   """Función para mostrar una matriz en donde se vea la posición de los barcos.
   Recibe por parámetros una matriz"""
   print("\n     MATRIZ FANTASMA\n")
   print("C | 1 2 3 4 5 6 7 8 9 10| F")
   n = 1
   for linea in m_f:
      print(" ", end = " ")
      print("|", end = " ")
      for elemento in linea:
         print(elemento,end = " ")
      print("|",n)
      n +=1

#----------------------------------------------------------------------------------------------------
#FUNCION PARA REALIZAR LOS DISPAROS EN LA MATRIZ    
def disparo(m,m_f):
   """Función para jugar el battleship. pide las filas y las columnas y luego imprime la matriz actualizada.
   Recibe por parámetros dos matrices, una que no tiene barcos(la que ve el jugador) y una que tiene barcos(la que no ve).   
   Retorna los intentos de disparos repetidos."""
   cont = 0
   while True:
      try:
         print("-"*50)
         f = int(input("Seleccione la fila a disparar: "))
         while f-1<0 or f>len(m):
               print("La fila que seleccionaste no se encuentra dentro del mapa. Por favor seleccione otra fila: \n")
               f = int(input("Seleccione la fila a disparar: "))
         break
      except ValueError:
         print("-"*50)
         print("La fila debe ser un número.")

   


   while True:
      try:
         print("-"*50)
         c = int(input("Seleccione la columna a disparar: "))
         while c-1<0 or c>len(m):
               print("La columna que seleccionaste no se encuentra dentro del mapa. Por favor seleccione otra fila: \n")
               c = int(input("Seleccione la columna a disparar: "))
         break
      except ValueError:
         print("-"*50)
         print("La columna debe ser un número.")

   

   if m[f-1][c-1] == "F" or m[f-1][c-1] == "X":
      print(" ")
      print("Ya has disparado a esa posición, escoge otra.")
      cont += 1
      return cont
      while True:
         try:
               print("-"*50)
               f = int(input("Seleccione la fila a disparar: "))
               break
         except ValueError:
               print("-"*50)
               print("La fila debe ser un número.")
      
      while f-1<0 or f>len(m):
         print("La fila que seleccionaste no se encuentra dentro del mapa. Por favor seleccione otra fila: \n")


      while True:
         try:
               print("-"*50)
               c = int(input("Seleccione la columna a disparar: "))
               break
         except ValueError:
               print("-"*50)
               print("La columna debe ser un número.")
      
      while c-1<0 or c>len(m):
         print("La columna que seleccionaste no se encuentra dentro del mapa. Por favor seleccione otra fila: \n")

   if m_f[f-1][c-1] == barco.mostrar_barco():
      m[f-1][c-1] = "F"
      m_f[f-1][c-1] = "F"
      screen_clear()
      print("Los números debajo de la 'F' representan las filas y los números al lado de la 'C' representan las columnas.\n  \n-Las 'O' en el mapa representan posiciones en las que aún no has disparado.\n-Las 'X' en el mapa representan las posiciones en las que disparaste y no acertaste.\n-Las 'F' en el mapa representan las posiciones en las que disparaste y acertaste.")
      mostrar_mapa(m)
      mostrar_m_fantasma(m_f)
      return 0

   else:
      m[f-1][c-1] = "X"
      m_f[f-1][c-1] = "X"
      screen_clear()
      print("Los números debajo de la 'F' representan las filas y los números al lado de la 'C' representan las columnas.\n  \n-Las 'O' en el mapa representan posiciones en las que aún no has disparado.\n-Las 'X' en el mapa representan las posiciones en las que disparaste y no acertaste.\n-Las 'F' en el mapa representan las posiciones en las que disparaste y acertaste.")
      mostrar_mapa(m)
      mostrar_m_fantasma(m_f)
      return 0

#---------------------------------------------------------------------------------------------------------------------------
def ver_usuarios():
   '''Función para ver los usuarios que ya han sido registrados'''
   try:
      lista = []
      usuarios = open("./registro_usuarios.txt", "r").readlines()

      for i in usuarios:
         usuario = i[:-1].split(",")

         lista.append(Usuario(usuario[0],usuario[1],usuario[2],usuario[3]))

      for i, user in enumerate(lista):
         print('-'*5, i+1, '-'*5)
         print(user)
   except FileNotFoundError:
      print(" ")
      print("Aún no se ha registrado ningún usuario.")

#---------------------------------------------------------------------------------------------------------------
def verificar_usuario_existe(username):
   '''Función para comprobar si el usuario ingresado ya está registrado.
   Recibe por parámetros un nombre de usuario.'''
   try:
      all_users = open("./registro_usuarios.txt", "r").readlines()
      for user in all_users:
         usuario = user[:-1].split(',') 
         if usuario[0] == username:
               return True
      return False
   except FileNotFoundError:
      print(" ")
      print("Aún no se ha registrado ningun usuario.")
      print(" ")
      return False

#-------------------------------------------------------------------------------------------------
def editar_usuario(user):
   '''Función para editar las características de los usuarios registrados. 
   Recibe por parámetros un número que corresponde a un usuario.'''
   
   datos = open("./registro_usuarios.txt", "r").readlines()
   
   while user > len(datos):
      print("El usuario que seleccionó no existe.")
      while True:
         try:
               user = int(input("Escoja un usuario:\n")) 
               break
         except ValueError:
               print("La respuesta debe ser un número.\n")

   while True:
      screen_clear()
      try:
         opcion = int(input("Seleccione la característica que desea editar:\n1)Username.\n2)Nombre.\n3)Edad.\n4)Género.\n"))
         print(" ")
         
         while opcion <1 or opcion > 4:
               print("Opción inválida.")
               print(" ")
               
               opcion = int(input("Seleccione la característica que desea editar:\n1)Username.\n2)Nombre.\n3)Edad.\n4)Género.\n"))
               print(" ")
         break
      except ValueError:
         print("La respuesta debe ser un número.\n")


   usuario = datos[user-1][:-1].split(",")

   if opcion == 1:
      screen_clear()
      while True:
         usuario[opcion - 1] = input("Ingrese el nuevo valor:\n")
         while len(usuario[opcion - 1]) == 0:
               usuario[opcion - 1] = input("Ingrese el nuevo valor:\n")
         
         while usuario[opcion - 1] != usuario[opcion - 1].replace(" ",""):

               print("-"*50)
               usuario[opcion - 1] = input("El nombre de usuario no puede contener espacios en blanco. Por favor vuelva a ingresar su nombre de usuario: \n")

         while usuario[opcion - 1] != usuario[opcion - 1].lower():

               print("-"*50)
               usuario[opcion - 1] = input("El nombre debe estar escrito en minúsculas. Por favor vuelva a ingresar su nombre de usuario: \n")

         while len(usuario[opcion - 1])>30:

               print("-"*50)
               usuario[opcion - 1] = input("El nombre de usuario a excedido el número de caracteres permitidos. Por favor ingrese otro nombre de usuario: \n")

         if (len(usuario[opcion - 1]) > 0 and usuario[opcion - 1] == usuario[opcion - 1].replace(" ","")) and (usuario[opcion - 1] == usuario[opcion - 1].lower() and len(usuario[opcion - 1])<30):
               break
               
   if opcion == 2:
      screen_clear()
      usuario[opcion - 1] = input("Ingrese el nuevo valor:\n")

      while len(usuario[opcion - 1]) == 0:
         print("-"*50)
         usuario[opcion - 1] = input("Ingrese el nuevo valor: \n").title()

   if opcion == 3:
      screen_clear()
      while True:
         try:
               usuario[opcion - 1] = int(input("Ingrese su edad(en números): \n"))
               while usuario[opcion - 1]<5 or usuario[opcion - 1] >100:
                  usuario[opcion - 1] = int(input("La edad no puede ser menor a 5 años ni mayor a 100 años. Igrese su edad otra vez:\n"))

               break
         except ValueError:
               print("-"*50)
               print("Error. La edad tiene que ser un número.")

   if opcion == 4:
      screen_clear()
      usuario[opcion - 1] = input("Ingrese su género. Masculino(M), Femenino(F), Otro(O): \n").upper()
      while usuario[opcion - 1].upper() != "M" and usuario[opcion - 1].upper() != "F" and usuario[opcion - 1].upper() != "O":
         print("Opción inválida. Vuelva a ingresar su respuesta.\n")
         usuario[opcion - 1] = input("Ingrese su género. Masculino(M), Femenino(F), Otro(O): \n").upper()

   nuevo_valor = ""
   for i in range(len(usuario)):
      if i != len(usuario) -1:
         nuevo_valor += usuario[i] + ','
      else:
         nuevo_valor += usuario[i] + '\n'
   datos[user - 1] = nuevo_valor
   with open("./registro_usuarios.txt", "w") as registro:
      registro.writelines(datos)
#-------------------------------------------------------------------
def registro():
   """Función para registrar los usuarios
   Retorna el nombre de usuario"""
   while True:
      
      user_name = input("Ingrese su nombre de usuario: \n")
      
      while len(user_name)==0:
         print("-"*50)
         user_name = input("Ingrese su nombre de usuario:\n")

      while user_name != user_name.replace(" ",""):

         print("-"*50)
         user_name = input("El nombre de usuario no puede contener espacios en blanco. Por favor vuelva a ingresar su nombre de usuario: \n")

      while user_name != user_name.lower():

         print("-"*50)
         user_name = input("El nombre de usuario debe estar escrito en minúsculas. Por favor vuelva a ingresar su nombre de usuario: \n")

      while len(user_name)>=30:

         print("-"*50)
         user_name = input("El nombre de usuario a excedido el número de caracteres permitidos. Por favor ingrese otro nombre de usuario: \n")
      if (len(user_name) > 0 and user_name == user_name.replace(" ","")) and (user_name == user_name.lower() and len(user_name)<30):
         break

   if verificar_usuario_existe(user_name):
      print(" ")
      print("Bienvenido!")
      print(" ")
      while True:
         try:
               iniciar = int(input("Presione '1' para comenzar el juego:\n"))
               while iniciar != 1:
                  print(" ")
                  print("Opción inválida. Vuelva ingresar su respuesta.")
                  print(" ")
                  iniciar = int(input("Presione '1' para comenzar el juego:\n"))
               break
         except ValueError:
               print(" ")
               print("La respuesta debe ser un número.")
               print(" ")
         
      return user_name
   else:
      print("Este usuario aún no está registrado. Procede a llenar los siguientes datos.")
      print("-"*50)
      nombre = input("Ingrese su nombre real: \n").title()
      while len(nombre) == 0:
         print("-"*50)
         nombre = input("Ingrese su nombre real: \n").title()
      print("-"*50)
      while True:
         try:
               edad = int(input("Ingrese su edad(en números): \n"))
               while edad<5 or edad >100:
                  edad = int(input("La edad no puede ser menor a 5 años ni mayor a 100 años. Igrese su edad otra vez:\n"))

               break
         except ValueError:
               print("-"*50)
               print("Error. La edad tiene que ser un número.")

      print("-"*50)
      genero = input("Ingrese su género. Masculino(M), Femenino(F), Otro(O): \n").upper()
      while genero.upper() != "M" and genero.upper() != "F" and genero.upper() != "O":
         print("Opción inválida. Vuelva a ingresar su respuesta.\n")
         genero = input("Ingrese su género. Masculino(M), Femenino(F), Otro(O): \n").upper()

   usuario = Usuario(user_name,nombre,edad,genero)

   with open("./registro_usuarios.txt", "a+") as registro:
      registro.write("{},{},{},{},{},{}\n".format(user_name,nombre,edad,genero,usuario.puntaje,usuario.disparos))
   print("El usuario: ", user_name, "se ha registrado correctamente.")
   print(" ")
   while True:
      try:
         iniciar = int(input("Presione '1' para comenzar el juego:\n"))
         while iniciar != 1:
               print(" ")
               print("Opción inválida. Vuelva ingresar su respuesta.")
               print(" ")
               iniciar = int(input("Presione '1' para comenzar el juego:\n"))
         break
      except ValueError:
         print(" ")
         print("La respuesta debe ser un número.")
         print(" ")
   return user_name

def inicio():
   """Función que muestra el menú de inicio"""
   while True:
      try:
         opciones = int(input("Bienvenido al juego de Batalla Naval. Escoja una de las siguientes opciones:\n1)Iniciar sesión.\n2)Ver los usuarios registrados\n3)Editar información del usuario.\n4)Datos de interés.\n"))
         while opciones <1 or opciones>4:
               opciones = int(input("Error, por favor ingrese una de las opciones presentadas anteriormente:\n"))
         break
      except ValueError:
         print("Error. La respuesta debe ser un número. Por favor ingrese una de las opciones presentadas anteriormente:\n")


   if opciones == 1:
      return True
   if opciones == 2:
      screen_clear()
      ver_usuarios()
      regresar = input("Presione 'r' para volver al menú de inicio:\n" )
      while regresar.lower() != "r":
         regresar = input("Opción inválida. Presione 'r' para volver al menú de inicio:\n")
      if regresar.lower() == "r":
         screen_clear()
         inicio()

   if opciones == 3:
      screen_clear()
      ver_usuarios()
      while True:
         try:
               user = int(input("Escoja un usuario:\n")) 
               break
         except ValueError:
               print("La respuesta debe ser un número.\n")
      
      editar_usuario(user) 
      
      regresar = input("Presione 'r' para volver al menú de inicio:\n" )
      while regresar.lower() != "r":
         regresar = input("Opción inválida. Presione 'r' para volver al menú de inicio:\n")
      if regresar.lower() == "r":
         screen_clear()
         inicio()
   if opciones == 4:
      screen_clear()
      while True:
         try:
               opcion = int(input("1)Rango de edad de los usuarios que más juegan.\n2)Cantidad total de puntos en partidas, por género.\n3)Promedio de disparos relizados para ganar.\n"))
               while opcion<1 or opcion >3:
                  opcion = int(input("Opción inválida. Por favor ingrese una de las opciones presentadas anteriormente.\n"))
               break
         except ValueError:
               print("La respuesta debe ser un número.")
               print(" ")
      
      if opcion == 1:
         screen_clear()
         edades()

         regresar = input("Presione 'r' para volver al menú de inicio:\n" )
         while regresar.lower() != "r":
               regresar = input("Opción inválida. Presione 'r' para volver al menú de inicio:\n")
         if regresar.lower() == "r":
               screen_clear()
               inicio()

      if opcion == 2:
         screen_clear()
         
         puntos_genero()

         regresar = input("Presione 'r' para volver al menú de inicio:\n" )
         while regresar.lower() != "r":
               regresar = input("Opción inválida. Presione 'r' para volver al menú de inicio:\n")
         if regresar.lower() == "r":
               screen_clear()
               inicio()
      
      if opcion == 3:
         screen_clear()
         disparos_prom()

         regresar = input("Presione 'r' para volver al menú de inicio:\n" )
         while regresar.lower() != "r":
               regresar = input("Opción inválida. Presione 'r' para volver al menú de inicio:\n")
         if regresar.lower() == "r":
               screen_clear()
               inicio()
        
def puntos_genero():
   """Función para sumar los puntos totales por género"""
   puntos_m = 0
   puntos_f = 0
   puntos_o = 0
   with open("./registro_usuarios.txt", "r") as p:
      puntos = p.readlines()
      for usuarios in puntos:
         usuario = usuarios[:-1].split(",")
         if usuario[3] == "M":
               puntos_m += int(usuario[4])
         elif usuario[3] == "F":
               puntos_f += int(usuario[4])
         else:
               puntos_o += int(usuario[4])
      print("Puntos totales Masculino: {}\nPuntos totales Femenino: {}\nPuntos totales Otro: {}".format(puntos_m,puntos_f,puntos_o))

def sumar_estadisticas(user_name,puntaje,disparos):
   """Función para sumar los puntos y los disparos realizados al usuarios después de cada partida.
   Recibe por parámetros nombre de usuario, puntaje y disparos."""
   all_users = open("./registro_usuarios.txt", "r").readlines()

   for i in range(len(all_users)):

      usuario = all_users[i][:-1].split(',') 
      nuevo_valor = ""
      if usuario[0] == user_name:

         usuario[4] = int(usuario[4]) + puntaje
         usuario[5] = int(usuario[5]) + disparos

      for j in range(len(usuario)):
         if j != len(usuario) -1:
               nuevo_valor += str(usuario[j]) + ','
         else:
               nuevo_valor += str(usuario[j]) + '\n'
      
      all_users[i] = nuevo_valor
      with open("./registro_usuarios.txt", "w") as bd:
         bd.writelines(all_users)

def disparos_prom():
   """Función para sacar el promedio de disparos realizados para ganar"""
   tot = 0
   sum_disparos = 0
   disparos = open("./disparos.txt", "r").readlines()
   for i in range(len(disparos)):
      sum_disparos += int(disparos[i])
      tot +=1
      
   disp_prom = sum_disparos//tot
   print("Promedio:",disp_prom,"disparos")

def edades():
   """Función para saber cuál es el rango de edad de los usuarios que más juegan"""
   usuario_1 = 0 
   usuario_2 = 0
   usuario_3 = 0
   usuario_4 = 0
   usuarios = open("./registro_usuarios.txt","r").readlines()
   for usuario in usuarios:
      user = usuario[:-1].split(",")
      if int(user[2])>=5 and int(user[2])<=18:
         usuario_1 +=1
         
      elif int(user[2])>=19 and int(user[2])<=45:
         usuario_2 +=1
         
      elif int(user[2])>=46 and int(user[2])<=60:
         usuario_3 +=1
         
      elif int(user[2])>=61 and int(user[2])<=100:
         usuario_4 +=1 
         
   
   if usuario_1>usuario_2 and usuario_1>usuario_3 and usuario_1>usuario_4:
      print("Edad: [5-18]")

   if usuario_2>usuario_1 and usuario_2>usuario_3 and usuario_2>usuario_4:
      print("Edad: [19-45]")

   if usuario_3>usuario_2 and usuario_3>usuario_1 and usuario_3>usuario_4:
      print("Edad: [46-60]")

   if usuario_4>usuario_2 and usuario_4>usuario_3 and usuario_4>usuario_1:
      print("Edad: [61-100]")           


def mostrar_top_10():
   """Función para ordenar y mostrar el top10 mejores jugadores"""
   print("Top 10 mejores jugadores\n")
   top = []
   user = []
   puntos = []
   disparos = []
   try:
      usuarios = open("./registro_usuarios.txt","r").readlines()
      try:
         for usuario in usuarios:
            jugador = usuario[:-1].split(",")
            user.append(jugador[0])
            puntos.append(int(jugador[4]))     
            disparos.append(jugador[5])
            top = zip(user,puntos,disparos)
            top = list(top)
            top = sorted(top,key = lambda jugadores : jugadores[1], reverse = True)
      except IndexError:
         return True
      for i, user in enumerate(top):
         print('-'*5, i+1, '-'*5)
         print(f"Usuario: {user[0]}\nPuntaje total: {user[1]}\nDisparos totales: {user[2]}")
         if i+1 == 10:
            print(" ")
            break
   except FileNotFoundError:
      print("Aún no hay jugadores.")
   
def orientacion_barcos(mapa_f):
   """Función para escoger si los barcos se van a posicionar de manera horizontal o vertical.
   Recibe por parámetro una matriz"""
   orientacion_b = randint(0,1)
   orientacion_f = randint(0,1)
   
   if orientacion_b == 1:
      colocar_v_buque(mapa_f)
      
   else:
      colocar_h_buque(mapa_f)
      
   if orientacion_f == 1:
      colocar_fragata_v(mapa_f)
   else:
      colocar_fragata_h(mapa_f)

   for i in range(4):
      colocar_sub(mapa_f)

def main():
   
   mostrar_top_10()
   empezar = input("Presiona 'enter' para seguir\n")
   while len(empezar)>0:
      empezar = input("Presiona 'enter' para seguir\n")
   screen_clear()
   print("Hint: Si eres Luis o Kevin y quieres agilizar el proceso de corrección te recomiendo revisar las lineas 121, 130 y 603 antes de empezar a jugar.")
   print(" ")
   inicio()
   screen_clear()
   user_name = registro()
   
   while True:
      screen_clear()
      print("Este es el mapa en el que se desarrollará el juego.\nLos números debajo de la 'F' representan las filas y los números al lado de la 'C' representan las columnas.\nTendrás que adivinar la fila y la columna en la cuál se encuentran los barcos para hundirlos.\nTienes un máximo de 70 intentos para hundir todos los barcos.\nSuerte!")
      cont_disp_a = 0
      cont_disp_repe = 0
      puntos = 0
      mar=[]
      mar_f=[]
      mapas = mapa(mar)
      mapa_f = mapa(mar_f)
      
      orientacion_barcos(mapa_f)

      mostrar_mapa(mapas)
      #mostrar_m_fantasma(mapa_f)
      while True:
         
         cont_disp_a = 0
         puntos = 0
         cont_disp_f = 0

         cont_disp_repe += disparo(mapas,mapa_f)

         for i in mapas:
               for j in i:
                  if j == "F":
                     puntos +=10
                     cont_disp_a +=1
                  elif j == "X":
                        puntos -=2
                        cont_disp_f +=1
         if puntos < 0:
            puntos = 0
         disparos = cont_disp_a + cont_disp_f
         puntaje = puntos
         print("disparos restantes: ",70-disparos)

         if puntaje == 90:
               screen_clear()
               print("Felicidades ! Ahora prueba sin ver la matriz de los barcos.")
               break
         elif cont_disp_a == 9:
               screen_clear()
               print("Felicidades! destruiste todos los barcos.")
               if disparos < 45:
                  screen_clear()
                  print("Tu estrategia fue excelente.")
                  break
               elif disparos >=45 and disparos < 70:
                  screen_clear()
                  print("Tu estrategia fue buena pero aún puedes mejorar.")
                  break
         elif disparos == 70:
               screen_clear()
               print("Has perdido, tienes que mejorar notablemente.")
               break  
      print(f""" 
   -Usuario: {user_name}
   -Cantidad de disparos realizados: {disparos}
   -Puntaje total: {puntaje}
   -Intentos de disparos repetidos: {cont_disp_repe}
      """)
      
      with open("./disparos.txt", "+a") as disp:
         disp.write("{}\n".format(disparos))
      
      sumar_estadisticas(user_name,puntaje,disparos)

      r = input("¿Desea jugar otra partida? sí(s)  no(n)\n")
      while r != "s" and r != "n":
         print("Opción incorrecta. Vuelva a ingresar su respuesta.\n")
         print(" ")
         r = input("¿Desea jugar otra partida? sí(s)  no(n)\n")
      if r == "n":
         break

main()
   

