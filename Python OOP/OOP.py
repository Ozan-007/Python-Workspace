class Car:
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color

    def start(self):
        print(f"{self.color} {self.model} has started.")

    def stop(self):
        print(f"{self.color} {self.model} has stopped.")


car1 = Car("Mustang", "2020", "Red")
Cars = [Car("Mustang", "2020", "Red"), Car("Ferrari", "2019", "Black")]
# print(Cars[0])
# car1.start()
