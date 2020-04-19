class Chainsaws:
    producer = "Ukraine"

    def __init__(self, name="Pylla", power_in_watts=800,
                 number_of_revolutions_of_chain_per_minute=5000,
                 price=100500, massInKilograms=3):
        self.name = name
        self.power_in_watts = power_in_watts
        self.number_of_revolutions_of_chain_per_minute = number_of_revolutions_of_chain_per_minute
        self.price = price
        self.massInKilograms = massInKilograms

    @staticmethod
    def staticmethod():
        return Chainsaws.producer

    def __str__(self):
        name = "Name: {}\n".format(self.name)
        power_in_watts = "Power in watts: {}\n".format(self.power_in_watts)
        number_of_revolutions_of_chain_per_minute = "Number of revolutions of chain per minute: {}\n".format(
            self.number_of_revolutions_of_chain_per_minute)
        price = "Price: {}\n".format(self.price)
        massInKilograms = "Mass in kg: {}\n".format(self.massInKilograms)
        producer = "Producer: {}\n".format(Chainsaws.producer)
        return name + power_in_watts + number_of_revolutions_of_chain_per_minute + price + massInKilograms + producer


    def __del__(self):
        print("End")

def main():
    first_chainsaw = Chainsaws()
    second_chainsaw = Chainsaws(price=123)
    third_chainsaw = Chainsaws(name="iSaw")
    print(first_chainsaw)
    print(second_chainsaw)
    print(third_chainsaw)


if __name__ == '__main__':
    main()
