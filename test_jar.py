from jar import Jar
import unittest

class TestJar(unittest.TestCase):

    def test_init(self):
        jar = Jar()
        assert jar.capacity == 12
        assert jar.size == 0

    def test_str(self):
        jar = Jar()
        assert str(jar) == ""
        jar.deposit(1)
        assert str(jar) == "🍪"
        jar.deposit(11)
        assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

    def test_withdraw(self):
        jar = Jar()
        jar.deposit(1)
        jar.withdraw(1)
        assert jar.size == 0
        with self.assertRaises(ValueError):
            jar.withdraw(-12)
        with self.assertRaises(ValueError):
            jar.withdraw(5)

    def test_deposit(self):
        jar = Jar()
        jar.deposit(5)
        assert jar.size == 5
        with self.assertRaises(ValueError):
            jar.deposit(-12)
        with self.assertRaises(ValueError):
            jar.deposit(12)




