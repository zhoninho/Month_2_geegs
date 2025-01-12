class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value

    def make_computations(self):
        return self.__cpu * self.__memory

    def __str__(self):
        return f"Computer: CPU = {self.__cpu}, Memory = {self.__memory} GB"

    def __eq__(self, other):
        return self.__memory == other.__memory

    def __ne__(self, other):
        return self.__memory != other.__memory

    def __lt__(self, other):
        return self.__memory < other.__memory

    def __le__(self, other):
        return self.__memory <= other.__memory

    def __gt__(self, other):
        return self.__memory > other.__memory

    def __ge__(self, other):
        return self.__memory >= other.__memory

class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value

    def call(self, sim_card_number, call_to_number):
        try:
            sim_card = self.__sim_cards_list[sim_card_number - 1]
            print(f"Идет звонок на номер {call_to_number} с сим-карты-{sim_card_number} - {sim_card}")
        except:
            print("Неверный номер сим-карты")

    def __str__(self):
        return f"Телефон с сим-картами {self.__sim_cards_list}"

class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)

    def use_gps(self, location):
        print(f"Построение маршрута до {location}...")

    def __str__(self):
        return f"SmartPhone: CPU = {self.cpu}, Memory = {self.memory} GB, SIM cards = {self.sim_cards_list}"

# Создание объектов
computer = Computer(4, 16)
phone = Phone(["Beeline", "O!", "Megacom"])
smartphone1 = SmartPhone(8, 254, ["Beeline", "O!"])
smartphone2 = SmartPhone(6, 128, ["Megacom"])

# Вывод информации об объектах
print(computer)
print(phone)
print(smartphone1)
print(smartphone2)

# Опробование методов
print(f"Вычисления на компьютере: {computer.make_computations()}")
phone.call(1, "+996 777 99 88 11")
smartphone1.use_gps("ЦУМ")
smartphone2.use_gps("Ошский рынок")

# Магические методы
print(f"Сравнение памяти смартфонов (1 > 2): {smartphone1 > smartphone2}")
print(f"Сравнение памяти (компьютер < смартфон 2): {computer < smartphone2}")