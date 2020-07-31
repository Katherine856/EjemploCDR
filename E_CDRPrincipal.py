from CDRPrincipal import *

class E_CDRPrincipal:
    def obtener_nombre(self):
        return "Menú"

    def operacion(self):
        patrones = [HandlerOptionSingleton(), HandlerOptionAbstractFactory(), HandlerOptionPrototype(),
                  HandlerOptionAdapter(),
                  HandlerOptionBridge(), HandlerOptionComposite(), HandlerOptionDecorator(), HandlerOptionProxy(),
                  HandlerOptionFachada(), HandlerOptionFlyweight(), HandlerOptionCadena(), HandlerOptionCommand(),
                  HandlerOptionInterpreter(), HandlerOptionDefault()]

        for i in range(len(patrones)-1):
            patrones[i].set_succesor(patrones[i+1])
            print(str(i) + "  --> " + patrones[i].get_nombre())

        opcion = int(input("ingrese una opcion: "))
        patrones[0].handler_request(opcion)

if __name__ == '__main__':
    Menu = E_CDRPrincipal()
    Menu.operacion()