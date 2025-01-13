from datetime import datetime

def get_date(prompt, allow_default=False):
    date_format = '%m/%d/%Y'
    date_str = input(prompt)
    if allow_default and not date_str:
        return datetime.now().strftime(date_format)
    try:
        valid_date = datetime.strptime(date_str, date_format)
        return valid_date.strftime(date_format)
    except ValueError:
        print("Invalid date format. Please enter a date in the format MM/DD/YYYY")
        return get_date(prompt, allow_default)

def get_amount():
    try:
        amount = float(input("Enter Amount: "))
        if amount <= 0:
            raise ValueError("Amount must be greater than 0")
        return amount
    except ValueError as e:
        print(e)
        return get_amount()

def get_category():
    Catergories =  {"I": "Income", "E": "Expense"}
    catergory = input("Enter the category('I' for income OR 'E' for Expense): ")
    if catergory.upper() not in Catergories:
        print("Invalid category. Please enter 'I' for income or 'E' for expense")
        return Catergories[catergory.upper()]
    print("Invalid category. Please enter 'I' for income or 'E' for expense")
    return get_category()

def get_description():
    return input("Enter Description: ")
