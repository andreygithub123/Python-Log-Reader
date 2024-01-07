import unittest
import exercicesImpl
import readFromFile

class TestExercices(unittest.TestCase):

    def test_should_verify_the_number_of_info_API(self):
        dict = exercicesImpl.ex1(readFromFile.extractData(readFromFile.readFile("../data/logs.txt")))
        self.assertEqual(dict.get("INFO").get("API"), 1)

    def test_should_verify_the_number_of_error_API(self):
        dict = exercicesImpl.ex1(readFromFile.extractData(readFromFile.readFile("../data/logs.txt")))
        self.assertEqual(dict.get("ERROR").get("API"), 1)

    def test_should_verify_the_number_of_debug_API(self):
        dict = exercicesImpl.ex1(readFromFile.extractData(readFromFile.readFile("../data/logs.txt")))
        self.assertEqual(dict.get("DEBUG").get("API"), 1)

    def test_should_verify_the_number_of_info_BackendApp(self):
        dict = exercicesImpl.ex1(readFromFile.extractData(readFromFile.readFile("../data/logs.txt")))
        self.assertEqual(dict.get("INFO").get("Backend"), 1)

    def test_should_verify_the_number_of_error_BackendApp(self):
        dict = exercicesImpl.ex1(readFromFile.extractData(readFromFile.readFile("../data/logs.txt")))
        self.assertEqual(dict.get("ERROR").get("Backend"), 1)

    def test_should_verify_the_number_of_debug_BackendApp(self):
        dict = exercicesImpl.ex1(readFromFile.extractData(readFromFile.readFile("../data/logs.txt")))
        self.assertEqual(dict.get("DEBUG").get("Backend"), 1)

    def test_should_verify_the_number_of_info_FrontendApp(self):
        dict = exercicesImpl.ex1(readFromFile.extractData(readFromFile.readFile("../data/logs.txt")))
        self.assertEqual(dict.get("INFO").get("Frontend"), 1)

    def test_should_verify_the_number_of_error_FrontendApp(self):
        dict = exercicesImpl.ex1(readFromFile.extractData(readFromFile.readFile("../data/logs.txt")))
        self.assertEqual(dict.get("ERROR").get("Frontend"), 1)

    def test_should_verify_the_number_of_debug_FrontendApp(self):
        dict = exercicesImpl.ex1(readFromFile.extractData(readFromFile.readFile("../data/logs.txt")))
        self.assertEqual(dict.get("DEBUG").get("Frontend"), 1)

    def test_should_verify_the_number_of_info_SYSTEM(self):
        dict = exercicesImpl.ex1(readFromFile.extractData(readFromFile.readFile("../data/logs.txt")))
        self.assertEqual(dict.get("INFO").get("System"), 1)

    def test_should_verify_the_number_of_error_SYSTEM(self):
        dict = exercicesImpl.ex1(readFromFile.extractData(readFromFile.readFile("../data/logs.txt")))
        self.assertEqual(dict.get("ERROR").get("System"), 1)

    def test_should_verify_the_number_of_debug_SYSTEM(self):
        dict = exercicesImpl.ex1(readFromFile.extractData(readFromFile.readFile("../data/logs.txt")))
        self.assertEqual(dict.get("DEBUG").get("System"), 1)


if __name__ == '__main__':
    unittest.main()