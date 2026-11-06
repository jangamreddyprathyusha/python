# import pandas as pd
# data=[10,20,30,40,50]
# s=pd.Series(data)
# print(s)

# import pandas as pd
# data=[10,20,30,40,50]
# s=pd.Series(data,index=['A','B','C','D','E'])
# print(s)

# import pandas as pd
# data=[10,"Priya",30,40,50]
# s=pd.Series(data)
# print(s)

# import pandas as pd
# data=[10,20,True,40,50]
# s=pd.Series(data)
# print(s)

# import pandas as pd
# data=[10,20,9.60,40,50]
# s=pd.Series(data)
# print(s)

# import pandas as pd
# data={"salary":[10,20,30,40,89,"90",56],"experience":[2,3,1,3,9,7,5]}
# df=pd.DataFrame(data)
# print(df)
# print(df.head())
# print(df.tail())
# print(df.info())
# print(df.describe())


# import pandas as pd
# s=pd.Series([10,True,30,40,50])
# print(s[:4])
# print(s[0:3:2])
# print(s[::-1])
# print(s[4:1:-1])
# print(s[0])

# import pandas as pd
# s=pd.Series([10,20,30,40,50],index=['A','B','C','D','E'])
# print(s)
# print(s['A'])
# print(s['E'])
# print(s.iloc[4])
# print(s.iloc[1:3])
# print(s[0])  #keyerror

# import pandas as pd
# df={
#     "name":["Priya","Riya","Sneha","Lara","chinu"],
#     "salary":[10,20,30,40,50]
# }
# print(df)

# import pandas as pd
# data={
#     "name":["riya","deena","panda","siri","chiya","lara"],
#     "marks":[90,94,87,89,80,40],
#     "sec":['A','B','C','D','E','F']
# }
# df=pd.DataFrame(data)
# print(df)
# print(df.iloc[5])
# print(df.name)   # "."Notation
# print(df.iloc[1:3])
# print(df.iloc[3:1:-1])
# print(df.marks.iloc[2])
# print(df["marks"].iloc[5])
# print(df[["marks","name"]].iloc[2])   #here [[]]-->use two brackets
# print(df.name.iloc[0])
# a=df["marks"]>90  #true or false
# a=df[df["marks"]>90]  # print names,marks,sec
# a=df[(df["marks"]>80) & (df["marks"]<90)]
# print(a)



# import pandas as pd
# data={
#     "name":["riya","deena","panda","siri"],
#     "age":[19,18,19,20],
#     "marks":[99,89,90,85]
# }
# df=pd.DataFrame(data)
# print(df.query("age>20" and "marks>90"))
# df[["state","nation","gender"]]=[["AP","India","F"],["TG","India","F"],["KA","India","F"],["UP","India","F"]]
# df.drop(columns=["state","gender"],inplace=True)
# df["name"]=["A","B","C","D"]
# df["name"]=df["name"]+" Rathod"
# x=df.loc[df["name"]=="panda"]
# x=df.loc[df["name"]=="panda","name"]="paandaa"
# print(x)
# print(df)

import pandas as pd
data={
    "date": ["2026-10-01", "2026-10-02", "2026-10-03", "2026-10-03", "2026-10-04"],
    "time": ["09:30:00", "10:15:00", "11:00:00", "12:30:00", "14:00:00"]
}
df=pd.DataFrame(data)
df["date"]=pd.to_datetime(df["date"])  #change datatype str to datetime
df["year"] = df["date"].dt.year
df["month"] = df["date"].dt.month
df["days"] = df["date"].dt.day
# df["monthname"]=df["date"].dt.month_name
# df["dayname"]=df["date"].dt.day_name
# df["yearname"]=df["date"].dt.is_year_end

df["time"]=pd.to_datetime(df["time"]) 
df["hours"] = df["time"].dt.hour
df["minutes"] = df["time"].dt.minute
df["second"] = df["time"].dt.second
# print(df.info())
print(df)
