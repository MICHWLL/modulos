'''creemos un modulo llamado calculadora con las siguientes funciones '''
def Sumar (N1,N2,N3=0):
    return N1+N2+N3;

def restar(N1,N2):
    return N1-N2;

def multiplicar (N1,N2):
    return N1*N2;

def dividir(N1,N2):
    if(N1 or N2 == 0):
        print ("operacion invalida");
      
