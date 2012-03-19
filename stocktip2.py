# stockTip2.py
# Solution to an InterviewStreet coding challenge
# Read README.txt for an explanation of this program.

from sys import exit

numTestCases=0
answer=[]

# Function: profitCalc
# Parameter pricesList: A list of stock prices for consecutive days
# Parameter profits: The current running profit total for the entire test case
# If the maximum price in the list is not the last number in the list,
# the pricesList is split in two, with the first one having its profit calculated and added to a running total
# and the second is called by the profitCalc function agian.
def profitCalc(pricesList,profits):
    tempProfits=0
    maxPrice = max(pricesList)
    maxPriceIndex = pricesList.index(maxPrice)
    
    if (maxPriceIndex==(len(pricesList)-1)):
        i=0
        while i<maxPriceIndex:
            tempProfits=tempProfits+(maxPrice-pricesList[i])
            i=i+1
    else:
        firstList=pricesList[0:(maxPriceIndex+1)]
        tempProfits=tempProfits+profitCalc(firstList,tempProfits)
        secondList=pricesList[(maxPriceIndex+1):(len(pricesList)+1)]
        tempProfits=tempProfits+profitCalc(secondList,tempProfits)

    return tempProfits

# Program begins
# I/O: stdin and stdout

print "Enter Number of Test Cases: " 
numTestCases=raw_input()
numTestCases=int(numTestCases)

while numTestCases>0:

    numDays=0
    prices=[]
    dayPrice=0
    portfolio=[]
    profit=0

    print "Enter number of days: "
    numDays=int(raw_input())

    startDays=1
    while numDays>0:
        print "Enter stock price for day %d:" %startDays
        dayPrice = int(raw_input())

# Todo: Allow for all the prices to be entered on one line separated by spaces
#        while True:
#            try: dayPrice = raw_input()
#            except EOFError: break
#            for w in dayPrice.split(): prices.append(w)

        prices.append(dayPrice)
        startDays=startDays+1
        numDays=numDays-1

# Total profit for individual test case is summed through the recursive function
# Then the profit is appended to a list of answers for all the test cases
    profit=profitCalc(prices,0)
    answer.append(profit)
    numTestCases=numTestCases-1

j=0
while j<len(answer):
    print answer[j]
    j=j+1
