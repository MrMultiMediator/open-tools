import sys
def worthit(sr, rate, years, mp, hv, rent, nw):
	"""
	This function determines the difference between the cost of taking out a mortgage as opposed to
	saving and buying a house in cash, based on the set of parameters provided by the user. It runs
	through the two scenarios, calculating a cost for each and then subtracts the two.
	Parameters:
	0.) sr = Savings rate
	1.) rate = Interest rate
	2.) years = Years
	3.) mp = Monthly payment in dollars
	4.) hv = Home value
	5.) rent = Monthly rent
	6.) nw = Net worth
	"""
	nw0 = nw
	rate *= 0.01

	cost1 = hv #Cost of the home if you wait to buy in cash.
	while nw < hv:
		nw += sr
		cost1 += rent

	nw = nw0
	cost2 = 0.0 #Cost of the home if you take a mortgage out immediately
	cost2 += nw
	principle = hv-nw

	while principle > 0.0:
		if rate*principle/12. > mp:
			print("This parameter set is invalid. Monthly payment < monthly interest in mortgage")
			return
		principle += rate*principle/12.
		principle -= mp
		cost2 += mp

	print(str(sr)+' '+str(nw)+' '+str(rate)+' '+str(years)+' '+str(mp)+' '+str(hv)+' '+str(rent)+' '+str(cost1-cost2))


if __name__ == '__main__':
	f = open(sys.argv[1],'r')
	f.readline()

	print("\ncost1 is the amount spent on rent plus the value of the home when eventually bought.")
	print("cost2 is the amount spent in total on the mortgage over it's entire period.")
	print("I.e. cost1-cost2 < 0: It is cheaper to save and buy in cash.\n")
	print("Savings rate  Net worth  Rate  Years  Monthly payment  Home value  Rent(Mo)  cost1-cost2")

	for line in f:
		line = line.split()
		worthit(float(line[0]), float(line[1]), int(line[2]), float(line[3]), float(line[4]), float(line[5]), float(line[6]))

	f.close()
