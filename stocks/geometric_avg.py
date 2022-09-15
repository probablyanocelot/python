rstock_expect = input("what expected return?\n:")


gain1 = int(input()) # projected gain based on past returns of x years
gain2 = int(input()) # possibly opposite of projected gain?


geometric_average = ((1 + gain1) * (1 + gain2))**(1/2) - 1 # projected growth based on past returns

prob1 = int(input()) # percent of projected probable gain e.g. 25%
prob2 = int(input()) # percent of projected probable loss e.g. 5%

inv1 = int(input("investment in $\n:")) # how much invested
prob_weight_value = (inv1 * prob1) * (0.5) + (inv1 * prob2) * (0.5) # avg's return, accounting for prob profit&loss