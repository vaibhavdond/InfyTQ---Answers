#Assignment-3

mileage = 12
amount_per_litre = 40
distance_one_way = 190
cost_per_head = 0
divisible_by_five = False

total_cost_of_fair = (distance_one_way*2)/mileage * amount_per_litre

cost_per_head = total_cost_of_fair/4
if(cost_per_head%5 == 0):
    divisible_by_five = True

print(cost_per_head)
print(divisible_by_five)