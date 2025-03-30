import string
import math



def get_min_payment(principal: float, years, payment_number, interest_rate: float):
    """
    Computes the minimum payment for mortgage.

    Parameters:
    principal(float): Total amount of mortgage.
    years(int): Term of mortageg in years and defaults to 30.
    payment_number(int): Number of payments per year and defaults to 12.
    interest_rate(float): Annual interst rate and is in between 0 and 1.

    Returns:
    int: This the minimum monthly payment and is rounded up to the next highest integer.
    """
    years = 30
    payment_number = 12
    r = interest_rate / payment_number
    p = principal
    n = years * payment_number
    if p <= 0:
        raise ValueError("Principle has to be greater than 0")
    if not (0 < interest_rate <= 1):
        raise ValueError("Interest rate has to be between 0 and 1, ex 3.5% would be 0.035")
    if r == 0:
        payment = p / n
    else:
        payment = (p * r * (1+r) ** n / ((1+r) ** n - 1))
    return math.ceil(payment)
    
    

def interest_due(balance: float, interest_rate: float, payment_number):
    """
    Computes the total interest due for the next payment

    Parameters:
    balance(float): Remaining balance of the mortgage.
    interest_rate(float): Annual interest rate which is between 0 and 1.
    payment_number(int): Number of payments for the year and defaults to 12.

    Returns:
    float: The amount of interest due for the next payment
    """
    payment_number = 12
    if balance <= 0:
        raise ValueError("The balance of the mortgage has to be a positive number")
    if not (0 < interest_rate <= 1):
        raise ValueError("Interest rate has to be between 0 and 1, ex 3.5% would be 0.035")
    b = balance
    r = interest_rate / payment_number
    i = b * r
    return i



def remaining_payment(balance: float, interest_rate: float, target_payment: float, payment_number):
    """
    Computes the number of remaining payments needed to comepletely pay off the mortgage.

    Parameters:
    balance(float): Remaining balance of the mortgage.
    interest_rate(float): Annual interest rate between 0 and 1.
    target_payment(float): Amount the user wants to pay every payment
    payment_number(float): Number of payments annually and defaults to 12

    Returns:
    int: Number of payments left to pay off the mortgage.
    """
    if balance <= 0:
        raise ValueError("The balance of the mortgage has to be a positive number")
    if target_payment <= 0:
        raise ValueError("The target payment has to be a positive number")
    if not (0 < interest_rate <= 1):
        raise ValueError("Interest rate has to be between 0 and 1, ex 3.5% would be 0.035")
    payment_number = 12
    counter = 0
    r = interest_rate / payment_number
    while balance > 0:
        interest = interest_due(balance, interest_rate, payment_number)
        principle = target_payment - interest
        if principle <= 0:
            raise ValueError("The target payment is too low to cover the interest.")
        balance -= principle
        counter += 1
    return counter



def main(principle: float, interest_rate: float, years, payment_number, target_payment: float):
    """
    Main function in order to compute/display mortgage details

    Parameters:
    principal(float): Total amount of mortgage.
    interest_rate(float): Annual interest rate between 0 and 1.
    years(int): Term of mortageg in years and defaults to 30.
    payment_number(float): Number of payments annually and defaults to 12
    target_payment(float): Amount the user wants to pay every payment
    """
    years = 30
    payment_number = 12
    p = principle
    if principle <= 0:
            raise ValueError("The target payment is too low to cover the interest.")
    if target_payment <= 0:
        raise ValueError("The target payment has to be a positive number")
    if not (0 < interest_rate <= 1):
        raise ValueError("Interest rate has to be between 0 and 1, ex 3.5% would be 0.035")
    if p <= 0:
        raise ValueError("Principle has to be greater than 0")
    min_payment = get_min_payment(p, years, interest_rate, payment_number)
    print(f"Your minimum mortage payment is : ${min_payment}")
    if target_payment is None:
        target_payment = min_payment
    if target_payment < min_payment:
        print("Your target payment is less than the minimum payment for this mortgage")
    else:
        balance = p
        total_payments = remaining_payment(balance, interest_rate, target_payment, payment_number)
        print(f"If you make payments of ${target_payment}, you will pay off the mortgage in {total_payments} payments")

          

    