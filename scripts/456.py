# By HandierChan
import hou,os

def Install_HDA(path, hdaFolderLists=['hda','otls'], hdaFolderBlacklists=['old','olds','backup'], hdaExtension=['.hda','.otl']):
    '''
    递归每个文件夹，自动加载搜索到的 *.hda 和 *.otl
    path: 要搜索的路径
    hdaFolderLists: 只搜索路径里的这些文件夹
    hdaFolderBlacklists: 不搜索路径里的这些文件夹
    hdaExtension: 只搜索这些后缀名的文件（减少搜索时间）
    '''
    for hdaList in hdaFolderLists:
        hdaFullPath = path + '/' + hdaList
        for hdaRoot, hdaDirs, hdaFiles in os.walk(hdaFullPath, topdown=True):
            hdaDirs[:] = [i for i in hdaDirs if i not in hdaFolderBlacklists]
            for hdaFile in hdaFiles:
                for ext in hdaExtension:
                    if os.path.splitext(hdaFile)[1] == ext:
                        # print(os.path.normpath(path))
                        hou.hda.installFile(os.path.join(hdaRoot, hdaFile))

hda = 'C:/Users/handier/Documents/houdini18.0'
Install_HDA(hda)
