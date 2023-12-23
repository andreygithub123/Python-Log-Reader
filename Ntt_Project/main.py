from readFromFile import *
from exercicesImpl import *

# variables declaration
timestamps = []
log_types = []
descriptions = []

numberOfErrors = 0
numberOfDebugs = 0
numberOfInfos = 0

lines = readFile('./output.txt')
timestamps, log_types, descriptions = extractInfo(lines)

# ex1(log_types)
# ex2(descriptions)
# ex3(descriptions)

# ex4 and 5 can be made by using same method. (the method from 5 by adding log_type and process statement (suc or failed))
# ex4(descriptions, log_types)
ex5(descriptions, log_types)




