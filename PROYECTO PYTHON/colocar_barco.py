from random import randint
from barco import Barco
tamaño = 1
posicion = 0
barco = Barco(posicion,tamaño)
def colocar_sub(m):
    """Función para colocar los submarinos(barcos de una posición) en la matriz """
    fila = randint(1,len(m))-1
    col = randint(1,len(m))-1
     
     
     
    if col == 9:
        if fila == 0:
            if  m[fila][col] != barco.mostrar_barco() or m[fila+1][col] != barco.mostrar_barco() or m[fila][col-1] != barco.mostrar_barco():
                 
                 
                 
                m[fila][col] = barco.mostrar_barco()

            
        elif fila == 9:
            if  m[fila][col] != barco.mostrar_barco() or m[fila-1][col] != barco.mostrar_barco() or m[fila][col-1] != barco.mostrar_barco():
                 
                 
                 
                m[fila][col] = barco.mostrar_barco()

            
        else:
            while fila == 0 or fila == 9 or col != 9 or m[fila][col] == barco.mostrar_barco() or m[fila-1][col] == barco.mostrar_barco() or m[fila][col-1] == barco.mostrar_barco() or m[fila+1][col] == barco.mostrar_barco():
                fila = randint(1,len(m))-1
                col = randint(1,len(m))-1

             
            m[fila][col] = barco.mostrar_barco()

    elif col == 0:

        if fila == 0:
            while m[fila][col] == barco.mostrar_barco() or m[fila+1][col] == barco.mostrar_barco() or m[fila][col+1] == barco.mostrar_barco():
                fila = 0
                col = randint(1,len(m))-1
                
                 
                 
                while col == 0 or col == 9 or m[fila][col] == barco.mostrar_barco() or m[fila][col-1] == barco.mostrar_barco() or m[fila][col+1] == barco.mostrar_barco() or m[fila+1][col] == barco.mostrar_barco():
                    fila = 0
                    col = randint(1,len(m))-1
  
             
            m[fila][col] = barco.mostrar_barco()
        elif fila == 9:
            while m[fila][col] == barco.mostrar_barco() or m[fila-1][col] == barco.mostrar_barco() or m[fila][col+1] == barco.mostrar_barco():
                fila = 9
                col = randint(1,len(m))-1
     
                while col == 0 or col ==9 or m[fila][col] == barco.mostrar_barco() or m[fila][col-1] == barco.mostrar_barco() or m[fila][col+1] == barco.mostrar_barco() or m[fila-1][col] == barco.mostrar_barco():
                    fila = 9
                    col = randint(1,len(m))-1
    
            m[fila][col] = barco.mostrar_barco()
        else:
            while fila == 0 or fila == 9 or col != 0 or m[fila][col] == barco.mostrar_barco() or m[fila-1][col] == barco.mostrar_barco() or m[fila][col+1] == barco.mostrar_barco() or m[fila+1][col] == barco.mostrar_barco():
                fila = randint(1,len(m))-1
                col = randint(1,len(m))-1
 
             
            m[fila][col] = barco.mostrar_barco()
    else:
        if fila == 0:
            while fila !=0 or col == 0 or col == 9 or m[fila][col] == barco.mostrar_barco() or m[fila+1][col] == barco.mostrar_barco() or m[fila][col+1] == barco.mostrar_barco() or m[fila][col-1] == barco.mostrar_barco():
                fila = randint(1,len(m))-1
                col = randint(1,len(m))-1

            m[fila][col] = barco.mostrar_barco()

        elif fila == 9:
            while fila !=9 or col == 0 or col == 9 or m[fila][col] == barco.mostrar_barco() or m[fila-1][col] == barco.mostrar_barco() or m[fila][col+1] == barco.mostrar_barco() or m[fila][col-1] == barco.mostrar_barco():
                fila = randint(1,len(m))-1
                col = randint(1,len(m))-1
    
            m[fila][col] = barco.mostrar_barco()
        else:
            while fila == 0 or fila ==9 or col == 0 or col == 9 or m[fila][col] == barco.mostrar_barco() or m[fila-1][col] == barco.mostrar_barco() or m[fila+1][col] == barco.mostrar_barco() or m[fila][col+1] == barco.mostrar_barco() or m[fila][col-1] == barco.mostrar_barco():
                fila = randint(1,len(m))-1
                col = randint(1,len(m))-1
  
            m[fila][col] = barco.mostrar_barco()
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def colocar_fragata_v(m):
    """Función para colocar las fragatas(barco de dos posiciones) de forma vertical"""    
    fila = randint(1,len(m))-1
    col = randint(1,len(m))-1
    
    while fila+2>len(m):
        fila = randint(1,len(m))-1
        col = randint(1,len(m))-1
        
    while fila == 9:
        fila = randint(1,len(m))-1
        col = randint(1,len(m))-1
       
    if fila != 0:

        if col == 0:
            while col !=0 or fila == 9 or fila == 0 or(fila+2>len(m)) or (m[fila-1][col] == barco.mostrar_barco() or m[fila][col] == barco.mostrar_barco() or m[fila+1][col] == barco.mostrar_barco() or m[fila][col+1] == barco.mostrar_barco() or m[fila+1][col+1] == barco.mostrar_barco()):
                fila = randint(1,len(m))-1
                col = randint(1,len(m))-1
          
            m[fila][col] = barco.mostrar_barco()
            m[fila+1][col] = barco.mostrar_barco()
            
            
        elif col == 9:
            if fila +1 == len(m)-1:
                while col !=9 or fila == 9  or fila == 0 or (fila+2>len(m)) or (m[fila-1][col] == barco.mostrar_barco() or m[fila][col] == barco.mostrar_barco() or m[fila+1][col] == barco.mostrar_barco()  or m[fila][col-1] == barco.mostrar_barco() or m[fila+1][col-1] == barco.mostrar_barco()):
                    fila = randint(1,len(m))-1
                    col = randint(1,len(m))-1
               
                m[fila][col] = barco.mostrar_barco()
                m[fila+1][col] = barco.mostrar_barco()
                
            else:
                while col !=9 or fila == 9  or fila == 0 or (fila+3>len(m)) or (m[fila][col-1] == barco.mostrar_barco() or m[fila][col] == barco.mostrar_barco() or m[fila+1][col] == barco.mostrar_barco() or m[fila][col-1] == barco.mostrar_barco() or m[fila+1][col-1] == barco.mostrar_barco() or m[fila+2][col] == barco.mostrar_barco()):
                    fila = randint(1,len(m))-1
                    col = randint(1,len(m))-1
                   
                m[fila][col] = barco.mostrar_barco()
                m[fila+1][col] = barco.mostrar_barco()
                

        else:
            if fila+1 == len(m)-1:

                while (fila+2>len(m)) or (m[fila-1][col] == barco.mostrar_barco() or m[fila][col] == barco.mostrar_barco() or m[fila+1][col] == barco.mostrar_barco() or m[fila][col+1] == barco.mostrar_barco() or m[fila+1][col+1] == barco.mostrar_barco() or m[fila][col-1] == barco.mostrar_barco() or m[fila+1][col-1] == barco.mostrar_barco()):
                
                    fila = randint(1,len(m))-1
                    col = randint(1,len(m))-1
                    
                    while (fila == 0 or fila == 9 or col == 9 or col == 0):
                        fila = randint(1,len(m))-1
                        col = randint(1,len(m))-1
                        
                m[fila][col] = barco.mostrar_barco()
                m[fila+1][col] = barco.mostrar_barco()
                


            else:
                while (fila+3>len(m)) or (m[fila-1][col] == barco.mostrar_barco() or m[fila][col] == barco.mostrar_barco() or m[fila+1][col] == barco.mostrar_barco() or m[fila][col+1] == barco.mostrar_barco() or m[fila+1][col+1] == barco.mostrar_barco() or m[fila][col-1] == barco.mostrar_barco() or m[fila+1][col-1] == barco.mostrar_barco()  or m[fila+2][col] == barco.mostrar_barco()):
                    
                    fila = randint(1,len(m))-1
                    col = randint(1,len(m))-1
                    
                    while (fila == 0 or fila == 9 or col == 9 or col == 0):
                        fila = randint(1,len(m))-1
                        col = randint(1,len(m))-1
                        
                m[fila][col] = barco.mostrar_barco()
                m[fila+1][col] = barco.mostrar_barco()
                

    elif col == 0:
        while (fila+2>len(m)) or (m[fila][col] == barco.mostrar_barco() or m[fila+1][col] == barco.mostrar_barco() or m[fila][col+1] == barco.mostrar_barco() or m[fila+1][col+1] == barco.mostrar_barco()):
            fila = randint(1,len(m))-1
            col = randint(1,len(m))-1
        
        m[fila][col] = barco.mostrar_barco()
        m[fila+1][col] = barco.mostrar_barco()
        
            
    elif col == 9:
        while (fila+2>len(m)) or (m[fila][col] == barco.mostrar_barco() or m[fila][col-1] == barco.mostrar_barco() or m[fila+1][col] == barco.mostrar_barco() or m[fila+1][col-1] == barco.mostrar_barco()):
            fila = randint(1,len(m))-1
            col = randint(1,len(m))-1
            
        m[fila][col] = barco.mostrar_barco()
        m[fila+1][col] = barco.mostrar_barco()
        
    else:
        while (fila != 0 or fila == 9 or col == 9 or col == 0) or(fila+3>len(m)) or (m[fila][col] == barco.mostrar_barco() or m[fila-1][col] == barco.mostrar_barco() or m[fila+1][col] == barco.mostrar_barco()  or m[fila][col-1] == barco.mostrar_barco() or m[fila+1][col-1] == barco.mostrar_barco()  or m[fila][col+1] == barco.mostrar_barco() or m[fila+1][col+1] == barco.mostrar_barco() or m[fila+2][col] == barco.mostrar_barco()):
            fila = randint(1,len(m))-1
            col = randint(1,len(m))-1
            
        m[fila][col] = barco.mostrar_barco()
        m[fila+1][col] = barco.mostrar_barco()

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def colocar_fragata_h(m):
    """Función para colocar las fragatas(barco de dos posiciones) de manera horizontal"""
    fila = randint(1,len(m))-1
    col = randint(1,len(m))-1
    
    while col+2>len(m):
        fila = randint(1,len(m))-1
        col = randint(1,len(m))-1
        
    while col == 9:
        fila = randint(1,len(m))-1
        col = randint(1,len(m))-1
        
    if col != 0:

        if fila == 0:
            while fila !=0 or col == 9 or col == 0 or(col+2>len(m)) or (m[fila][col-1] == barco.mostrar_barco() or m[fila][col] == barco.mostrar_barco() or m[fila][col+1] == barco.mostrar_barco() or m[fila+1][col] == barco.mostrar_barco() or m[fila+1][col+1] == barco.mostrar_barco()):
                fila = randint(1,len(m))-1
                col = randint(1,len(m))-1
              
            m[fila][col] = barco.mostrar_barco()
            m[fila][col+1] = barco.mostrar_barco()
            
            
        elif fila == 9:
            if col +1 == len(m)-1:
                while fila !=9 or col == 9  or col == 0 or (col+2>len(m)) or (m[fila][col-1] == barco.mostrar_barco() or m[fila][col] == barco.mostrar_barco() or m[fila][col+1] == barco.mostrar_barco()  or m[fila-1][col] == barco.mostrar_barco() or m[fila-1][col+1] == barco.mostrar_barco()):
                    fila = randint(1,len(m))-1
                    col = randint(1,len(m))-1
                    
                m[fila][col] = barco.mostrar_barco()
                m[fila][col+1] = barco.mostrar_barco()
                
            else:
                while fila !=9 or col == 9  or col == 0 or (col+3>len(m)) or (m[fila-1][col] == barco.mostrar_barco() or m[fila][col] == barco.mostrar_barco() or m[fila][col+1] == barco.mostrar_barco() or m[fila-1][col] == barco.mostrar_barco() or m[fila-1][col+1] == barco.mostrar_barco() or m[fila][col+2] == barco.mostrar_barco()):
                    fila = randint(1,len(m))-1
                    col = randint(1,len(m))-1
                
                m[fila][col] = barco.mostrar_barco()
                m[fila][col+1] = barco.mostrar_barco()
                

        else:
            if col+1 == len(m)-1:

                while (col+2>len(m)) or (m[fila][col-1] == barco.mostrar_barco() or m[fila][col] == barco.mostrar_barco() or m[fila][col+1] == barco.mostrar_barco() or m[fila+1][col] == barco.mostrar_barco() or m[fila+1][col+1] == barco.mostrar_barco() or m[fila-1][col] == barco.mostrar_barco() or m[fila-1][col+1] == barco.mostrar_barco()):
                
                    fila = randint(1,len(m))-1
                    col = randint(1,len(m))-1
                    
                    while (fila == 0 or fila == 9 or col == 9 or col == 0):
                        fila = randint(1,len(m))-1
                        col = randint(1,len(m))-1
                  
                m[fila][col] = barco.mostrar_barco()
                m[fila][col+1] = barco.mostrar_barco()
                


            else:
                while (col+3>len(m)) or (m[fila][col-1] == barco.mostrar_barco() or m[fila][col] == barco.mostrar_barco() or m[fila][col+1] == barco.mostrar_barco() or m[fila+1][col] == barco.mostrar_barco() or m[fila+1][col+1] == barco.mostrar_barco() or m[fila-1][col] == barco.mostrar_barco() or m[fila-1][col+1] == barco.mostrar_barco()  or m[fila][col+2] == barco.mostrar_barco()):
                    
                    fila = randint(1,len(m))-1
                    col = randint(1,len(m))-1
                    
                    while (fila == 0 or fila == 9 or col == 9 or col == 0):
                        fila = randint(1,len(m))-1
                        col = randint(1,len(m))-1
                   
                m[fila][col] = barco.mostrar_barco()
                m[fila][col+1] = barco.mostrar_barco()
                

    elif fila == 0:
        while (col+2>len(m)) or (m[fila][col] == barco.mostrar_barco() or m[fila][col+1] == barco.mostrar_barco() or m[fila+1][col] == barco.mostrar_barco() or m[fila+1][col+1] == barco.mostrar_barco()):
            fila = randint(1,len(m))-1
            col = randint(1,len(m))-1
            
        m[fila][col] = barco.mostrar_barco()
        m[fila][col+1] = barco.mostrar_barco()
        
            
    elif fila == 9:
        while (col+2>len(m)) or (m[fila][col] == barco.mostrar_barco() or m[fila][col+1] == barco.mostrar_barco() or m[fila-1][col] == barco.mostrar_barco() or m[fila-1][col+1] == barco.mostrar_barco()):
            fila = randint(1,len(m))-1
            col = randint(1,len(m))-1
          
        m[fila][col] = barco.mostrar_barco()
        m[fila][col+1] = barco.mostrar_barco()
        
    else:
        while (col != 0 or col == 9 or fila == 9 or fila == 0) or(col+3>len(m)) or (m[fila][col] == barco.mostrar_barco() or m[fila][col-1] == barco.mostrar_barco() or m[fila][col+1] == barco.mostrar_barco()  or m[fila-1][col] == barco.mostrar_barco() or m[fila-1][col+1] == barco.mostrar_barco()  or m[fila+1][col] == barco.mostrar_barco() or m[fila+1][col+1] == barco.mostrar_barco() or m[fila][col+2] == barco.mostrar_barco()):
            fila = randint(1,len(m))-1
            col = randint(1,len(m))-1
          
        m[fila][col] = barco.mostrar_barco()
        m[fila][col+1] = barco.mostrar_barco()

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def colocar_v_buque(m):
    """Función para colocar los buques(barco de tres posiciones) de manera vertical"""
    fila = randint(1,len(m))-1
    col = randint(1,len(m))-1
  
    while fila+3>len(m):
        fila = randint(1,len(m))-1
        col = randint(1,len(m))-1
        
    while fila == 9:
        fila = randint(1,len(m))-1
        col = randint(1,len(m))-1
        
    if fila != 0:

        if col == 0:

            while fila == 9 or fila == 0 or(fila+3>len(m)) or (m[fila-1][col] == barco.mostrar_barco() or m[fila][col] == barco.mostrar_barco() or m[fila+1][col] == barco.mostrar_barco() or m[fila+2][col] == barco.mostrar_barco() or m[fila][col+1] == barco.mostrar_barco() or m[fila+1][col+1] == barco.mostrar_barco() or m[fila+2][col+1] == barco.mostrar_barco()):
                fila = randint(1,len(m))-1
                col = 0
                
            m[fila][col] = barco.mostrar_barco()
            m[fila+1][col] = barco.mostrar_barco()
            m[fila+2][col] = barco.mostrar_barco()
            
        elif col == 9:
            if fila +2 == len(m)-1:
                while fila == 9  or fila == 0 or (fila+3>len(m)) or (m[fila-1][col] == barco.mostrar_barco() or m[fila][col] == barco.mostrar_barco() or m[fila+1][col] == barco.mostrar_barco() or m[fila+2][col] == barco.mostrar_barco() or m[fila][col-1] == barco.mostrar_barco() or m[fila+1][col-1] == barco.mostrar_barco() or m[fila+2][col-1] == barco.mostrar_barco()):
                    fila = randint(1,len(m))-1
                    col = 9
                  
                m[fila][col] = barco.mostrar_barco()
                m[fila+1][col] = barco.mostrar_barco()
                m[fila+2][col] = barco.mostrar_barco()
            else:
                while (m[fila][col] == barco.mostrar_barco() or m[fila+1][col] == barco.mostrar_barco() or m[fila+2][col] == barco.mostrar_barco() or m[fila][col-1] == barco.mostrar_barco() or m[fila+1][col-1] == barco.mostrar_barco() or m[fila+2][col-1] == barco.mostrar_barco() or m[fila+3][col] == barco.mostrar_barco()):
                    while fila == 9  or fila == 0:
                        fila = randint(1,len(m))-1
                        col = 9
                 
                m[fila][col] = barco.mostrar_barco()
                m[fila+1][col] = barco.mostrar_barco()
                m[fila+2][col] = barco.mostrar_barco()

        else:
            if fila+2 == len(m)-1:

                while (fila+3>len(m)) or (m[fila-1][col] == barco.mostrar_barco() or m[fila][col] == barco.mostrar_barco() or m[fila+1][col] == barco.mostrar_barco() or m[fila+2][col] == barco.mostrar_barco() or m[fila][col+1] == barco.mostrar_barco() or m[fila+1][col+1] == barco.mostrar_barco() or m[fila+2][col+1] == barco.mostrar_barco() or m[fila][col-1] == barco.mostrar_barco() or m[fila+1][col-1] == barco.mostrar_barco() or m[fila+2][col-1] == barco.mostrar_barco()):
                
                    fila = randint(1,len(m))-1
                    col = randint(1,len(m))-1
                    
                    while (fila == 0 or fila == 9 or col == 9 or col == 0):
                        fila = randint(1,len(m))-1
                        col = randint(1,len(m))-1
                        
                m[fila][col] = barco.mostrar_barco()
                m[fila+1][col] = barco.mostrar_barco()
                m[fila+2][col] = barco.mostrar_barco()


            else:
                while (fila+4>len(m)) or (m[fila-1][col] == barco.mostrar_barco() or m[fila][col] == barco.mostrar_barco() or m[fila+1][col] == barco.mostrar_barco() or m[fila+2][col] == barco.mostrar_barco() or m[fila][col+1] == barco.mostrar_barco() or m[fila+1][col+1] == barco.mostrar_barco() or m[fila+2][col+1] == barco.mostrar_barco() or m[fila][col-1] == barco.mostrar_barco() or m[fila+1][col-1] == barco.mostrar_barco() or m[fila+2][col-1] == barco.mostrar_barco() or m[fila+3][col] == barco.mostrar_barco()):
                    
                    fila = randint(1,len(m))-1
                    col = randint(1,len(m))-1
                    
                    while (fila == 0 or fila == 9 or col == 9 or col == 0):
                        fila = randint(1,len(m))-1
                        col = randint(1,len(m))-1
                        
                m[fila][col] = barco.mostrar_barco()
                m[fila+1][col] = barco.mostrar_barco()
                m[fila+2][col] = barco.mostrar_barco()

    elif col == 0:
        while (fila+3>len(m)) or (m[fila][col] == barco.mostrar_barco() or m[fila+1][col] == barco.mostrar_barco() or m[fila+2][col] == barco.mostrar_barco() or m[fila][col+1] == barco.mostrar_barco() or m[fila+1][col+1] == barco.mostrar_barco() or m[fila+2][col+1] == barco.mostrar_barco()):
            fila = randint(1,len(m))-1
            col = randint(1,len(m))-1
            
        m[fila][col] = barco.mostrar_barco()
        m[fila+1][col] = barco.mostrar_barco()
        m[fila+2][col] = barco.mostrar_barco()
            
    elif col == 9:
        while (fila+3>len(m)) or (m[fila][col] == barco.mostrar_barco() or m[fila+1][col] == barco.mostrar_barco() or m[fila+2][col] == barco.mostrar_barco() or m[fila][col-1] == barco.mostrar_barco() or m[fila+1][col-1] == barco.mostrar_barco() or m[fila+2][col-1] == barco.mostrar_barco()):
            fila = randint(1,len(m))-1
            col = randint(1,len(m))-1
            
        m[fila][col] = barco.mostrar_barco()
        m[fila+1][col] = barco.mostrar_barco()
        m[fila+2][col] = barco.mostrar_barco()
    else:
        while (fila != 0 or fila == 9 or col == 9 or col == 0) or(fila+4>len(m)) or (m[fila][col] == barco.mostrar_barco() or m[fila-1][col] == barco.mostrar_barco() or m[fila+1][col] == barco.mostrar_barco() or m[fila+2][col] == barco.mostrar_barco() or m[fila][col-1] == barco.mostrar_barco() or m[fila+1][col-1] == barco.mostrar_barco() or m[fila+2][col-1] == barco.mostrar_barco() or m[fila][col+1] == barco.mostrar_barco() or m[fila+1][col+1] == barco.mostrar_barco() or m[fila+2][col+1] == barco.mostrar_barco() or m[fila+3][col] == barco.mostrar_barco()):
            fila = randint(1,len(m))-1
            col = randint(1,len(m))-1
            
        m[fila][col] = barco.mostrar_barco()
        m[fila+1][col] = barco.mostrar_barco()
        m[fila+2][col] = barco.mostrar_barco()

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def colocar_h_buque(m):
    """Función para colocar los buques(barco de tres posiciones) de manera horizontal"""
    fila = randint(1,len(m))-1
    col = randint(1,len(m))-1
    
    while col+3>len(m):
        fila = randint(1,len(m))-1
        col = randint(1,len(m))-1
        
    while col == 9:
        fila = randint(1,len(m))-1
        col = randint(1,len(m))-1
        
    if col != 0:

        if fila == 0:
            while col == 9 or col == 0 or(col+3>len(m)) or (m[fila][col-1] == barco.mostrar_barco() or m[fila][col] == barco.mostrar_barco() or m[fila][col+1] == barco.mostrar_barco() or m[fila][col+2] == barco.mostrar_barco() or m[fila+1][col] == barco.mostrar_barco() or m[fila+1][col+1] == barco.mostrar_barco() or m[fila+1][col+2] == barco.mostrar_barco()):
                fila = 0
                col = randint(1,len(m))-1
                
            m[fila][col] = barco.mostrar_barco()
            m[fila][col+1] = barco.mostrar_barco()
            m[fila][col+2] = barco.mostrar_barco()
            
        elif fila == 9:
            if col +2 == len(m)-1:
                while col == 9  or col == 0 or (col+3>len(m)) or (m[fila][col-1] == barco.mostrar_barco() or m[fila][col] == barco.mostrar_barco() or m[fila][col+1] == barco.mostrar_barco() or m[fila][col+2] == barco.mostrar_barco() or m[fila-1][col] == barco.mostrar_barco() or m[fila-1][col+1] == barco.mostrar_barco() or m[fila-1][col+2] == barco.mostrar_barco()):
                    fila = 9
                    col = randint(1,len(m))-1
                    
                m[fila][col] = barco.mostrar_barco()
                m[fila][col+1] = barco.mostrar_barco()
                m[fila][col+2] = barco.mostrar_barco()
            else:
                while (col+4>len(m)) or (m[fila-1][col] == barco.mostrar_barco() or m[fila][col] == barco.mostrar_barco() or m[fila][col+1] == barco.mostrar_barco() or m[fila][col+2] == barco.mostrar_barco() or m[fila-1][col] == barco.mostrar_barco() or m[fila-1][col+1] == barco.mostrar_barco() or m[fila-1][col+2] == barco.mostrar_barco() or m[fila][col+3] == barco.mostrar_barco()):
                    fila = 9
                    col = randint(1,len(m))-1
                    
                    while (col == 9 or col == 0):
                        fila = randint(1,len(m))-1
                        col = randint(1,len(m))-1
                        
                m[fila][col] = barco.mostrar_barco()
                m[fila][col+1] = barco.mostrar_barco()
                m[fila][col+2] = barco.mostrar_barco()

        else:
            if col+2 == len(m)-1:

                while (col+3>len(m)) or (m[fila][col-1] == barco.mostrar_barco() or m[fila][col] == barco.mostrar_barco() or m[fila][col+1] == barco.mostrar_barco() or m[fila][col+2] == barco.mostrar_barco() or m[fila+1][col] == barco.mostrar_barco() or m[fila+1][col+1] == barco.mostrar_barco() or m[fila+1][col+2] == barco.mostrar_barco() or m[fila-1][col] == barco.mostrar_barco() or m[fila-1][col+1] == barco.mostrar_barco() or m[fila-1][col+2] == barco.mostrar_barco()):
                
                    fila = randint(1,len(m))-1
                    col = randint(1,len(m))-1
                    
                    while (fila == 0 or fila == 9 or col == 9 or col == 0):
                        fila = randint(1,len(m))-1
                        col = randint(1,len(m))-1
                        
                m[fila][col] = barco.mostrar_barco()
                m[fila][col+1] = barco.mostrar_barco()
                m[fila][col+2] = barco.mostrar_barco()


            else:
                while (col+4>len(m)) or (m[fila][col-1] == barco.mostrar_barco() or m[fila][col] == barco.mostrar_barco() or m[fila][col+1] == barco.mostrar_barco() or m[fila][col+2] == barco.mostrar_barco() or m[fila+1][col] == barco.mostrar_barco() or m[fila+1][col+1] == barco.mostrar_barco() or m[fila+1][col+2] == barco.mostrar_barco() or m[fila-1][col] == barco.mostrar_barco() or m[fila-1][col+1] == barco.mostrar_barco() or m[fila-1][col+2] == barco.mostrar_barco() or m[fila][col+3] == barco.mostrar_barco()):
                    
                    fila = randint(1,len(m))-1
                    col = randint(1,len(m))-1
                    
                    while (fila == 0 or fila == 9 or col == 9 or col == 0):
                        fila = randint(1,len(m))-1
                        col = randint(1,len(m))-1
                        print("--8.4--")
                    
                m[fila][col] = barco.mostrar_barco()
                m[fila][col+1] = barco.mostrar_barco()
                m[fila][col+2] = barco.mostrar_barco()

    elif fila == 0:
        while (col+3>len(m)) or (m[fila][col] == barco.mostrar_barco() or m[fila][col+1] == barco.mostrar_barco() or m[fila][col+2] == barco.mostrar_barco() or m[fila+1][col] == barco.mostrar_barco() or m[fila+1][col+1] == barco.mostrar_barco() or m[fila+1][col+2] == barco.mostrar_barco()):
            fila = randint(1,len(m))-1
            col = randint(1,len(m))-1
            
        m[fila][col] = barco.mostrar_barco()
        m[fila][col+1] = barco.mostrar_barco()
        m[fila][col+2] = barco.mostrar_barco()
            
    elif fila == 9:
        while (col+3>len(m)) or (m[fila][col] == barco.mostrar_barco() or m[fila][col+1] == barco.mostrar_barco() or m[fila][col+2] == barco.mostrar_barco() or m[fila-1][col] == barco.mostrar_barco() or m[fila-1][col+1] == barco.mostrar_barco() or m[fila-1][col+2] == barco.mostrar_barco()):
            fila = randint(1,len(m))-1
            col = randint(1,len(m))-1
            
        m[fila][col] = barco.mostrar_barco()
        m[fila][col+1] = barco.mostrar_barco()
        m[fila][col+2] = barco.mostrar_barco()
    else:
        while (col != 0 or col == 9 or fila == 9 or fila == 0) or(col+4>len(m)) or (m[fila][col] == barco.mostrar_barco() or m[fila][col-1] == barco.mostrar_barco() or m[fila][col+1] == barco.mostrar_barco() or m[fila][col+2] == barco.mostrar_barco() or m[fila-1][col] == barco.mostrar_barco() or m[fila-1][col+1] == barco.mostrar_barco() or m[fila-1][col+2] == barco.mostrar_barco() or m[fila+1][col] == barco.mostrar_barco() or m[fila+1][col+1] == barco.mostrar_barco() or m[fila+1][col+2] == barco.mostrar_barco() or m[fila][col+3] == barco.mostrar_barco()):
            fila = randint(1,len(m))-1
            col = randint(1,len(m))-1
            
        m[fila][col] = barco.mostrar_barco()
        m[fila][col+1] = barco.mostrar_barco()
        m[fila][col+2] = barco.mostrar_barco()