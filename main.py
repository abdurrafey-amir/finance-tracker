import pandas as pd
import csv
from datetime import datetime
from entry import *


class CSV:
    CSV_FILE = 'data.csv'
    COLUMNS = ['date', 'amount', 'category', 'description']
    FORMAT = '%d-%m-%Y'
    @classmethod
    def init_csv(self):
        try:
            pd.read_csv(self.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns=self.COLUMNS)
            df.to_csv(self.CSV_FILE, index=False)

    @classmethod
    def add_entry(self, date, amount, category, description):
        new_entry = {
            'date': date,
            'amount': amount,
            'category': category,
            'description': description
        }
        
        with open(self.CSV_FILE, 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.COLUMNS)
            writer.writerow(new_entry)
        print('entry added')

    @classmethod
    def get_transactions(self, start_date, end_date):
        df = pd.read_csv(self.CSV_FILE)
        df['date'] = pd.to_datetime(df['date'], format= CSV.FORMAT)
        start_date = datetime.strptime(start_date, CSV.FORMAT)
        end_date = datetime.strptime(end_date, CSV.FORMAT)

        mask = (df['date'] >= start_date) & (df['date'] <= end_date)
        filtered_df = df.loc[mask]

        if filtered_df.empty:
            print('no transactions found')
        else:
            print(f'transactions from {start_date.strftime(CSV.FORMAT)} to {end_date.strftime(CSV.FORMAT)}')
            print(filtered_df.to_string(index=False, formatters={'date': lambda x: x.strftime(CSV.FORMAT)}))

            total_income = filtered_df[filtered_df['category'] == 'income']['amount'].sum()
            total_expense = filtered_df[filtered_df['category'] == 'expense']['amount'].sum()

            print('\nsummary:')
            print(f'total income: {total_income}')
            print(f'total expense: {total_expense}')
            print(f'savings: {total_income - total_expense}')
        return filtered_df


def add():
    CSV.init_csv()
    date = get_date("enter date (dd-mm-yyyy) or enter for today's date: ", allow_default=True)
    amount = get_amount()
    category = get_category()
    description = get_description()
    CSV.add_entry(date, amount, category, description)


# CSV.get_transactions('21-01-2000', '15-08-2024')
# add()
