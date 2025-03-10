# A component which is instantiated only once.

def singleton(class_):
    """Decorator that ensures a class be instantiated only one."""
    instances = {}
    def get_instances(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return get_instances


def is_singleton(class_name):
    """Method that checks whether class is singleton."""
    obj1 = class_name()
    obj2 = class_name()
    return obj1 is obj2


@singleton
class MainDatabase:
    def __init__(self, user, password, port):
        self.user = user
        self.password = password
        self.port = port
        print("Loading database...")

    def __str__(self):
        return f"Username: {self.user}, password: {self.password}, port: {self.port}"


class SomeDatabase:
    def __init__(self, user, password, port):
        self.user = user
        self.password = password
        self.port = port
        print("Loading database...")

    def __str__(self):
        return f"Username: {self.user}, password: {self.password}, port: {self.port}"


if __name__ == '__main__':
    mdb1 = MainDatabase("admin", "admin", 5000)
    print("mdb1: ", mdb1)
    mdb2 = MainDatabase("admin", "password", 5010)
    print("mdb2: ", mdb2)
    print("Does mdb1 equal mdb2: ", mdb2 == mdb2)
    print("mdb1 is mdb2: ", mdb2 is mdb2)
    print("---------------------")
    sdb1 = SomeDatabase("admin", "admin", 5000)
    print("sdb1: ", sdb1)
    sdb2 = SomeDatabase("admin", "password", 5010)
    print("sdb2: ", sdb2)
    print("Does sdb1 equal sdd2: ", sdb1 == sdb2)
    print("sdb1 is sdb2: ", sdb1 is sdb2)
    print("---------------------")
    print("Is MainDatabase singleton:")
    print(is_singleton(lambda: MainDatabase("admin", "admin", 5000)))
    print("Is SomeDatabase singleton:")
    print(is_singleton(lambda : SomeDatabase("admin", "admin", 5000)))