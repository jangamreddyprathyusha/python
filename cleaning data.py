import pandas as pd
data={
    "name": ["Prathyusha", " rahul", "RAHUL", "Anil ", "anil","Sneha", "SNEHA ", " Ravi", "ravi", 
            "Kiran","kiran ", "Pooja", "pooja", "Arjun", "ARJUN"],
    "age": [22, 25, 25, -5, 28,30, 30, 150, 24, 26,26, None, 23, 0, 27],
    "gender": ["Female", "Male", "M", "male", "MALE","Female", "F", "Male", "m", "Female","female", 
            "FEMALE", "F", "Male", "M"],
    "city": ["Hyderabad", "hyderabad", "HYDERABAD", "Chennai", "chennai", "Bangalore", "BANGALORE",
            " Hyderabad ", "HYDERABAD","Delhi", "delhi", "Mumbai", "MUMBAI", "Chennai", "chennai"],
    "salary": [30000, 40000, 40000, -10000, 45000,50000, 50000, 35000, 35000, 60000,
            60000, None, 32000, 45000, 45000],
    "email": ["prathyusha@gmail.com","rahul@gmail.com","RAHUL@GMAIL.COM","anil@gmail.com","anil@gmail",
        "sneha@gmail.com","sneha@gmail.com ","ravi@gmail.com","RAVI@GMAIL.COM",None,"kiran@gmail.com",
        "pooja@gmail.com","pooja@gmail.com","arjun@gmail.com","arjun@gmail.com"]
}
df=pd.DataFrame(data)

df=df.fillna(0)
df = df.drop_duplicates()
df = df.sort_values("name")
print(df)

df["name"]=(df["name"]
         .str.strip()
         .str.title())

df.loc[(df["age"]<0)|(df["age"]>100),"age"] = df["age"].median()
df["age"]=(df["age"]
           .astype(int))

df["gender"]=(df["gender"]
              .str.upper()
              .str.replace("FEMALE","F")
              .str.replace("MALE","M"))

df["city"]=(df["city"]
            .str.strip()
            .str.upper())


print(df)
