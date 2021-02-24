#Exercise-7

def calculate_total_ticket_cost(no_of_adults, no_of_children):
    total_ticket_cost = 0
    price_per_adult = 37550
    price_per_child = (price_per_adult)/3
    charge_for_all_passengers = (no_of_adults*price_per_adult) + (no_of_children*price_per_child)
    charge_including_tax = 107/100 * (charge_for_all_passengers)
    total_ticket_cost = 90/100 * (charge_including_tax)
    return total_ticket_cost

total_ticket_cost=calculate_total_ticket_cost(1,2)
print("Total Ticket Cost:",total_ticket_cost)