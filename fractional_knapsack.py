def Fractional_knapsack(items_wt, price, capacity):
    n = len(items_wt)

    # items = [(24,3,7), (12,4,3), (10,5,2)]
    items = [ (price[i], items_wt[i], price[i]/items_wt[i]) for i in range(n)]

    for i in range(n):
        for j in range(i+1,n):
            if( items[i][2] < items[j][2]):
                items[i], items[j] = items[j], items[i]

    profit = 0.0
    for price, item_wt, perkgpPrice in items:
        if capacity >= item_wt:
            capacity = capacity - item_wt
            profit = profit + price
        else:
            profit = profit + perkgpPrice*capacity

    print("Total profit = ", profit)

price = [24,21,12,10]
item_wt = [7,3,4,5]
capacity = 20

Fractional_knapsack(item_wt,price,capacity)