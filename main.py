import Ntt_Project.readFromFile
from Ntt_Project.LogOperations import logOperations


# lines = Ntt_Project.readFromFile.readFile("data/output.txt")
# logs = Ntt_Project.readFromFile.extractData(lines)
# longlogs = len(logs)
# print(logs)

a = logOperations.ex1("data/output.txt")
# a = logOperations.ex2("data/output.txt")
# a = logOperations.ex3("data/output.txt")
# a = logOperations.ex4("data/output.txt")
# a = logOperations.ex5("data/output.txt")
# a = logOperations.ex6("data/output.txt")
# a = logOperations.ex7("data/output.txt")
# a = logOperations.ex8("data/output.txt")
# a = logOperations.ex9("data/output.txt")
print(a)