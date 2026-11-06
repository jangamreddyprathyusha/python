import pandas as pd
from sklearn.linear_model import LinearRegression
data={
    "exp":[1,2,3,4,5],
    "salary":[10000,15000,20000,25000,30000]
}
df=pd.DataFrame(data)
X=df[["exp"]]
y=df["salary"]
model=LinearRegression()
model.fit(X,y)
pred=model.predict([[6]])
print(pred)

# import pandas as pd
# import streamlit as st
# from sklearn.linear_model import LinearRegression      #Logistic regre  -->categories-->yes/no
# from sklearn.model_selection import train_test_split
# data ={"exp":[1,2,3,4,5],
#        "salary":[10000,15000,20000,25000,30000]}
# #numeric 
# df=pd.DataFrame(data)
# X=df[["salary"]].values  #input
# y=df["exp"]        #output                        
# X_train,X_test,Y_train,Y_test=train_test_split(X,y,test_size=0.2,random_state=42)
# st.title("Salary Prediction")
# model=LinearRegression()  #model name                   
# model.fit(X_train,Y_train)
# s=st.number_input("enter a salary")
# pred=model.predict([[s]])
# st.button("Submit")
# st.write(pred)







