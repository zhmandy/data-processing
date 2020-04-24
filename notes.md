## Data Acquisition and Representation

```python
file_obj=open(filename, mode='r', buffering=-1, ...)  #read file
```

文本文件必须要缓冲，二进制文件可以不缓冲
w模式会清空原来内容
open()函数返回一个文件对象，文件对象可迭代

```python
with open('D:\zhmandy\courses\Data Processing-python\test.txt', 'w') as f:
    f.write('Hello World!') #with语句在执行结束后会自动关闭文件
file_obj.read(size) #从文件中至多读出size字节数据，返回一个字符串
file_obj.read() #读文件至文件结束，返回一个字符串
file_obj.readlines() #读多行数据，返回列表(保留'\n')
file_obj.seek(offset, whence=0) #在文件中移动文件指针
```

```python
r = requests.get(url)
r.status_code #查看状态，若出现200则成功
r.text #解码获得到的信息，可以有多种形式.json等
```

Beautiful Soup：从HTML或XML文件中提取数据的Python库

正则表达式-重要/有用-https://regex101.com/

```python
print('There are {0:d} punctuation marks.'.format(count)) #格式化输出
aList = ["hello","world"]
" ".join(aList) #利用空格将aList中的字符串连接起来
```

列表解析→动态创建列表

```python
[expression for expr in sequence1 if condition]
```

```python
2014, #创建单元素元组
```

Python中多个参数可以构成一个元组赋值给变量↓

```python
def foo(args1, *argst): #可变长位置参数
    ...
foo("Hello","Wang","Def","About") #*号收集参数，第一个Hello赋值给args1,后面三个都给argst
return 1,2,3 #返回一个元组(1,2,3)
```

```python
if __name__ == "__main__":
    ... #当模块被直接运行时，以下代码块将被运行，当模块是被导入时，代码块不被运行
```

**1.序列**

**(1) 序列的标准类型运算**

<、>、<=、>=、==、!= 值比较

is、is not 对象身份比较

and、or、not 逻辑运算

**(2) 通用序列类型操作**

seq[start: end]	切片操作

*	重复组合序列数据

		连接 2 个序列

	n、not in	判断元素是否存在序列中

**(3) 序列常用函数**

函数 描 述

list(iter) 将可迭代对象iter转换成列表

tuple(iter) 将可迭代对象iter转换成元组

str(obj) 将对象obj转换成字符串表示

len(sequence) 返回sequence的长度，为整型类型

sorted(iter, key, reverse) 返回可迭代对象iter排序后的列表，key用来指定排序的规则，reverse用来指定顺序还是逆序排列

reversed(sequence) 返回序列sequence逆序排列后的迭代器

sum(iter, start) 将iter中的数值和start参数的值相加，返回float类型数值

max(iter) 返回可迭代对象iter中的最大值

min(iter) 返回可迭代对象iter中的最小值

enumerate(iter[, start]) 返回一个enumerate对象，可生成一个迭代器，该迭代器的元素是由参数iter元素的索引和值组成的元组

zip(iter1 [,iter2 [...]]) 返回一个zip对象，可生成一个迭代器，该迭代器的第n个元素是每个可迭代对象的第n个元素组成的元组

**2.字符串**

**字符串常用方法**

方法	描述

s.capitalize() 返回字符串s首字母大写其余小写的形式

s.lower() 返回字符串s的小写形式

s.upper() 返回字符串s的大写形式

s.title() 返回字符串s的标题形式即单词首字母大写形式

s.format(*args, **kwargs) 格式化字符串操作

s.count(sub[, start[, end]]) 返回指定字符在[指定位置的]字符串s中出现的次数

s.find(sub[, start[, end]]) 返回指定字符在[指定位置的]字符串s中出现的索引号，找不到则返回-1

s.index(sub[, start[, end]]) 与 find()类似，不同的是如果找不到会引发ValueError异常

s.replace(old, new[, count]) 把字符串s中的old（旧字符串）替换成new（新字符串）。如果指定第三个参数count，则仅仅替换前count次出现的子串

s.lstrip([chars]) 移除字符串s左边的指定字符（默认为空格），返回移除字符串s左边指定字符后生成的新字符串

s.rstrip([chars]) 移除字符串s末尾的指定字符（默认为空格），返回移除字符串s末尾指定字符后生成的新字符串

s.strip([chars]) 移除字符串s头尾指定的字符（默认为空格），返回移除字符串s头尾指定字符后生成的新字符串

s.join(iterable) 用指定的字符串s连接元素为字符串的可迭代对象

s.split(sep=None, maxsplit=-1) 以指定的字符作为分隔符（默认为空格）分割字符串s，maxsplit指分割次数（默认为不限制次数）

s.endswith(suffix[, start[, end]]) 判断字符串s[的指定位置]是否以后缀suffix结尾

s.startswith(prefix[, start[, end]]) 判断字符串s[的指定位置]是否以前缀prefix开头

**3.列表**

**列表常用方法**

方法	描述

l.append(obj) 在列表l末尾添加新的对象

l.count(obj) 统计某个元素在列表l中出现的次数

l.extend(seq) 在列表l末尾一次性追加另一个序列seq中的多个值(用新列表扩展原来的列表)

l.index(obj) 从列表l中找出某个值第一个匹配项的索引位置，索引从0开始

l.insert(index, obj) 将对象obj插入列表l中索引为index的元素前

l.pop(index) 移除列表l中索引为index的一个元素(默认为最后一个元素)，并且返回该元素的值

l.remove(obj) 移除列表l中某个值的第一个匹配项

l.reverse() 将列表l中的元素反转

l.sort(key=None, reverse=False) 对原列表l进行排序，可通过参数key指定排序依据，通过参数reverse指定顺序（默认方式）或逆序排列

**4.元组**

**元组常用函数**

函数	描述

len(t) 计算元组t的元素个数

max(t) 返回元组t中元素的最大值

min(t) 返回元组t中元素的最小值

tuple(seq) 将序列seq转换为元组

> 所有标准序列操作，例如分片索引等，对字符串都是适用的，但是字符串都是不可变的，要注意不能对分片数据进行赋值

字典形成key-value对；值是无序的，只和key有关

```python
dict() #生成字典
d = {"name":"Andy"}
aDict = {}.fromkeys(("Amy","Zendy","Drama"),3000)
sorted(aDict) #返回一个列表，是key在内部的存储顺序
dict(zip(names,salaries))
```

```python
hash() #用于获取取一个对象（字符串或者数值等）的哈希值
aDict.keys()
aDict.values()
for k,v in aDict.items():
    print(k,v)
aDict.update()
aDict.get('AAA') #返回指定key的value，无则为none
aDict = {} #将aDict和字典的指向关系解除
aDict.clear() #直接将字典清空
```

```python
def func(args1, *argst, **argsd): #可变长关键字参数
    print(args1)
    print(argst)
    print(argsd)
func("Hello","Wandds","ASlic","ASdwddd",a1=1,a2=2,a3=3)
>Hello,
>("Wandds","ASlic","ASdwddd")
>{'a1':1,'a3':3,'a2':2}
```

```python
set(names) #删除重复项
#集合关系运算
```

```python
#numpy：ndarray数组
#series 带有索引；类似于字典；数据计算；数据对齐
#series对应一维序列；dataFrame对应二维表结构
data = {'name':["wanjd","asdasd","awww"],'pay':[4000,5243,3622]}
frame = pd.DataFrame(data)

data = np.array([("wanjd",4000),("asdasd",5000),("awww",40551)])
frame = pd.DataFrame(data,index=range(1,4),columns=['name','pay'])
#可以查看行索引/列索引/值
```

```python
#将网络下载数据csv转换为DataFrame
import pandas as pd
quotesdf = pd.read_csv(r'c:\...\xxx.csv')
print(quotesdf)
```

```python
#获取网路数据并存储至dataframe
import requests
import re
import pandas as pd
 
def retrieve_dji_list():
    r = requests.get('http://money.cnn.com/data/dow30/')
    search_pattern = re.compile('class="wsod_symbol">(.*?)<\/a>.*?<span.*?">(.*?)<\/span>.*?\n.*?class="wsod_stream">(.*?)<\/span>')
    dji_list_in_text = re.findall(search_pattern, r.text)
    dji_list = []
    for item in dji_list_in_text:
        dji_list.append([item[0], item[1], float(item[2])])
    return dji_list
 
dji_list = retrieve_dji_list()
djidf = pd.DataFrame(dji_list)
print(djidf)
#数据的预处理
cols = ['code', 'name', 'lasttrade']
djidf.columns = cols
```

```python
import requests
import re
import json
import pandas as pd
from datetime import date
 
def retrieve_quotes_historical(stock_code):
    quotes = []
    url = 'http://finance.yahoo.com/quote/%s/history?p=%s' % (stock_code, stock_code)
    r = requests.get(url)
    m = re.findall('"HistoricalPriceStore":{"prices":(.*?),"isPending"', r.text)
    if m:
        quotes = json.loads(m[0])
        quotes = quotes[::-1]
    return  [item for item in quotes if not 'type' in item]
quotes = retrieve_quotes_historical('IBM')
#数据预处理
list1 = []
for i in range(len(quotes)): #将数据中的时间戳转换成固定时间格式的时间
    x = date.fromtimestamp(quotes[i]['date'])
    y = date.strftime(x,'%Y-%m-%d')
    list1.append(y)
quotesdf_ori = pd.DataFrame(quotes, index = list1)
quotesdf = quotesdf_ori.drop(['date'], axis = 1)
print(quotesdf)

pd.date_range() #创建时间序列
```

可以通过数据显示来检查数据或程序结果是否符合要求

```python
dataFrame.loc( , ) #行索引、列索引
dataFrame.iloc( , ) #参数表示物理位置
dataFrame.ix() #ix是loc和iloc的混合
dataFrame.iat() #选择具体某个值
```

```python
np.sign(np.diff(dataFrame.xx)) #np.diff查看相邻数据的区别，np.sign获得数据符号(±1..)
```

```python
对象的describe()(dataFrame.describe())方法或用相关分析(dataFrame.corr())进行数据整体的查看和探索
dataFrame.sort_values( , ) #排序
dataFrame.groupby() #分组
#合并
dataFrame.append()
dataFrame.concat()
dataFrame.join() #基于共同字段合并
```

> K-means基本的聚类算法：以空间中k个点为中心进行聚类，对最靠近他们的对象归类
>
> 任意选择k个对象最为初始聚类中心，对每个确定其聚类中心点，计算每个新聚类的聚类中心，若是收敛的，则聚类完成；否则重复继续确定新聚类的中心

```python
# 本程序有一定的网络负载，可不运行程序根据结果理解程序
# 某次聚类结果：[2 2 1 1 2 2 2 2 0 0]
import requests
import re
import json
import pandas as pd
from sklearn.cluster import KMeans 
import numpy as np

def retrieve_quotes_historical(stock_code):
    quotes = []
    url = 'http://finance.yahoo.com/quote/%s/history?p=%s' % (stock_code, stock_code)
    r = requests.get(url)
    m = re.findall('"HistoricalPriceStore":{"prices":(.*?),"isPending"', r.text)
    if m:
        quotes = json.loads(m[0])
        quotes = quotes[::-1]
    return  [item for item in quotes if not 'type' in item]
 
def create_df(stock_code):
    quotes = retrieve_quotes_historical(stock_code)
    list1 = ['close','date','high','low','open','volume']
    df_totalvolume = pd.DataFrame(quotes,columns=list1)
    # 用数据的平均值代替数据中的空值（NaN）
    df_totalvolume = df_totalvolume.fillna(df_totalvolume.mean())
    return df_totalvolume
 
listDji = ['MMM','AXP','AAPL','BA','CAT','CVX','CSCO','KO','DIS','DD']
listTemp = [0] * len(listDji)
for i in range(len(listTemp)):
    listTemp[i] = create_df(listDji[i]).close
status = [0] * len(listDji)
for i in range(len(status)):
    status[i] = np.sign(np.diff(listTemp[i]))
# 简单处理某一只或几只股票数据没有获得（值为[])的问题，删掉此数据
for i in range(len(status)):
    if len(status[i]) == 0:
             status.pop(i)
             break
kmeans = KMeans(n_clusters = 3).fit(status) #fit进行聚类
pred=kmeans.predict(status) #predict预测每一个应属于哪个聚类
print(pred)
```

```python
#绘图
plt.plot(x, y, 'o') #散点图
plt.plot(x, y) #柱状图
plt.plot(x, y, 'string') #可以通过string变化来改变颜色样式等
plt.xlabel('')/plt.ylabel('')/plt.title('')
plt.subplot(...)/plt.axes([,,,]) #多个图在一个界面
#pandas绘图对于dataFrame格式的更方便
quoteslldf.boxplot() #箱型图
```

```python
df.to_csv('xx.csv') #dataFrame转csv格式
df.to_excel()/pd.read_excel()/pd.write_excel() #转读写Excel
```

```python
#PIL基本图像处理
from PIL import Image
im1 = Image.open('1.jpg')
Image.open('1.jpg').save('2.png')
im2 = Image.open('2.png')
size(288, 180)
im2.thumbnail(size)
out = im2.rotate(45)
im1.paste(out, (50, 50))
```

```python
#nltk自然语言处理工具包
#情态动词在文本很常用，不同文体中情态动词是否有不同的使用规律，以下程序用来比较情态动词can、could、may、might、must、will、would在新闻(news)和浪漫(romance)这两种不同文体中的频率，依据不同的“条件”即文体计算每个类别的频率分布，tabulate()方法用来为条件概率分布绘制分布表，其conditions参数指定要显示的条件这里是文体，默认为所有条件，samples参数指定要显示的样本这里是情态动词
import nltk
from nltk.corpus import brown

cfd = nltk.ConditionalFreqDist((genre, word)
           for genre in brown.categories()
           for word in brown.words(categories = genre))
genres = ['news', 'romance']
modals = ['can', 'could', 'may', 'might', 'must', 'will', 'would']
cfd.tabulate(conditions = genres, samples = modals)
cfd.plot(conditions = genres, samples = modals)
```

```python
# OOP
class ClassName(object): #（）内表示现在正定义的类的父类；若没有父类，默认父类为object
    'define ClassName Class' #Doc String
    pass
class Dog(object):
    def greet(self):
        print("Hi!")
dog = Dog()
dog.greet()
# 👆1.定义类——Dog 2.创建一个实例——dog 3.通过实例使用属性或方法——dog.greet
__init__() #类似其他语言的构造器
#类/静态属性；可由类中方法更新，也可在主程序更新；类属性和实例无关，修改类属性需要用类名
#继承：单继承/多继承；派生子类的时候可以对父类的方法进行改写
Class SubClassName(ParentClass1[, ParentClass2, ...]):
    'Optional class documentation string'
    pass
Class Dog(object):
    'define Dog Class'
    counter = 0
    def __init__(self, name):
        self.name = name
        Dog.counter += 1
    def greet(self):
        print("Hi! I am %s, my number is %d" % (self.name, Dog.counter))
Class BarkingDog(Dog):
    'define subclass BarkingDog'
    def greet(self): #重写了父类greet()方法
        'initial subclass'
        print("Woof! I am %s, my number is %d" % (self.name, Dog.counter))
if __name__ == '__main___':
    dog = BarkingDog('Zoe')
    dog.greet()
#默认python成员属性是public；可用控制访问符来限定成员函数访问
#双下划线__；限定属性和方法在类内部可见
#    _var属性会被__classname_var替换，防止父类与子类中的同名冲突
#单下划线_
#    在属性名前使用一个单下划线字符，防止模块的属性用'from mymodule import *'来加载
```

```python
#GUI-面向过程
import wx
app = wx.App()
frame = wx.Frame(None, title = "Hello, World!")
frame.Show(True)
app.MainLoop()
#GUI-面向对象
import wx
class MyApp(wx.App):
    def OnInit(self):
        frame = wx.Frame(None, title = "Hello, world!")
        frame.Show()
        return True
if __name__ == '__mian__':
    app = MyApp()
    app.MainLoop()
#GUI-面向对象-基于wx.Frame类派生
import wx
class Frame1(wx.Frame):
    def __init__(self, superior):
        wx.Frame.__init__(self, parent = superior, title = "Example", pos = (100, 200), size(350, 200))
        panel = wx.Panel(self)
        text1 = wx.TextCtrl(panel, value = "Hello, World!", size = (350, 200))
if __name__ == '__main__':
    app.wxApp()
    frame = Frame1(None)
    frame.Show(True)
    app.MainLoop()
```

> 布局管理
>
> sizer本身不是一个容器或者一个窗口部件，是屏幕布局算法；可嵌套
>
> 1.创建自动调用尺寸的容器，如panel
>
> 2.创建seizer
>
> 3.创建子窗口（窗体部件）
>
> 4.使用sizer.Add()方法将每个子窗口添加给sizer
>
> 5.调用容器的SetSizer(sizer)方法

```python
import wx 
class Frame1(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, title = "Example", pos= (100,200), size= (350,200))
        self.panel = wx.Panel(self)
        self.panel.Bind(wx.EVT_LEFT_UP, self.OnClick) 

    def OnClick(self, event):
        posm = event.GetPosition()
        wx.StaticText(parent = self.panel,label = "Hello, World!",pos = (posm.x, posm.y))
if __name__ == '__main__': 
    app = wx.App()
    frame = Frame1(None)
    frame.Show(True)
    app.MainLoop()
```

```python
import wx 
class Frame1(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, title = "Hello World in wxPython")
        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.text1= wx.TextCtrl(panel, value = "Hello, World!", size = (200,180), style = wx.TE_MULTILINE)
        sizer.Add(self.text1, 0, wx.ALIGN_TOP | wx.EXPAND)
        button = wx.Button(panel, label = "Click Me")
        sizer.Add(button)
        panel.SetSizerAndFit(sizer)        
        panel.Layout()
        self.Bind(wx.EVT_BUTTON,self.OnClick,button)
    def OnClick(self, text):
        self.text1.AppendText("\nHello, World!")
if __name__ == '__main__': 
    app = wx.App()
    frame = Frame1(None)
    frame.Show(True)
    app.MainLoop()
```

