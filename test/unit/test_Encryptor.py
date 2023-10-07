import unittest


from encrypt_sp.Encryptor import Encryptor


class TestEncryptor(unittest.TestCase):

    def test_file(self):
        with open("test.txt", "w") as file:
            file.write("test")

        Encryptor("test.txt")

        with open("test.txt", "r") as file:
            self.assertEqual(file.read(), "grfg")