import pandas as pd
import csv
from datetime import datetime
import entry


class CSV:
    CSV_FILE = 'data.csv'
    COLUMNS = ['date', 'amount', 'category', 'description']
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


CSV.init_csv()
CSV.add_entry('21-01-2000', 100, 'food', 'lunch')