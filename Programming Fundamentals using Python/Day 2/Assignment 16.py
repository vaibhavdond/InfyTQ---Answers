#Assignment-16

def make_amount(rupees_to_make,no_of_five,no_of_one):
    five_needed=0
    one_needed=0
    
    total_we_have = 5*no_of_five + no_of_one
    if(rupees_to_make>total_we_have):
        print(-1)
    else:
        five_needed = int(rupees_to_make/5)
        if(five_needed == 0):
            if(no_of_one >= rupees_to_make):
                one_needed=rupees_to_make
        elif(no_of_five>=five_needed):
            remainig_rupees = rupees_to_make - 5*five_needed
            if(no_of_one>=remainig_rupees):
                one_needed = remainig_rupees
        else:
            five_needed=no_of_five
            remainig_rupees = rupees_to_make - 5*five_needed
            if(no_of_one>=remainig_rupees):
                one_needed = remainig_rupees
            
        total = 5*five_needed + one_needed
        if(total == rupees_to_make):
            print("No. of Five needed :", five_needed)
            print("No. of One needed  :", one_needed)
        else:
            print(-1)

make_amount(100,21,5)