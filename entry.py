from datetime import datetime

dformat = '%d-%m-%Y'

def get_date(prompt, allow_default=False):
    date_str = input(prompt)

    if allow_default and not date_str:
        return datetime.now().strftime(dformat)
    
    try:
        valid_date = datetime.strptime(date_str, dformat)
        return valid_date.strftime(dformat)
    except ValueError:
        print('invalid format. please use dd-mm-yyyy')
        return get_date(prompt, allow_default)
    
def get_amount():
    try:
        amount = float(input('amount: '))
        if amount <= 0:
            raise ValueError('amount must be greater than 0')
        return amount
    except ValueError as e:
        print(e)
        return get_amount()

CATEGORIES = {'I': 'income', 'E': 'expense'}

def get_category():
    category = input('enter category (i/e): ').upper()
    if category in CATEGORIES:
        return CATEGORIES[category]
    print('invalid category, enter i/e')
    return get_category()

def get_description():
    return input('enter description (optional): ')