# Слушатель курса Junior Python-разработчик
# Рыжаков Андрей Николаевич, anryzhakov@yandex.ru
# Домашнее задание по теме "Простые Юнит-Тесты"

import unittest

from Module_12.classRunner import Runner


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


if __name__ == '__main__':
    unittest.main()
