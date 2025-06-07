from abc import ABC,abstractmethod

class Handler(ABC):
    @abstractmethod
    def setNext():
        pass

    @abstractmethod
    def handle():
        pass

class BaseHandler(Handler):
    nextHandler=None

    def setNext(self,handler):
        self.nextHandler=handler
        return handler

    def handle(self,params):
        if self.nextHandler:
            return self.nextHandler.handle(params)
        return None

        