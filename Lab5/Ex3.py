class Vehicle:
    def __init__(self, make, model, year, fuel_level=0, fuel_efficiency=None, extra_max_distance=0):
        self._make = make
        self._model = model
        self._year = year
        self._fuel_level = fuel_level
        self._fuel_efficiency = fuel_efficiency
        self._extra_max_distance = extra_max_distance

    def calculate_mileage(self, distance):
        if not isinstance(distance, (float, int)) or distance <= 0:
            raise ValueError("Distanta trebuie sa fie un numar pozitiv!")
        if self._fuel_efficiency == 0:
            raise ValueError("Eficienta combustibilului trebuie sa fie mai mare de 0!")
        return distance / self._fuel_efficiency

    def refuel(self, amount):
        if amount <= 0:
            raise ValueError("Cantitatea trebuie sa fie un numar pozitiv.")
        self._fuel_level += amount

    def calculate_max_distance(self):
        if self._fuel_efficiency is None or self._fuel_efficiency == 0:
            raise ValueError("Eficiența combustibilului trebuie să fie un număr pozitiv diferit de zero!")
        return (self._fuel_efficiency * self._fuel_level) + self._extra_max_distance

    def get_info(self):
        return self._year, self._make, self._model, self._fuel_level, self._fuel_efficiency, self._extra_max_distance

    def __str__(self):
        return (f"An: {self.get_info()[0]}\n"
                f"Marca: {self.get_info()[1]}\n"
                f"Model: {self.get_info()[2]}\n"
                f"Nivel combustibil: {self.get_info()[3]}l\n"
                f"Eficienta consum: {self.get_info()[4]}l/100km\n"
                f"Distanta max suplimentara: {self.get_info()[5]}km")


class Car(Vehicle):
    def __init__(self, make, model, year, fuel_level, fuel_efficiency):
        super().__init__(make, model, year, fuel_level, fuel_efficiency, extra_max_distance=10)


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, fuel_level, fuel_efficiency, num_cylinders):
        super().__init__(make, model, year, fuel_level, fuel_efficiency, extra_max_distance=5)
        self._num_cylinders = num_cylinders

    def get_num_cylinders(self):
        return self._num_cylinders


class Truck(Vehicle):
    def __init__(self, make, model, year, fuel_level, fuel_efficiency, towing_capacity):
        super().__init__(make, model, year, fuel_level, fuel_efficiency, extra_max_distance=15)
        self._towing_capacity = towing_capacity

    def get_towing_capacity(self):
        return self._towing_capacity


if __name__ == '__main__':
    print("\n--------------------")
    car = Car(make="Toyota", model="Camry", year=2022, fuel_level=15, fuel_efficiency=30)
    print(car.__str__())

    print("\n--------------------")
    motorcycle = Motorcycle(make="Honda", model="CBR600RR", year=2022, fuel_level=12, fuel_efficiency=25, num_cylinders=4)
    print(motorcycle.__str__())
    print(f"Numar cilindrii: {motorcycle.get_num_cylinders()}")

    print("\n--------------------")
    truck = Truck(make="Ford", model="F-150", year=2023, fuel_level=30, fuel_efficiency=15, towing_capacity=10000)
    print(truck.__str__())
    print(f"Capacitate remorcare: {truck.get_towing_capacity()} lire sterline")
