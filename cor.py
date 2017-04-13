import pandas as pd
import matplotlib.pyplot as plt



df=pd.read_csv("sleepdatamarch.csv")


df1=pd.read_csv("tweets.csv")

print list(df)





corr=df.apply(lambda s: df1.corrwith(s))
print corr

plt.matshow(corr)
plt.xlabel(list(df))
plt.ylabel(list(df1))
plt.show()

# fig = plt.figure()
# ax = fig.add_subplot(111)
# cax = ax.matshow(corr)
# fig.colorbar(cax)

# ax.set_xticklabels(df.columns)
# ax.set_yticklabels(df1.columns)


# print df.columns
# print df1.columns
# plt.show()

