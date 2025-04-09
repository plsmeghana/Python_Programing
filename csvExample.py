import pandas as pd
df = pd.read_csv('students.csv')
print(df)
df['Average'] = (df['Math'] + df['Science'] + df['English'])/3
print(df)
student_dict={}
for index,row in df.iterrows():
    student_dict[row['Name']] = round(row['Average'],2)
print(student_dict)
