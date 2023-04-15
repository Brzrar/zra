from enum import Enum
from random import randint, choice


class SuperAbility(Enum):
    CRITICAL_DAMAGE = 1
    HEAL = 2
    BOOST = 3
    SAVE_DAMAGE_AND_REVERT = 4
    REVIVE = 5
    STUN = 6


class GameEntity:
    def __init__(self, name, health, damage):
        self.__name = name
        self.__health = health
        self.__damage = damage

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value < 0:
            self.__health = 0
        else:
            self.__health = value

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value

    def __str__(self):
        return f'{self.__name} health: {self.__health} damage: {self.__damage}'



class Boss(GameEntity):
    def __init__(self, name, health, damage):
        super(Boss, self).__init__(name, health, damage)
        self.__defence = None

    @property
    def defence(self):
        return self.__defence

    def choose_defence(self, heroes):
        chosen_hero = choice(heroes)
        self.__defence = chosen_hero.ability

    def attack(self, heroes):
        for hero in heroes:
            if hero.health > 0:
                hero.health -= self.damage

    def __str__(self):
        return 'BOSS ' + super(Boss, self).__str__() + f' defence: {self.defence}'



class Hero(GameEntity):
    def __init__(self, name, health, damage, ability):
        super(Hero, self).__init__(name, health, damage)
        if not isinstance(ability, SuperAbility):
            raise ValueError('Value for attribute ability must be of type SuperAbility')
        else:
            self.__ability = ability

    @property
    def ability(self):
        return self.__ability

    def attack(self, boss):
        if boss.health > 0:
            boss.health -= self.damage

    def apply_super_power(self, boss, heroes):
        pass



class Warrior(Hero):
    def __init__(self, name, health, damage):
        super(Warrior, self).__init__(name, health, damage, SuperAbility.CRITICAL_DAMAGE)

    def apply_super_power(self, boss, heroes):
        coefficient = randint(2, 5)
        boss.health -= self.damage * coefficient
        print(f'Warrior hits critically: {self.damage * coefficient}')


class Magic(Hero):
    def __init__(self, name, health, damage, boost_points):
        super(Magic, self).__init__(name, health, damage, SuperAbility.BOOST)
        self.__boost_points = boost_points

    def apply_super_power(self, boss, heroes):
        for hero in heroes:
            if hero.health > 0 and self != hero:
                hero.damage += self.__boost_points
        print(f'{self.name} boost heroes {self.__boost_points}')


class Medic(Hero):
    def __init__(self, name, health, damage, heal_points):
        super(Medic, self).__init__(name, health, damage, SuperAbility.HEAL)
        self.__heal_points = heal_points

    def apply_super_power(self, boss, heroes):
        for hero in heroes:
            if hero.health > 0 and self != hero:
                hero.health += self.__heal_points


class Berserk(Hero):
    def __init__(self, name, health, damage):
        Hero.__init__(self, name, health, damage, SuperAbility.SAVE_DAMAGE_AND_REVERT)
        self.__saved_damage = 0

    @property
    def saved_damage(self):
        return self.__saved_damage

    @saved_damage.setter
    def saved_damage(self, value):
        self.__saved_damage = value

    def apply_super_ability(self, boss):
        if boss.health > 0:
            reverted_damage = self.saved_damage // randint(1, 6)
            boss.health = max(0, boss.health - reverted_damage)
            print(f'Berserk {self.name} attack boss {reverted_damage}')
            self.saved_damage = 0


class Witcher(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.REVIVE)

    def apply_super_ability(self, heroes):
        for hero in heroes:
            if hero.health <= 0:
                hero.health = self.health
                self.health = 0
                print(f'{self.name} revived {hero.name}')
                break


class Thor(Hero):
    def __init__(self, name, health, damage):
        Hero.__init__(self, name, health, damage, SuperAbility.STUN)
        self.__stun = 0

    def apply_super_ability(self, boss):
        chance_to_stun_boss = randint(1, 5)
        if chance_to_stun_boss == 3:
            boss.damage = 0
            print(f'{self.name} stunned BOSS')
        else:
            boss.damage = 50


round_number = 0


def is_game_finished(boss, heroes):
    if boss.health <= 0:
        print('Heroes won!!!')
        return True
    all_heroes_dead = True
    for hero in heroes:
        if hero.health > 0:
            all_heroes_dead = False
            break
    if all_heroes_dead:
        print('Boss won!!!')
    return all_heroes_dead


def print_statistics(boss, heroes):
    print(f'ROUND {round_number} --------------')
    print(boss)
    for hero in heroes:
        print(hero)



def play_round(boss, heroes):
    global round_number
    round_number += 1
    boss.choose_defence(heroes)
    boss.attack(heroes)
    for hero in heroes:
        if boss.defence != hero.ability and hero.health > 0:
            hero.attack(boss)
            hero.apply_super_power(boss, heroes)
    print_statistics(boss, heroes)



def start_game():
    boss = Boss("Dabi", 1000, 50)
    warrior = Warrior("Zaki", 270, 10)
    doc = Medic("Flora", 255, 5, 15)
    magic = Magic("Mag", 260, 20, randint(10, 20))
    berserk = Berserk("Halk", 280, 15)
    assistant = Medic("Megan", 295, 10, 5)
    witcher = Witcher('Geralt', 360, 0)
    thor = Thor('Thor', 285, 16)
    heroes_list = [warrior, doc, magic, berserk, assistant, witcher, thor]

    print_statistics(boss, heroes_list)
    while not is_game_finished(boss, heroes_list):
        play_round(boss, heroes_list)


start_game()

