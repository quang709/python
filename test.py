import pandas as pd
excel_file = 'test.xls'
movies = pd.read_excel(excel_file)
movies_sheet1 = pd.read_excel(excel_file, sheetname=0, index_col=0)
movies_sheet1.head()
