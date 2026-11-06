# house sales prediction 
import pandas as pd 
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import streamlit as st


df=pd.read_csv(r"c:\Users\lenovo\Downloads\hyderabad_house_price_synthetic_20000.csv")
area_name=LabelEncoder()
property_type=LabelEncoder()
furnishing=LabelEncoder()
gated_community=LabelEncoder()

df["area_name"]=area_name.fit_transform(df["area_name"])
df["property_type"]=property_type.fit_transform(df["property_type"])
df["furnishing"]=furnishing.fit_transform(df["furnishing"])
df["gated_community"]=gated_community.fit_transform(df["gated_community"])

X=df[["area_name","property_type","bhk","bathrooms","balconies","area_sqft","age_years","furnishing","parking","floor","total_floors","gated_community","distance_to_metro_km"]]
y=df["price_inr"]

X_train,X_test,Y_train,Y_test=train_test_split(X,y,test_size=0.2,random_state=42)

model=RandomForestRegressor(n_estimators=100,random_state=42)

model.fit(X_train,Y_train)

st.title("House Sale Prediction")
st.subheader("Choose your Options ")
area_name1=st.selectbox("select Any area_name",area_name.classes_.tolist())
property_type1=st.selectbox("select property_type",property_type.classes_.tolist())
bhk1=st.number_input("select bhk",min_value=0,max_value=5)
bathrooms1=st.number_input("select bathrooms",min_value=0,max_value=5)
balconies1=st.number_input("select balconies",min_value=0,max_value=5)
area_sqft1=st.number_input("select area_sqft",min_value=100,max_value=1000)
age_years1=st.number_input("select age_years",min_value=0,max_value=20)
furnishing1=st.selectbox("select furnishing",furnishing.classes_.tolist())
parking1=st.number_input("select parking",min_value=0,max_value=20)
floor1=st.number_input("select floor",min_value=0,max_value=20)
total_floors1=st.number_input("select totalFloor",min_value=0,max_value=20)
gated_community1=st.selectbox("select gated_community",gated_community.classes_.tolist())
distance_to_metro_km1=st.number_input("select maxDist",min_value=0,max_value=20)

a=area_name.transform([area_name1])[0]
b=property_type.transform([property_type1])[0]
c=furnishing.transform([furnishing1])[0]
d=gated_community.transform([gated_community1])[0]
if(st.button("Sumbit")):
    pred=model.predict([[a,b,bhk1,bathrooms1,balconies1,area_sqft1,age_years1,c,parking1,floor1,total_floors1,d,distance_to_metro_km1]])
    st.write("pred amount",pred)
    
    
    
# 0   property_id           20000 non-null  str    
#  1   area_name             20000 non-null  str    
#  2   property_type         20000 non-null  str    
#  3   bhk                   20000 non-null  int64  
#  4   bathrooms             20000 non-null  int64  
#  5   balconies             20000 non-null  int64  
#  6   area_sqft             20000 non-null  int64  
#  7   age_years             20000 non-null  int64  
#  8   furnishing            20000 non-null  str    
#  9   parking               20000 non-null  int64  
#  10  floor                 20000 non-null  int64  
#  11  total_floors          20000 non-null  int64  
#  12  gated_community       20000 non-null  str    
#  13  distance_to_metro_km  20000 non-null  float64
#  14  price_inr             20000 non-null  int64