# https://pandas.pydata.org/
# https://pandas.pydata.org/docs/reference/api/pandas.ExcelWriter.html
# pip install pandas
# pip install openpyxl
import pandas as pd 
df = pd.DataFrame([["Apple", 10], ["Orange", 12], ["Mango", 20]],columns=["Item", "Price"])
with pd.ExcelWriter("fruit.xlsx") as writer:
    df.to_excel(writer)
    