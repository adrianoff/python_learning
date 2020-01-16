from abc import ABC, abstractmethod

from objects import HardObjects, HardMap, MediumObjects, MediumMap, EasyObjects, EasyMap


class AbstractObjects(ABC):
    def __init__(self, objects):
        self.object = object

    def get_objects(self, map_obj):
        return self.object.get_objects(map_obj)


class AbstractMap(ABC):
    def __init__(self, map):
        self.map = map

    def get_map(self):
        return self.map.get_map()


class HardObjectsAdapter(AbstractObjects):
    def __init__(self):
        super().__init__(HardObjects())


class HardMapAdapter(AbstractMap):
    def __init__(self):
        super().__init__(HardMap())


class MediumObjectsAdapter(AbstractObjects):
    def __init__(self):
        super().__init__(MediumObjects())


class MediumMapAdapter(AbstractMap):
    def __init__(self):
        super().__init__(MediumMap())


class EasyObjectsAdapter(AbstractObjects):
    def __init__(self):
        super().__init__(EasyObjects())


class EasyMapAdapter(AbstractMap):
    def __init__(self):
        super().__init__(EasyMap())