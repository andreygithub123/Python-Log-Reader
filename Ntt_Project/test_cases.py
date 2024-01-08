import unittest
import exercicesImpl
import readFromFile

class TestExercices(unittest.TestCase):

    #test for the ex1
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
##############################################################################################################

# test for the ex4
    def test_most_errors(self):
        dict = exercicesImpl.ex4(readFromFile.extractData(readFromFile.readFile("../data/logs.txt")))
        #self.assertEqual(dict.get("ERROR").get("System"), 2)
        most_failed_app, num_failures = dict
        self.assertEqual(most_failed_app, "System")
        self.assertEqual(num_failures, 2)

# test for the ex5
    def test_most_succesful_runs(self):
        dict = exercicesImpl.ex5(readFromFile.extractData(readFromFile.readFile("../data/logs.txt")))
        most_successful_runs_app, num_successful_runs = dict
        self.assertEqual(most_successful_runs_app, "BackendApp")
        self.assertEqual(num_successful_runs, 2)


# test for the ex 6
    def test_failed_runs_time_interval(self):
         result = exercicesImpl.ex6(readFromFile.extractData(readFromFile.readFile("../data/logs.txt")))
         self.assertEqual(result, 3)  # Assuming 08:00:00-15:59:59 has the most failed runs


if __name__ == '__main__':
    unittest.main()