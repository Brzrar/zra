class Computer:

    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    # getters
    @property
    def getCPU(self):
        return self.__cpu

    @property
    def getMemory(self):
        return self.__memory

    # setters
    @getCPU.setter
    def setCPU(self, cpu):
        self.__cpu = cpu

    @getMemory.setter
    def setCPU(self, memory):
        self.__memory = memory

    def make_computations(self):
        return self.__cpu * self.__memory

    def __cmp__(self):
        return self.__memory > self.__cpu

    def __gt__(self, other):
        return len(self) > len(other)

    def __lt__(self, other):
        return len(self) < len(other)

    def __ge__(self, other):
        return len(self) >= len(other)

    def __le__(self, other):
        return len(self) <= len(other)

    def __str__(self):
        return f"CPU: {self.__cpu} \nMemory: {self.__memory}"


class Phone:
    def __init__(self, sim_card_list):
        self.__sim_card_list = sim_card_list

    @property
    def getSIM(self):
        return self.__sim_card_list

    @getSIM.setter
    def setSIM(self, sim):
        self.__sim_card_list = sim

    def call(self, sim_card_number, call_to_number):
        print(f"Идет звонок на номер {call_to_number} с сим-карты-{sim_card_number}")

    def __str__(self):
        return f"SIM-Cards: {self.__sim_card_list}"


class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory):
        super().__init__(cpu, memory)

    def use_gps(self, location):
        print(f"Ваша геопозиция определена! На данный момент вы здесь: {location}")

    def __str__(self):
        return super().__str__()


comp = Computer(8, 256)
print(comp.__str__())
print(comp.make_computations())
phone = Phone(sim_card_list=[0, 1, 2, 3, 4, 5])
print(phone.__str__())
print(phone.call(1, +996555999000))
smartPhone1 = SmartPhone(8, 256)
print(smartPhone1.use_gps("vefa center"))
print(smartPhone1.__str__())
smartPhone2 = SmartPhone(8, 256)
