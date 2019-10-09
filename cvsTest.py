import pandas
data=pandas.read_csv("c:\\Users\\shenjiajun\\Desktop\\test.csv")
print(data)
print(data.columns)                         #返回全部列名
print(data.shape)                           #f返回csv文件形状
print(data.loc[1:2])