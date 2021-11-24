from unittest import TestCase, main

from project.hero import Hero

class TestHero(TestCase):
    def setUp(self):
        self.hero = Hero('Joe', 10, 100, 20)
        self.enemy = Hero('Bob', 5, 210, 10)
        self.enemy_zero = Hero('Bob', 5, 200, 10)
        self.hero_zero = Hero('Max', 10, 50, 20)

    def test_init_creates_all_attributes(self):
        self.assertEqual('Joe', self.hero.username)
        self.assertEqual(10, self.hero.level)
        self.assertEqual(100, self.hero.health)
        self.assertEqual(20, self.hero.damage)

    def test_cannot_fight_yourself_same_username(self):
        second_hero = Hero('Joe', 20, 20, 10)
        with self.assertRaises(Exception) as ex:
            self.hero.battle(second_hero)
        self.assertEqual('You cannot fight yourself', str(ex.exception))

    def test_when_health_is_zero_or_negative(self):
        enemy = Hero('Bob', 10, 100, 200)
        self.hero.battle(enemy)
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(enemy)
        self.assertEqual('Your health is lower than or equal to 0. You need to rest', str(ex.exception))

    def test_when_enemy_health_is_zero_or_negative(self):
        enemy = Hero('Bob', 1, 1, 2)
        self.hero.battle(enemy)
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(enemy)
        self.assertEqual('You cannot fight Bob. He needs to rest', str(ex.exception))

    def test_player_health(self):
        self.hero.battle(self.enemy)
        self.assertEqual(50, self.hero.health)
        self.assertEqual(15, self.enemy.health)

    def test_if_hero_zero_or_bellow_and_enemy_zero_or_bellow(self):
        res = self.hero_zero.battle(self.enemy_zero)
        self.assertEqual('Draw', res)

    def test_hero_win(self):
        res = self.hero.battle(self.enemy_zero)
        self.assertEqual('You win', res)
        self.assertEqual(11, self.hero.level)
        self.assertEqual(55, self.hero.health)
        self.assertEqual(25, self.hero.damage)

    def test_enemy_win(self):
        res = self.hero.battle(self.enemy)
        self.assertEqual('You lose', res)

    def test_str_(self):
        self.assertEqual("Hero Joe: 10 lvl\n" \
               "Health: 100\n" \
               "Damage: 20\n", self.hero.__str__())

if __name__ == '__main__':
    main()