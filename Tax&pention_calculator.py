#tax calculator

def calculate_tax(income):
    if income <= 9875:
        tax = income * 0.10
    elif income <= 40125:
        tax = 987.50 + (income - 9875) * 0.12
    elif income <= 85525:
        tax = 4617.50 + (income - 40125) * 0.22
    elif income <= 163300:
        tax = 14605.50 + (income - 85525) * 0.24
    else:
        tax = 33271.50 + (income - 163300) * 0.32
    return tax
def main():
    try:
        income = float(input("Enter your annual income: "))
        if income < 0:
            print("Income cannot be negative.")
            return
        tax = calculate_tax(income)
        print(f"The calculated tax on an income of ${income:.2f} is: ${tax:.2f}")
    except ValueError:
        print("Invalid input. Please enter a numeric value for income.")
if __name__ == "__main__":
    main()  



