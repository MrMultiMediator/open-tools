import sys
def running_int(principle,interest,years,cinv,compound):
    #cinv is the continuous investment amount. The amount added to the account each month.
    amount = principle
    counter = 0

    while counter < years*compound:
        amount = amount + amount*interest*0.01/compound + cinv*(12./compound)

        counter += 1

    print(str(principle)+'  '+str(interest)+'  '+str(years)+'  '+str(compound)+'  '+str(cinv)+'  '+str(amount))

if __name__ == '__main__':
    #Read the input file. Each line contains 5 variables: principle, interest rate, number of years, continuous, monthly
    #investment amount, and compounding rate.
    #Run it through the compound interest calculator which will print the result to the screen
    comp_dict = {'monthly':12., 'annually':1., 'semiannually':2., 'weekly':52., 'daily':365.}

    f = open(sys.argv[1],'r')
    f.readline() #Skip first line of input file

    print('Principle  Interest rate  Years  Compound rate  Continuous investment  Final Amount')

    for line in f:
        running_int(float(line.split()[0]),float(line.split()[1]),float(line.split()[2]),float(line.split()[3]),comp_dict[line.split()[-1]])
    f.close()
