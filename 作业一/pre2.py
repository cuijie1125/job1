import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
df=pd.read_csv('e:\dmjob\job1\NFLPlaybyPlay2009-2017 (v4).csv')
#对标称属性，给出每个可能取值的频数
g1=df.groupby('ExPointResult')
g1.size()
g1=df.groupby('TwoPointConv')
g1.size()
#g1=df.groupby('PlayType')
#g1.size()
df['PlayType'].value_counts()
#平均数、最大、最小、四分位
df.describe()
#缺失数
total =df.isnull().sum().sort_values(ascending=False)
print(total)
#中位数：
df.median()
#直方图
c1=df[np.isnan(df['FieldGoalDistance'])==False]
fig = plt.figure()
ax = fig.add_subplot(111)
ax.hist(c1['FieldGoalDistance'], bins=10)
plt.title('Field Goal Distance')
plt.xlabel('Field Goal Distance')
plt.ylabel('NFL Play-by-Play 2009-2017')
plt.show()
#df['FieldGoalDistance'].dropna().hist(bins=10,range=(0,80))
#plt.show()
#盒图
fig = plt.figure()
ax = fig.add_subplot(111)
ax.boxplot(c1['FieldGoalDistance'])
plt.show()
#数据缺失处理
#统计缺失数据
total =df.isnull().sum().sort_values(ascending=False)
print(total)
#去掉缺失信息多的列
df = df.drop(['DefTwoPoint','BlockingPlayer','TwoPointConv','ChalReplayResult'], axis = 1)
#使用平均数填补
df['DefTeamScore'] = df['DefTeamScore'].fillna(df['DefTeamScore'].mean())
#用最高频率值来填补缺失值
df["down"].value_counts()
df['down'] = df['down'].fillna(1)
#返回已经去掉重复行的数据集
df.drop_duplicates()

#写到XLS文件

df.to_excel('e:\dmjob\job1\NFLPlaybyPlay-new.csv',sheetname='Sheet1')
