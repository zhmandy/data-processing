import pandas as pd

# 导入评分数据
ratingData = pd.read_table(r"D:\zhmandy\courses\Data Processing-python\project movieAnalysis\ml-100k\u.data", sep='\t', names=['userid','itemid','rating','timestamp'], usecols=['userid','itemid','rating'])
#print(ratingData.groupby('userid').size())

#导入用户信息
userData = pd.read_table(r"D:\zhmandy\courses\Data Processing-python\project movieAnalysis\ml-100k\u.user", sep='|', names=['userid','age','gender'], usecols=['userid','age','gender'])

#合并
merggData = pd.merge(ratingData,userData,on='userid')
meanDataM = merggData[merggData.gender == 'M'].groupby('userid').rating.mean().std()
meanDataF = merggData[merggData.gender == 'F'].groupby('userid').rating.mean().std()

#将结果存入文本
with open(r'D:\zhmandy\courses\Data Processing-python\project movieAnalysis\movieresult.txt','w') as f:
    f.write("{:.0f}{:.0f}".format(meanDataM*100, meanDataF*100))