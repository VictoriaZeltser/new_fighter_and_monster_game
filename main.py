from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

class Sword(Weapon):
    def attack(self):
        return "Боец наносит удар мечем."

class Bow(Weapon):
    def attack(self):
        return "Выстрел из лука!"

class Fighter:
    def __init__(self, name, health, weapon: Weapon):
        self.name = name
        self.health = health
        self.weapon = weapon

    def changeWeapon(self, new_weapon: Weapon):
        self.weapon = new_weapon

    def attack(self, target):
        print(f"{self.weapon.attack()} {target.name} побежден!")


class Monster:
    def __init__(self, name, health):
        self.name = name
        self.health = health

# Создаем оружие
sword = Sword()
bow = Bow()

# Создаем бойца и монстра
fighter = Fighter("Боец", 100, sword)
monster = Monster("Монстр", 50)

# Бой мечом
fighter.attack(monster)

# Меняем оружие на лук
fighter.changeWeapon(bow)

# Бой луком
fighter.attack(monster)

