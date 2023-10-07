import unittest


from encrypt_sp.Decryptor import Decryptor


class TestDecryptor(unittest.TestCase):

    def test_file_overwrite(self):
        with open("test.txt", "w") as file:
            file.write("grfg")

        Decryptor("test.txt")

        with open("test.txt", "r") as file:
            self.assertEqual(file.read(), "test")