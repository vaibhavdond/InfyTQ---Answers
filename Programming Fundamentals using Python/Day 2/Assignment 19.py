#Assignment-19

def calculate_bill_amount(food_type,quantity_ordered,distance_in_kms):
    bill_amount=0
    cost_per_plate = 0
    delivery_charge = 0

    if(quantity_ordered>=1 and distance_in_kms >0):
        if(food_type=="N"):
            cost_per_plate = 150
        elif(food_type=="V"):
            cost_per_plate = 120
        else:
            bill_amount = -1
    else:
        bill_amount = -1
    
    if(bill_amount!=-1):
        if(distance_in_kms>=1 and distance_in_kms<=3):
            delivery_charge = 0
        elif(distance_in_kms>=4 and distance_in_kms<=6):
            delivery_charge = (distance_in_kms-3)*3
        elif(distance_in_kms>6):
            delivery_charge = ((distance_in_kms-6) * 6) + 9 #Here 9 is the delivery charge for next 3 km
        bill_amount = quantity_ordered*cost_per_plate + delivery_charge
    return bill_amount


bill_amount=calculate_bill_amount("V",2,5)
print(bill_amount)