from creacionales.abstract_factory.ejemplo_abstract_factory import EjemploAbstractFactory
from creacionales.singleton.ejemplo_singleton import EjemploSingleton
from creacionales.prototype.ejemplo_prototype import EjemploPrototype
from estructurales.adapter.ejemplo_adapter import EjemploAdapter
from estructurales.bridge.ejemplo_bridge import EjemploBridge
from estructurales.Composite.ejemplo_composite import EjemploComposite
from estructurales.decorator.ejemplo_decorator import EjemploDecorator
from estructurales.proxy.ejemplo_proxy import EjemploProxy
from estructurales.fachada.ejemplo_fachada import EjemploFachada
from estructurales.flyweight.ejemplo_flyweight import EjemploFlyweight
from comportamiento.chain_of_resposability.ejemplo_cadena import EjemploCadena
from comportamiento.command.ejemplo_command import EjemploCommand
from comportamiento.interpreter.ejemplo_interpreter import EjemploInterpreter

class Handler:
    def __init__(self):
        self.__succesor__ = None

    def set_succesor(self, succesor):
        self.__succesor__ = succesor

    def handler_request(self, opt):
        pass


class HandlerOptionSingleton(Handler):

    def get_nombre(self):
        return EjemploSingleton().obtener_nombre()

    def handler_request(self, opt):
        if opt == 0:
            EjemploSingleton().operacion()
        else:
            self.__succesor__.handler_request(opt)

class HandlerOptionAbstractFactory(Handler):

    def get_nombre(self):
        return EjemploAbstractFactory().obtener_nombre()

    def handler_request(self, opt):
        if opt == 1:
            EjemploAbstractFactory().operacion()
        else:
            self.__succesor__.handler_request(opt)

class HandlerOptionPrototype(Handler):

    def get_nombre(self):
        return EjemploPrototype().obtener_nombre()

    def handler_request(self, opt):
        if opt == 2:
            EjemploPrototype().operacion()
        else:
            self.__succesor__.handler_request(opt)

class HandlerOptionAdapter(Handler):

    def get_nombre(self):
        return EjemploAdapter().obtener_nombre()

    def handler_request(self, opt):
        if opt == 3:
            EjemploAdapter().operacion()
        else:
            self.__succesor__.handler_request(opt)

class HandlerOptionBridge(Handler):

    def get_nombre(self):
        return EjemploBridge().obtener_nombre()

    def handler_request(self, opt):
        if opt == 4:
            EjemploBridge().operacion()
        else:
            self.__succesor__.handler_request(opt)

class HandlerOptionComposite(Handler):

    def get_nombre(self):
        return EjemploComposite().obtener_nombre()

    def handler_request(self, opt):
        if opt == 5:
            EjemploComposite().operacion()
        else:
            self.__succesor__.handler_request(opt)

class HandlerOptionDecorator(Handler):

    def get_nombre(self):
        return EjemploDecorator().obtener_nombre()

    def handler_request(self, opt):
        if opt == 6:
            EjemploDecorator().operacion()
        else:
            self.__succesor__.handler_request(opt)

class HandlerOptionProxy(Handler):

    def get_nombre(self):
        return EjemploProxy().obtener_nombre()

    def handler_request(self, opt):
        if opt == 7:
            EjemploProxy().operacion()
        else:
            self.__succesor__.handler_request(opt)

class HandlerOptionFachada(Handler):

    def get_nombre(self):
        return EjemploFachada().obtener_nombre()

    def handler_request(self, opt):
        if opt == 8:
            EjemploFachada().operacion()
        else:
            self.__succesor__.handler_request(opt)

class HandlerOptionFlyweight(Handler):

    def get_nombre(self):
        return EjemploFlyweight().obtener_nombre()

    def handler_request(self, opt):
        if opt == 9:
            EjemploFlyweight().operacion()
        else:
            self.__succesor__.handler_request(opt)

class HandlerOptionCadena(Handler):

    def get_nombre(self):
        return EjemploCadena().obtener_nombre()

    def handler_request(self, opt):
        if opt == 10:
            EjemploCadena().operacion()
        else:
            self.__succesor__.handler_request(opt)

class HandlerOptionCommand(Handler):

    def get_nombre(self):
        return EjemploCommand().obtener_nombre()

    def handler_request(self, opt):
        if opt == 11:
            EjemploCommand().operacion()
        else:
            self.__succesor__.handler_request(opt)

class HandlerOptionInterpreter(Handler):

    def get_nombre(self):
        return EjemploInterpreter().obtener_nombre()

    def handler_request(self, opt):
        if opt == 12:
            EjemploInterpreter().operacion()
        else:
            self.__succesor__.handler_request(opt)

class HandlerOptionDefault(Handler):

    def handler_request(self, opt):
        print("Opción no valida")