from abc import ABC, abstractmethod
from typing import Any, Optional


class AbstractBaseChainHandler(ABC):
    @abstractmethod
    def set_next(self, handler):
        pass

    @abstractmethod
    def handle(self, request, options):
        pass


class AbstractChainHandler(AbstractBaseChainHandler):

    _next_handler: AbstractBaseChainHandler = None

    def set_next(self, handler: AbstractBaseChainHandler) -> AbstractBaseChainHandler:
        self._next_handler = handler

        return self._next_handler

    def handle(self, request: Any, options):
        if self._next_handler:
            return self._next_handler.handle(request, options)

        return None


class CheckDataIsOK(AbstractChainHandler):
    def handle(self, request: Any, options):
        print('CheckDataIsOK')
        request.append(self.__class__.__name__)
        if self._next_handler:
            return self._next_handler.handle(request, options)


class CleanUpData(AbstractChainHandler):
    def handle(self, request: Any, options):
        print('CleanUpData')
        request.append(self.__class__.__name__)
        if self._next_handler:
            return self._next_handler.handle(request, options)


class ModifyData(AbstractChainHandler):
    def handle(self, request: Any, options):
        print('ModifyData')
        request.append(self.__class__.__name__)
        if self._next_handler:
            return self._next_handler.handle(request, options)

        return request


checkDataIsOK = CheckDataIsOK()
cleanUpData = CleanUpData()
modifyData = ModifyData()

checkDataIsOK.set_next(cleanUpData).set_next(modifyData)
request = checkDataIsOK.handle([], [])

print(request)