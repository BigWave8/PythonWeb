from abc import ABC, abstractmethod


class AbstractParent(ABC):
    @abstractmethod
    def hello_friend(self):
        raise NotImplementedError


class Father(AbstractParent, ABC):

    def __init__(self):
        print("Father constructor!")

    def play_guitar(self):
        print("father is play guitar")

    def do_hourse_work(self):
        print("sitting on the sofa and drink beer")


class Mother:
    def __init__(self, age=0):
        self.age = age
        print("Mother constructor!")

    def do_work(self):
        print("I'm working")

    def do_hourse_work(self):
        print("listening music")

    def say(self):
        print("go do homework!")


class Daughter(Mother, Father):
    def __init__(self, age=0):
        Mother.__init__(self, age=age)
        Father.__init__(self)

    def do_work(self):
        print("I'm working like a horse!")

    def hello_friend(self):
        pass


class Friend:
    pass


def greet_mother(mother: Mother):
    print("Hello mother!")
    mother.do_work()


def greet_father(father: Father):
    print("time to beer!")
    father.play_guitar()


if __name__ == "main":
    daughter = Daughter()
    greet_mother(daughter)
    greet_father(daughter)
    daughter.hello_friend()
    daughter.do_hourse_work()

    for x in [daughter]:
        x.do_hourse_work()

    # list
    povtorka_list = ["mathan_2", "programming_5", "superprise"]

    # tuple
    vasian = ("11 years", 12, 3.14, daughter)

    # set
    my_set = {23, 11, 10, 10, "call"}
    print(my_set)

    # frozen set
    another_set = frozenset(["di_", "mi", "do"])

    # dictionary
    my_dict = {1: "first", "2": 123, (1, 2, 3): "tuple_as_a_key"}
