import pandas as pd 
from sklearn.preprocessing import LabelEncoder 
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
df=pd.read_csv(r"c:\Users\lenovo\Downloads\job_salary_prediction_dataset.csv")
print(df.describe())
print(df.info())
#step2 preprocessing
jt=LabelEncoder()
el=LabelEncoder()
df["job_title"]=jt.fit_transform(df["job_title"])
df["education_level"]=el.fit_transform(df["education_level"])
X=df[["job_title","experience_years","education_level","skills_count"]]
y=df["salary"]
#step 3 train & test data
X_train,X_test,Y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
#step 4:training model
model=LinearRegression()
model.fit(X_train,Y_train)
#step 5:predict
job_title=input("Enter job title:")
experience_years=int(input("enter experience years:"))
education_level=input("enter education level:")
skills_count=int(input("enter skill count:"))

#conver string values into numbers
job_title_num=jt.transform([job_title])[0]
education_level_num=el.transform([education_level])[0]
pred=model.predict([[job_title_num,experience_years,education_level_num,skills_count]])
print(pred)
print(df)