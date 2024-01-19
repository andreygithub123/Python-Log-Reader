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

    #test for the ex2
    def test_should_verify_average_successful_time_for_frontend(self):
        vect = exercicesImpl.ex2(readFromFile.extractData(readFromFile.readFile("../data/logs.txt")))
        self.assertEqual(vect[0], 1)
        self.assertEqual(vect[1], 25.0)
    def test_should_verify_average_successful_time_for_backend(self):
        vect = exercicesImpl.ex2(readFromFile.extractData(readFromFile.readFile("../data/logs.txt")))
        self.assertEqual(vect[2], 2)
        self.assertEqual(vect[3], 16.0)
    def test_should_verify_average_successful_time_for_api(self):
        vect = exercicesImpl.ex2(readFromFile.extractData(readFromFile.readFile("../data/logs.txt")))
        self.assertEqual(vect[4], 1)
        self.assertEqual(vect[5], 20.0)

##############################################################################################################
    #test for the ex3
    def test_should_verify_the_number_of_failed_runs_for_frontend(self):
        a = exercicesImpl.ex3(readFromFile.extractData(readFromFile.readFile("../data/logs.txt")))
        self.assertEqual(a[0], 1)
    def test_should_verify_the_number_of_failed_runs_for_backend(self):
        a = exercicesImpl.ex3(readFromFile.extractData(readFromFile.readFile("../data/logs.txt")))
        self.assertEqual(a[1], 1)

    def test_should_verify_the_number_of_failed_runs_for_api(self):
        a = exercicesImpl.ex3(readFromFile.extractData(readFromFile.readFile("../data/logs.txt")))
        self.assertEqual(a[2], 1)

    def test_should_verify_the_number_of_failed_runs_for_system(self):
        a = exercicesImpl.ex3(readFromFile.extractData(readFromFile.readFile("../data/logs.txt")))
        self.assertEqual(a[3], 2)

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

#Edge Case 1: Empty Log File
def test_empty_log_file(self):
    dict = exercicesImpl.ex1([])
    self.assertEqual(dict, {"INFO": {"API": 0, "Frontend": 0, "Backend": 0, "System": 0},
                            "DEBUG": {"API": 0, "Frontend": 0, "Backend": 0, "System": 0},
                            "ERROR": {"API": 0, "Frontend": 0, "Backend": 0, "System": 0}})

def test_empty_log_file_ex2(self):
    vect = exercicesImpl.ex2([])
    self.assertEqual(vect, (0, 0, 0, 0, 0, 0))

def test_empty_log_file_ex3(self):
    a = exercicesImpl.ex3([])
    self.assertEqual(a, (0, 0, 0, 0))

def test_empty_log_file_ex4(self):
    dict = exercicesImpl.ex4([])
    self.assertEqual(dict, ("", 0))

def test_empty_log_file_ex5(self):
    dict = exercicesImpl.ex5([])
    self.assertEqual(dict, ("", 0))

def test_empty_log_file_ex6(self):
    result = exercicesImpl.ex6([])
    self.assertEqual(result, 0)

def test_empty_log_file_ex7(self):
    result = exercicesImpl.ex7([])
    self.assertEqual(result, ([], [], [], [], [], []))

def test_empty_log_file_ex8(self):
    result = exercicesImpl.ex8([])
    self.assertEqual(result, {"API": "", "Backend": "", "Frontend": ""})

def test_empty_log_file_ex9(self):
    result = exercicesImpl.ex9([])
    self.assertEqual(result, {"Frontend": 0.0, "Backend": 0.0, "API": 0.0, "System": 0.0})


if __name__ == '__main__':
    unittest.main()