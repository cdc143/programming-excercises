#Takes in list of ints as argument (which is assumed to be sorted "chronologically")
#Returns a tuple in the form (max profit, buy date, sell date)
#Returned buy and sell indicies are incremented by one (so that non cs people can use this too :)
#-1 indicates no their are no possible sell/buy dates
#This solution uses dynamic programming and has an worst case asymtotic time complexity of O(n) and a space complexity of O(1)


def maxProfit(prices):
    cur_max_profit = 0
    if len(prices) == 0:
        return (cur_max_profit,-1,-1)
    cur_min_price = prices[0]
    cur_min_idx = 0
    cur_max_idx = 0
    for day in range(1, len(prices)):
        if prices[day] < cur_min_price:
            cur_min_price = prices[day]
            cur_min_idx = day + 1
        if (prices[day] - cur_min_price > cur_max_profit):
            cur_max_profit = prices[day] - cur_min_price
            cur_max_idx = day + 1
    return (cur_max_profit,cur_min_idx,cur_max_idx)


def main():
    prices = [1 , 1, 3, 5, 0, 7]
    max_profit = maxProfit(prices)
    print "Maximum profit is:", max_profit[0]
    print "Buy on day", max_profit[1], "and sell on day", max_profit[2]

if __name__ == "__main__":
    main()
