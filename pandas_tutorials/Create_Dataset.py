import pandas as pd

data= {'Name': ['Mitu','Shahadat','Masud','Sourov','Mahi','Sumaiya'],
      'Age': [23,23,24,22,22,20],
      'Gender': ['F','M','M','M','F','F'],
      'Marks': [80,83,'NaN',90,92,'NaN']}
df =pd.DataFrame(data)

# df.to_csv('students.csv', index=False) 

exel = df.to_excel('students1.xlsx', index=False)

read_csv = pd.read_csv('students.csv')
print(read_csv)
