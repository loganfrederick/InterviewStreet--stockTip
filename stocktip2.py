# stockTip

from sys import exit

numTestCases=0
answer=[]

# Function: profitCalc
# Parameter pricesList: A list of stock prices for consecutive days
# Parameter profits: The current running profit total for the entire test case
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

        while True:
            try: dayPrice = raw_input()
            except EOFError: break
            for w in dayPrice.split(): prices.append(w)

        prices.append(dayPrice)
        startDays=startDays+1
        numDays=numDays-1

    profit=profitCalc(prices,0)
    answer.append(profit)
    numTestCases=numTestCases-1

j=0
while j<len(answer):
    print answer[j]
