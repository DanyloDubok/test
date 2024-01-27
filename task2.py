class Cat:
    def __init__(self, has_breed=False, name=None):
        self.has_breed = has_breed
        self.name = name

class WildCat(Cat):
    def __init__(self, has_breed=False):
        # Викликаємо конструктор батьківського класу
        super().__init__(has_breed)

    def adopt(self):
        # Створюємо новий екземпляр класу DomesticCat при "удомашненні" дикого кота
        return DomesticCat(has_breed=self.has_breed)

class DomesticCat(Cat):
    def __init__(self, has_breed=False, name=None):
        # Викликаємо конструктор батьківського класу
        super().__init__(has_breed, name)
        # Якщо ім'я відсутнє, генеруємо виключення
        if name is None:
            raise ValueError("A DomesticCat must have a name.")

# Приклад використання
wild_cat = WildCat(has_breed=True)
print(wild_cat.has_breed)  # False
print(wild_cat.name)  # None

domestic_cat = wild_cat.adopt()
print(domestic_cat.has_breed)  # False (спадковано від WildCat)
print(domestic_cat.name)  # Raises ValueError (ім'я обов'язкове для DomesticCat)
