import os
os.system("cls")

#Function to calculate monthly installment
def calMonthlyInstallment(loanAmount,rate,term):
    monthlyInstallment = round((loanAmount * (((rate/100)/12)*((1+(rate/100)/12)**(term*12)))/(((1+(rate/100)/12)**(term*12))-1)),2)
    return monthlyInstallment

#Function to calculate total amount payable
def caltotalAmountPayable(installment,term):
    amountPayable = round(installment * (term * 12),2)
    return amountPayable

#Function to create debt service ratio
def calDSR(mortgage,commitment,income):
    DSR = round(((mortgage + commitment)/income)*100,2)
    return DSR

#function to modify threshold debt service ratio
def modifyDSR():
    while True:
        newDSR_Range = float(input("Enter a new guideline for debt service ratio: "))
        if newDSR_Range > 100 or newDSR_Range < 0:
            print("Error : insufficient value")
        else:
            print("Modify successful")
            return newDSR_Range

i=0
debtServiceRatioRange = 70
calculation = []

#Set a main menu
while i != 5:
    i = int(input("=====MAIN MENU=====\n1.Calculate new loan\n2.Modify DSR threshold\n3.View\n4.Delete\n5.Exit\n"))
    if i == 1:
        #insert the details and calculaton the loan
        while True:
            principalLoanAmount = float(input("Principal Loan Amount: "))
            if principalLoanAmount < 100000:
                print("Error : please enter a valid amount") #error message print when principal amount is less than 100000
                break 
            annualInterestRate = float(input("Annual Interest Rate: "))
            if annualInterestRate > 5 or annualInterestRate < 3:
                print("Error : invalid interest rate") #error message print when interest rate is not in between 3 and 5
                break
            loanTerm = int(input("Loan Term(in year): "))
            if loanTerm > 35:
                print("Error: The loan term is over 35 years") #error message print when principal amount is more than 35years
                break
            monthlyIncome = float(input("Monthly Income: "))
            if monthlyIncome < 1500:
                print("Error: Please input a valid amount") #error message print when monthly income is less than minimum salary
                break
            financialCommitments = float(input("Monthly Financial Commitment: "))
            if financialCommitments < 0:
                print("Error: Please input a valid amount")#error message print when financial commitment is less than 0
                break
            monthlyInstallment = calMonthlyInstallment(principalLoanAmount, annualInterestRate, loanTerm)
            totalAmountPayable = caltotalAmountPayable(monthlyInstallment,loanTerm)
            debtServiceRatio = calDSR(monthlyInstallment,financialCommitments,monthlyIncome)
            if debtServiceRatio <= debtServiceRatioRange:
                eligible = "Yes"
            else:
                eligible = "No"
            print("1.Monthly Installment: ", monthlyInstallment)
            print("2.Total Amount Payable: ", totalAmountPayable)
            print("3.Eligible for the loan based on DSR: ", eligible)

            calculation.append({"Principal Loan Amount": principalLoanAmount,
                                "Annual Interest Rate": annualInterestRate,
                                "Loan Term(in year)": loanTerm,
                                "Monthly Income": monthlyIncome, 
                                "Financial Commitments": financialCommitments,
                               "Monthly Installment": monthlyInstallment,
                               "Total Amount Payable": totalAmountPayable,
                               "Debt Service Ratio": debtServiceRatio,
                               "Eligible" : eligible})
            newCal = str(input("Add new calculation? [y/n]: "))
            if newCal != 'y':
                break
    elif i == 2:
        #modify threshold debt service ratio
        debtServiceRatioRange = modifyDSR()
        print("Latest guideline of Debt Service Ratio: ", debtServiceRatioRange)  
    elif i == 3:
        #display all calculations
        for count,index in enumerate(calculation,start=1):
            print(f"Calculaton {count}")
            for title,result in index.items():
                print(f"{title}:{result}")
            print()
    elif i == 4:
        #delete the previous calculation
        delete = int(input("Please choose the calculation you would like to delete: ")) - 1
        if 0 <= delete < len(calculation):
            deleted = calculation.pop(delete)
            print("Delete succesful")
        else:
            print("Error: not record found")
    else:
        #exit whole system
        print("System terminated")
        