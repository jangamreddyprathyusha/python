# forest:multiple of trees or no.of trees in one node
# class:grouping the data regre: cal math data

# import pandas as pd
# from sklearn.ensemble import RandomForestClassifier
# data={
#     "marks":[89,87,38,98,23,29,59,96,33,35,29,90],
#     "result":[1,1,1,1,0,0,1,1,0,0,0,1]
# }
# df=pd.DataFrame(data)
# print(df)
# X=df[["marks"]]
# y=df["result"]
# model=RandomForestClassifier(
#     n_estimators=100,
#     criterion="gini",
#     max_depth=None,
#     max_features=1,
#     max_leaf_nodes=2,
#     random_state=42
# )
# model.fit(X,y)
# print(model.predict([[1]]))

#pass or fail

import pandas as pd
data = {
    "marks": [89, 87, 38, 98, 23, 29, 59, 96, 33, 35, 29, 90],
    "result": [1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1]
}
df = pd.DataFrame(data)
df["result"] = df["result"].map({
    1: "Pass",
    0: "Fail"
})
print(df)

#pass or fail

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
data = {
    "marks": [89, 87, 38, 98, 23, 29, 59, 96, 33, 35, 29, 90],
    "result": [1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1]
}
X = df[["marks"]]
y = df["result"]
model = RandomForestClassifier(
    n_estimators=100,
    criterion="gini",
    max_depth=None,
    max_features=1,
    max_leaf_nodes=2,
    random_state=42
)
model.fit(X, y)
# Enter student marks
marks = int(input("Enter student marks: "))
if marks >= 35:
    print("Pass")
else:
    print("Fail")


# randamregression
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
data={
    "exp":[1,2,3,4,5],
    "salary":[10,20,30,40,50]
}
df=pd.DataFrame(data)
print(df)
X=df[["exp"]]
y=df["salary"]
model=RandomForestRegressor()
model.fit(X,y)
print(model.predict([[16]]))


# #streamlit
# import streamlit as st 
# st.button
# st.title
# #python -m 