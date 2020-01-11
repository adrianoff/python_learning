class Hero:
    def __init__(self):
        self.positive_effects = []
        self.negative_effects = []
        self.stats = {
            "HP": 128,  # health points
            "MP": 42,  # magic points,
            "SP": 100,  # skill points
            "Strength": 15,  # сила
            "Perception": 4,  # восприятие
            "Endurance": 8,  # выносливость
            "Charisma": 2,  # харизма
            "Intelligence": 3,  # интеллект
            "Agility": 8,  # ловкость
            "Luck": 1  # удача
        }

    def get_positive_effects(self):
        return self.positive_effects.copy()

    def get_negative_effects(self):
        return self.negative_effects.copy()

    def get_stats(self):
        return self.stats.copy()


class AbstractEffect(Hero):

    def __init__(self, hero):
        super().__init__()
        self.hero = hero

    def get_positive_effects(self):
        return self.hero.get_positive_effects()

    def get_negative_effects(self):
        return self.negative_effects.copy()

    def get_stats(self):
        return self.stats.copy()


class Berserk(AbstractEffect):

    def __init__(self, hero):
        super().__init__(hero)

    def get_stats(self):
        stats = self.hero.get_stats()
        pos_effect_increase = 7
        stats['Strength'] = stats['Strength'] + pos_effect_increase
        stats['Endurance'] = stats['Endurance'] + pos_effect_increase
        stats['Agility'] = stats['Agility'] + pos_effect_increase
        stats['Luck'] = stats['Luck'] + pos_effect_increase

        stats['HP'] = stats['HP'] + 50

        pos_effect_decrease = 3
        stats['Perception'] = stats['Perception'] - pos_effect_decrease
        stats['Charisma'] = stats['Charisma'] - pos_effect_decrease
        stats['Intelligence'] = stats['Intelligence'] - pos_effect_decrease

        return stats

    def get_positive_effects(self):
        positive_effects = self.hero.get_positive_effects()
        positive_effects.append('Berserk')

        return positive_effects


class Blessing(AbstractEffect):
    def __init__(self, hero):
        super().__init__(hero)

    def get_stats(self):
        stats = self.hero.get_stats()
        stats = {key: stats[key] + 2 for key in stats}

        return stats

    def get_positive_effects(self):
        positive_effects = self.hero.get_positive_effects()
        positive_effects.append('Blessing')

        return positive_effects


hero1 = Hero()
berserk1 = Berserk(hero1)
print(berserk1.get_positive_effects())
print(berserk1.get_stats())

berserk2 = Berserk(berserk1)
print(berserk2.get_positive_effects())
print(berserk2.get_stats())

blessing1 = Blessing(berserk2)
print(blessing1.get_positive_effects())
print(blessing1.get_stats())

blessing1.hero = berserk1
print(blessing1.get_positive_effects())
print(blessing1.get_stats())
