import pandas as pd
df=pd.read_csv(r"c:\Users\lenovo\Downloads\job_salary_prediction_dataset.csv")
# print(df)
# print(df.columns)
# print(df.describe())
# print(df[df["experience_years"]>18])
# print(df.info())
# print(max(df[df["job_title"]=="AI Engineer"].salary))
# print(min(df[df["job_title"]=="AI Engineer"].salary))

#find no.of departments
print(df["job_title"].nunique)

#find min salary of any 5 job titles
# a=df.groupby("job_title")["salary"].min()
# print(a.head(5))

# #find max & avg any 5 job titles
# a=df.groupby("job_title")["salary"].agg(["max","mean"])
# print(a.head(5))

#find 2nd highest salary of name with salary
# a=df["salary"].sort_values(ascending=False).iloc[1]
# print(a)
# print(df[df["salary"]==a][["job_title","salary"]])

#find 2nd min salary of AI-Engineers
# print(df[df["job_title"]=="AI Engineer"]["salary"].sort_values().iloc[1])