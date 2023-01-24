import os

class operacionesBas:

    def __init__(self, a, b):
        self.num1=a
        self.num2=b

    def suma(self):
        #num1=12
        #num2=10
        self.res=self.num1+self.num2
        print("La suma es: {}".format(self.res))

    def resta(self):
        self.res=self.num1-self.num2
        print("La resta es: {}".format(self.res))

    def multiplicacion(self):
        self.res=self.num1*self.num2
        print("la multiplicacion es: {}".format(self.res))

    def divicion(self):
        self.res=self.num1/self.num2
        print("la divicion es: {}".format(self.res))
    
    def salir():
        print('Saliendo...')


def main():
    opciones=0
    
    while True:  
    
        print('''
        'Opción 1',
        'Opción 2,
        'Opción 3',
        'Opción 4',
        'opcion 5' ''')
        opciones=int(input("Elige la opcion"))
        obj=operacionesBas(10,5)

        if opciones==1:
            obj.suma()
        elif opciones==2:
            obj.resta()
        elif  opciones==3:
            obj.multiplicacion()
        elif opciones==4:
            obj.divicion()
        elif opciones==5:
            obj.salir()
            break

if __name__ == "__main__":
    main()
