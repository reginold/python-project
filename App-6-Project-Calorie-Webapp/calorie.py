from temperature import Temperature


class Calorie:
    def __init__(self, weight, height, age, temperature):
        self.weight = weight
        self.height = height
        self.age = age
        self.temperature = temperature

    def calulate(self):
        result = 10 * self.weight + 6.5 * self.height + 5 - self.temperature * 10
        return result


if __name__ == "__main__":
    temperature = Temperature(country="usa", city="san-francisco").scrap_temp()
    calorie = Calorie(weight=70, height=175, age=32, temperature=temperature)
    print(calorie.calulate())
