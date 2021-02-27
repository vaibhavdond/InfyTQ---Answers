#Assignment-20

def calculate_loan(account_number,salary,account_balance,loan_type,loan_amount_expected,customer_emi_expected):
    eligible_loan_amount=0
    bank_emi_expected=0
    eligible_loan_amount=0


    first_digit = int(account_number/1000)
    if(first_digit==1):
        if(account_balance>=100000):
            if(salary>25000 and loan_type == "Car"):
                eligible_loan_amount = 500000
                bank_emi_expected = 36
                if(eligible_loan_amount>=loan_amount_expected and bank_emi_expected>=customer_emi_expected):
                    print("Account number:", account_number)
                    print("The customer can avail the amount of Rs.", eligible_loan_amount)
                    print("Eligible EMIs :", bank_emi_expected)
                    print("Requested loan amount:", loan_amount_expected)
                    print("Requested EMI's:",customer_emi_expected)
                else:
                    print("The customer is not eligible for the loan")
            elif(salary>50000 and loan_type == "House"):
                eligible_loan_amount = 6000000
                bank_emi_expected = 60
                if(eligible_loan_amount>=loan_amount_expected and bank_emi_expected>=customer_emi_expected):
                    print("Account number:", account_number)
                    print("The customer can avail the amount of Rs.", eligible_loan_amount)
                    print("Eligible EMIs :", bank_emi_expected)
                    print("Requested loan amount:", loan_amount_expected)
                    print("Requested EMI's:",customer_emi_expected)
                else:
                    print("The customer is not eligible for the loan")
            elif(salary>75000 and loan_type == "Business"):
                eligible_loan_amount = 7500000
                bank_emi_expected = 84
                if(eligible_loan_amount>=loan_amount_expected and bank_emi_expected>=customer_emi_expected):
                    print("Account number:", account_number)
                    print("The customer can avail the amount of Rs.",     eligible_loan_amount)
                    print("Eligible EMIs :", bank_emi_expected)
                    print("Requested loan amount:", loan_amount_expected)
                    print("Requested EMI's:",customer_emi_expected)
                else:
                    print("The customer is not eligible for the loan")
            else:
                print("Invalid loan type or salary")
        else:
            print("Insufficient account balance")
    else:
        print("Invalid account number")


calculate_loan(1001,40000,250000,"Car",300000,30)