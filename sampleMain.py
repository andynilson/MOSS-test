import mosspy

userid = 505447473
moss = mosspy.Moss(userid, "python")


# Files
moss.addFile("sumOfLeftLeavesWhileLoopSolutionBase.py")
moss.addFile("CarbonCopyOfsumOfLeftLeavesWhileLoopSolution.py")
moss.addFile("sumOfLeftLeavesWhileLoopSolutionVariabeDeclarationOrderChangedMultipleComments.py")
moss.addFile("sumOfLeftLeavesWhileLoopSolutionVariabeDeclarationOrderChangedMultipleComments.py")
moss.addFile("sumOfLeftLeavesWhileLoopSolutionBaseWithCommentsStrategicallyPlacedToHidePlagiarism.py")
moss.addFile("SumOfLeftLeavesPointToPointSolutionBase.py")

# progress function optional, run on every file uploaded
# result is submission URL
url = moss.send(lambda file_path, display_name: print('*', end='', flush=True))
print()

# print report url
print("Report Url: " + url)



