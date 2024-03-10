# https://pandas.pydata.org/
# https://pandas.pydata.org/docs/reference/api/pandas.ExcelWriter.html
# pip install pandas
# pip install openpyxl
import pandas as pd 
item_price = pd.read_excel("fruit.xlsx")
item=item_price['Item']
price=item_price['Price']
print(item)
print(price)
