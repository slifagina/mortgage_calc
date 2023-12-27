import matplotlib.pyplot as plt

loan_amount = 400000
ir = 4.02 # interest rate
P = ir / 100 / 12 # 1/100 of interest rate per month
payments = [2000, 2300] # list of different monthly payments to compare

"""
S #loan amount
I = S * P # interest part of payment
payment - I #debt part of payment
S - (payment - S * I) #new debt balance
"""

for payment in payments:
    S = loan_amount
    debt = [S]
    while (S > 0):
        if (S <= payment):
            payment = S
        I = round(S * P, 2)
        S = S - (payment - I)
        debt.append(S)
    print("Number of years to repay the loan: ", round(len(debt)/12, 1))

    plt.plot(debt)
    plt.xlabel('Months')
    plt.ylabel('Euro')
    plt.title('Mortgage Repayment')
    plt.grid(linestyle = 'dashed')
    plt.legend(['according to the loan offer', 'equal to the current rent payment'], title = 'Monthly payments') 

plt.show()