#Assignment-21

def generate_next_date(day,month,year):
    next_day=0
    next_month=0
    next_year=0
    if((year%4==0 and year%100!=0) or year%400==0):
        if(month>=1 and month<=7):
            if(month==2):
                if(day==29):
                    next_day = 1
                    next_month = month+1
                    next_year = year
                else:
                    next_day = day+1
                    next_month = month
                    next_year = year
            elif(month%2==0):
                if(day==30):
                    next_day = 1
                    next_month = month +1
                    next_year = year
                else:
                    next_day = day+1
                    next_month = month
                    next_year = year
            else:
                if(day==31):
                    next_day = 1
                    next_month = month +1
                    next_year = year
                else:
                    next_day = day +1
                    next_month = month
                    next_year = year
        elif(month>=8 and month<=12):
            if(month == 12):
                if(day==31):
                    next_day = 1
                    next_month = 1
                    next_year = year + 1
                else:
                    next_day = day + 1
                    next_month = month
                    next_year = year
            elif(month%2==0):
                if(day==31):
                    next_day = 1
                    next_month = month +1
                    next_year = year
                else:
                    next_day =day +1
                    next_month = month
                    next_year = year
            else:
                if(day==30):
                    next_day = 1
                    next_month = month + 1
                    next_year = year
                else:
                    next_day = day + 1
                    next_month = month
                    next_year = year
    else:
        if(month>=1 and month<=7):
            if(month==2):
                if(day==28):
                    next_day = 1
                    next_month = month+1
                    next_year = year
                else:
                    next_day = day+1
                    next_month = month
                    next_year = year
            elif(month%2==0):
                if(day==30):
                    next_day = 1
                    next_month = month +1
                    next_year = year
                else:
                    next_day = day+1
                    next_month = month
                    next_year = year
            else:
                if(day==31):
                    next_day = 1
                    next_month = month +1
                    next_year = year
                else:
                    next_day = day +1
                    next_month = month
                    next_year = year
        elif(month>=8 and month<=12):
            if(month == 12):
                if(day==31):
                    next_day = 1
                    next_month = 1
                    next_year = year + 1
                else:
                    next_day = day + 1
                    next_month = month
                    next_year = year
            elif(month%2==0):
                if(day==31):
                    next_day = 1
                    next_month = month +1
                    next_year = year
                else:
                    next_day =day +1
                    next_month = month
                    next_year = year
            else:
                if(day==30):
                    next_day = 1
                    next_month = month + 1
                    next_year = year
                else:
                    next_day = day + 1
                    next_month = month
                    next_year = year
    print(next_day,end="")
    print("-",end="")
    print(next_month,end="")
    print("-",end="")
    print(next_year)


generate_next_date(22,3,2011)