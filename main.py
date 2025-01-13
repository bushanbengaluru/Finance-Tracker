import pandas as pd
import csv
import os
from datetime import datetime
from data_entry import get_date, get_amount, get_category, get_description
class CSV:
    CSV_File = 'finance_data.csv'
    COLUMNS = ['Date', 'Amount', 'Category', 'Description']
    FORMAT = '%m/%d/%Y'
    @classmethod
    def initialize_csv(cls): #cls is a reference to the class itself
        try:
            pd.read_csv(cls.CSV_File)
        except FileNotFoundError:  
            df = pd.DataFrame(columns=['Date', 'Amount','Category', 'Description'])
            df.to_csv(cls.CSV_File, index=False)

    @classmethod
    def add_entry(cls, date, amount, category, description):
        new_entry = {
            'Date': date,
            'Amount': amount,
            'Category': category,
            'Description': description
        }
        with open(cls.CSV_File, mode='a', newline='') as csvfile:
            csv_writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMNS)
            csv_writer.writerow(new_entry)
        print("Entry added successfully")
    
    @classmethod
    def get_transactions(cls, start_date, end_date):
        df = pd.read_csv(cls.CSV_File)
        df['Date'] = pd.to_datetime(df['Date'], format=CSV.FORMAT) 
        start_date = datetime.strptime(start_date, CSV.FORMAT)
        end_date = datetime.strptime(end_date, CSV.FORMAT)
        mask = (df["dare"] >= start_date) & (df["Date"] <= end_date)
        filtered_df = df.loc[mask] #locating the rows that meet the condition

        if filtered_df.empty:
            print("No transactions found for the specified date range")
        else:
            print(f"Transactions from {start_date.strftime(CSV.FORMAT)} and {end_date.strftime(CSV.FORMAT)}")
            print(filtered_df.to_string(index=False, formatters="date": lambda x: x.strftime(CSV.FORMAT)))
def add():
    CSV.initialize_csv()
    date = get_date("Enter Date (MM/DD/YYYY) or Enter for today's date: ", allow_default=True)
    amount = get_amount()
    category = get_category()
    description = get_description()
    CSV.add_entry(date, amount, category, description)