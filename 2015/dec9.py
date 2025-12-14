from aocd import get_data, submit
def solve1(test=True):
    # Your solution code here
    testdata = ''''''
    testans = ''
    if test:
		data = testdata
	else:
		data = get_data(day=9, year=2015)
    
    
    
    
    
    
    if test and result == testans:
    	print("Test passed")
    elif test and result != testans:
		print("Test failed")
	elif not test:
		print(result)
        submit(result, part="a", day=9, year=2015)

