#Assignment-15

def find_product(num1,num2,num3):
    product=0
    if(num3==7):
        product = -1
    elif(num2==7):
        product = num3
    elif(num1==7):
        product = num2*num3
    else:
        product = num1*num2*num3
    return product

product=find_product(1,5,7)
print(product)