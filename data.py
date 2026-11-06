# import matplotlib.pyplot as plt
# import pandas as pd
# data={
#     "Day":[1,2,3,4,5,6],
#     "Money":[500,800,300,600,1000,700]
# }
# df=pd.DataFrame(data)
#scatter plot
# plt.scatter(df["Day"],df["Money"])

# #line graph
# plt.plot(df["Day"],df["Money"],marker="o",color="red",linestyle="--",linewidth=2,label="day")
# plt.xlabel("Days")
# plt.ylabel("Money")
# plt.title("Pani puri sales")
# plt.legend()
# plt.show()

#bar graph
# import matplotlib.pyplot as plt
# overs=[1,2,3,4,5,6,7,8,9,10]
# ind_score=[16,5,9,12,4,6,8,7,20,12]
# aus_score=[10,4,20,12,9,1,6,7,18,9]
# plt.bar(overs,
#         ind_score,
#         color="red",
#         width=0.8,
#         label="IND")
# plt.bar(
#     overs,
#     aus_score,color="yellow",
#     width=0.8,
#     label="AUS",
#     alpha=0.5)
# plt.legend()
# plt.show()

#  another
# import matplotlib.pyplot as plt
# import numpy as np
# overs=np.array([1,2,3,4,5,6,7,8,9,10])
# ind_score=[16,5,9,12,4,6,8,7,20,12]
# aus_score=[10,4,20,12,9,1,6,7,18,9]
# width=0.4
# plt.bar(overs-width/2,
#         ind_score,
#         color="red",
#         width=width,
#         label="IND")
# plt.bar(overs+width/2,
#         aus_score,
#         color="yellow",
#         width=width,
#         label="AUS"
# #         alpha=0.5
# )
# plt.legend()
# plt.show()

#pie graph
# import matplotlib.pyplot as plt
# players=["virat","rohit","gill","rahul","pant"]
# score=[90,87,60,40,50]
# colors=["pink","yellow","orange","green","red"]
# plt.pie(
#     score,
#     labels=players,
#     autopct='%1.1f%%',
#     colors=colors,
#     startangle=90,
#     shadow=True,
#     pctdistance=0.7,
#     labeldistance=1.2,
#     explode=[0.2,0,0,0.3,0]
# )
# plt.legend()
# plt.show()

#histogram
# import matplotlib.pyplot as plt
# marks=[90,39,59,67,44,68,84,76,49,94,64,98,60,73]
# plt.hist(marks,
#          color="green",
#          label=marks,
#          width=5,
#          bins=6,
#          alpha=0.3
# )
# plt.xlabel("Marks")
# plt.ylabel("No.of values")
# plt.title("Grouping marks")
# plt.legend()
# plt.show()


#box plot
# import matplotlib.pyplot as plt
# salary=[1000,2000,3000,4000,5000]
# plt.boxplot(salary)
# plt.show()

#another
# import matplotlib.pyplot as plt
# it=[2099,3090,1000,5000,7000]
# salary=[1000,2000,3000,4000,5000]
# plt.boxplot(it,salary,vert=False)
# plt.show()


#area chart
# import matplotlib.pyplot as plt
# product=["A","B","C","D","E"]
# sales=[1000,3000,2000,2500,5000]
# plt.fill_between(product,sales)
# plt.show()

#another
import matplotlib.pyplot as plt
product=["A","B","C","D","E"]
raju=[1000,3000,2000,2500,5000]
ravi=[2000,3000,4000,1000,5000]
plt.fill_between(product,raju,ravi,color="blue",alpha=0.5,linewidth=5)
plt.show()
