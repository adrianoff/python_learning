class Singleton:
    instance = None

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super(Singleton, cls).__new__(cls, *args, **kwargs)

        return cls.instance


obj = Singleton()
