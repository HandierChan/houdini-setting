# 存放路径
文件放在 `%HOMEPATH%\Documents\houdini18.0\scripts\456.py`
(houdini 每次打开会自动读取 456.py 文件)

# Install_HDA 使用方法
'''
hdapath = 'C:/Users/handier/Documents/houdini18.0'
Install_HDA(hdapath)
'''
意思是默认去搜索 hdapath/hda 和 hdapath/otls 文件夹里的hda文件


'''
mypath = 'D:/houdini18.0'
Install_HDA(mypath,['aa','bb'],['cc'])
'''
意思是 `D:/houdini18.0` 里有三个文件夹，会搜索 aa、bb 文件夹，而不会搜索 cc 文件夹
