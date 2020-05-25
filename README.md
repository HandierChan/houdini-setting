目的：用文件夹分类了很多个 hda ，但 houdini 环境变量只能一个个文件夹加载，于是写下这个代码，自动递归加载文件夹每个 hda 文件

# 存放路径
文件放在 `%HOMEPATH%\Documents\houdini18.0\scripts\456.py`
houdini 每次打开会自动读取 456.py 文件

# Install_HDA 使用方法
修改 456.py 最后两行
▼ 例子一：默认去搜索 hdapath/hda 和 hdapath/otls 文件夹里的hda文件
```
hdapath = 'C:/Users/handier/Documents/houdini18.0'
Install_HDA(hdapath)
```

▼ 例子二：`D:/houdini18.0` 里有三个文件夹，会搜索 aa、bb 文件夹，而不会搜索 cc 文件夹
```
mypath = 'D:/houdini18.0'
Install_HDA(mypath,['aa','bb'],['cc'])
```
