wordlist=[
    'my name is zhangsan',
    'you are stupid',
    'my boyfriend is NB',
    'you looks like very smart i like you very much'
]
wordclass=[0,1,1,0]
from sklearn.feature_extraction.text import CountVectorizer #特征提取：用于提取符合机器学习算法支持的特征，比如文本和图片。
cv=CountVectorizer()
print(cv)
cvlist=cv.fit_transform(wordlist)#特征选择
# print(cvlist)
cvs=cvlist.toarray()#最近邻
# print(cvs)

from sklearn.naive_bayes import GaussianNB #高斯朴数贝叶斯
model=GaussianNB().fit(cvs,wordclass)#广义线性模型：预测数据（估计值）之间的残差平方和最小
# print(model)
testword=['your friend is stupid NB is like']
# print(testword)
testlist=cv.transform(testword)#特征选择
print(testlist)
tests=testlist.toarray()#最近邻
print(tests)
res=model.predict(tests)
print(res)