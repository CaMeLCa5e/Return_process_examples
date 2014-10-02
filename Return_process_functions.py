## Process examples 

# return process to list using .append()
def process(xs):
	rv = []
	for x in xs:
		rv.append(x)
	return rv
	
# add process to x
def process(xs):
	rv = set()
	for x in xs:	
		rv.add(x)
	return rv
	
# add process to tuple 
def process(xs):
	rv = ()
	for x in xs:
		rv += (x,)
	return rv