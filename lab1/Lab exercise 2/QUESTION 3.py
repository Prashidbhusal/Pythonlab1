3#PRISE OF HOUSE IS 1M. IF A BUYER HAS CRADIT, THEY NEED TO PUT DOWN 10% OTHERWISE THEY NEED TO PUT DOWN 20%.
#PRINT THE DOWN PAYMENT.


price=1000000
credit_score=input("Enter if the buyer has good credit:")
if credit_score=='yes':
    credit_score=True
if credit_score==True:
    downpayment=(10/100)*price
else:
    downpayment=(20/100)*price
print("The price of the house is",downpayment)