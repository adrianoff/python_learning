from abc import ABC, abstractmethod

from objects_adapter import *


class AbstractFactory(ABC):

    @abstractmethod
    def create_map(self) -> AbstractMap:
        pass

    @abstractmethod
    def create_object(self) -> AbstractObjects:
        pass


class EasyFactory(AbstractFactory):
    def create_map(self):
        return EasyMapAdapter()

    def create_object(self):
        return EasyObjectsAdapter()


class MediumFactory(AbstractFactory):
    def create_map(self):
        return MediumMapAdapter()

    def create_object(self):
        return MediumObjectsAdapter()


class HardFactory(AbstractFactory):
    def create_map(self):
        return HardMapAdapter()

    def create_object(self):
        return HardObjectsAdapter()


def map_creator(factory: AbstractFactory) -> AbstractMap:
    return factory.create_map()


def objects_creator(factory: AbstractFactory) -> AbstractObjects:
    return factory.create_object()


easy_factory = EasyFactory()
easy_map = map_creator(easy_factory)
easy_objects = objects_creator(easy_factory)
