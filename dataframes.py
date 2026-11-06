import pandas as pd
data={
    "name":["riya","sara","diya","panda"],
    "age":[19,18,19,20],
    "marks":[99,89,90,85]
}
df=pd.DataFrame(data)
# print(df.query("age>20" and "marks>90"))
# df["state"]=["AP","TG","KA","RJ"]
# df["nation"]="India"
df[["state","nation","gender"]]=[["AP","Ind","M"],["TG","Ind","M"],["KA","Ind","F"],["RJ","Ind","F"]]
print(df)