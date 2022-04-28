import mosspy

userid = 505447473
moss = mosspy.Moss(userid, "python")

# File submissions for sum of left leaves problem

# base while loop solution
moss.addFile("baseWhileLoopSolution.py")

# simple copy paste of base solution
moss.addFile("copyOfWhileLoopSolution.py")

# variable declaration order changed and a few single-line comments added
moss.addFile("solutionWithMinorChanges.py")

# variable declaration order changed and a few multi-line comments added
moss.addFile("solutionWithBiggerChanges.py")

# variable declaration order changed and comments strategically added to hide plagiarism
moss.addFile("solutionWithStrategicChanges.py")

# basic point to point solution - completely different to while loop
moss.addFile("pointToPointSolution.py")

# progress function optional, run on every file uploaded
# result is submission URL
url = moss.send(lambda file_path, display_name: print('*', end='', flush=True))
print()

# print report url
print("Report Url: " + url)
