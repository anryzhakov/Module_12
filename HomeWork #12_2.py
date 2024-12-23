# Слушатель курса Junior Python-разработчик
# Рыжаков Андрей Николаевич, anryzhakov@yandex.ru
# Домашнее задание по теме "Методы Юнит-тестирования"

import unittest

from Module_12.runner_and_tournament import Runner, Tournament


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        obj = Runner('Тест №1')
        for _ in range(10):
            obj.walk()
        self.assertEqual(obj.distance, 50)

    def test_run(self):
        obj = Runner('Тест №2')
        for _ in range(10):
            obj.run()
        self.assertEqual(obj.distance, 100)

    def test_challenge(self):
        obj_1 = Runner('Тест №3.1')
        obj_2 = Runner('Тест №3.2')
        for _ in range(10):
            obj_1.walk()
            obj_2.run()
        self.assertNotEqual(obj_1.distance, obj_2.distance)


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner(name="Усэйн", speed=10)
        self.andrew = Runner(name="Андрей", speed=9)
        self.nik = Runner(name="Ник", speed=3)

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print(f"{key}: {value}")

    def test_race_1(self):
        participants = [self.usain, self.nik]
        race = Tournament(90, *participants)
        results = race.start()
        self.all_results.update(results)
        self.assertTrue(max(self.all_results) in results and results[max(self.all_results)] == "Ник")

    def test_race_2(self):
        participants = [self.andrew, self.nik]
        tournament = Tournament(90, *participants)
        results = tournament.start()
        self.all_results.update(results)
        self.assertTrue(max(self.all_results) in results and results[max(self.all_results)] == "Ник")

    def test_race_3(self):
        participants = [self.usain, self.andrew, self.nik]
        tournament = Tournament(90, *participants)
        results = tournament.start()
        self.all_results.update(results)
        self.assertTrue(max(self.all_results) in results and results[max(self.all_results)] == "Ник")


if __name__ == '__main__':
    unittest.main()
