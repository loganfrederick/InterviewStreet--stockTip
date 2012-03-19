stockTip was written as a solution to a challenge from InterviewStreet.com's CodeSprint on February 25th.

I lost the copy of the official problem text, but here were the main ideas from the Challenge.

Reading the challenge, devising a solution, and programming it took about 45 minutes in total. This is also my first worthwhile program in Python, so most of the time was spent solving the problem on paper and looking up Python syntax.

The Challenge:
Imagine you are an investor who can accurately predict the prices out N number of days.
Because of your divination abilities, you should be able to maximize your profit over the duration of the time period.

However, one any given day, you can only do one of three actions:
1. Buy *one* share of stock.
2. Sell any number of stock you might own.
3. Nothing.

Write a program which, given T test cases, each with N number of days with P prices, determine the maximum profit you can make.

Constraints:
1 <= T <= 100
1 <= N <= 50
P: Only integers

Example Test Cases (The prices per day are separated):
1
1 10
3 1
1 2 5
1 2 5 1 3 2
1 2 1 5 1 3 2

Example Solutions:
Profit = 0
Profit = 9
Profit = 0
Profit = 7
Profit = 9
Profit = 13

My Solution Explanation:
The key to solving this problem ar the definitions of the three actions. Because you can only purchase one share of stock a day, but sell any number of them, there is no advantage to selling at local maximums and buying more at minimums because you can only purchase one stock a day.

In the last example test case, in a market where you can buy more than one share of stock per day, you would buy one share on day one, sell your stock on day two, and then buy two shares on day three. However, the rules forbid buying multiple shares.

Therefore, to maximize profit, the investor should buy one share of stock every day and sell all of it at the "global maximum" where every share purchased up to that day can be sold at the highest price. However, this maximum is not "global" by the traditional mathematical definition, because after a day has passed, it obviously does not affect future days.

This can be demonstrated using another example from the last test case. Stock purchased on days five, six and seven have can not be sold on day four. The stock price on day seven has no effect on any of the previous days, and in the given test case, is therefore useless information.

This logic led me to two key insights:
1. Stocks should be purchased every day until a global maximum. We can figure out the day with the global maximum because we know the prices for every future day.
2. If the global maximum is not on the last day, then the global maximum day and all its preceding days should have their profit calculated and removed from the list, so that the profits for the remaining days can be calculated in the same fashion.

After realizing the second point, the idea of sublists within the original price list leant itself to a recursive solution. The profits for each set of days leading up to a global maximum are calculated, then this same process is applied to the list of days following the global maximum. The profits from each of these sublists are added together to find the overall profits for the time period of predicted stock prices.
