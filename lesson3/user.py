class User:

    def __init__(self, first_name, last_name):
        self.name = first_name
        self.surname = last_name

    def sayName(self):
        print("Имя: ", self.name)

    def saySurname(self):
        print("Фамилия: ", self.surname)

    def nameAndSurname(self):
        print("Имя и Фамилия: ", self.name, self.surname)
