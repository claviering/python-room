import os
import xlrd
import xlwt
from os import listdir
from xlrd import open_workbook
from math import log
import re
 
# xpath是数据存放的路径
xpath="F:/大三/数据挖掘/taidi4/附件1：旅客列车梯形密度表（31天）"
# 这个是最后存数据用的文件
savefile = 'test.xls'
 
# 列出目录下所有文件
def list_all_files(rootdir):
    _files = []
    # subName = []
    # listdir返回指定文件夹包含的文件或文件夹名称的列表
    list = os.listdir(rootdir) # 列出文件夹下所有的目录与文件
    for i in range(0,len(list)):
        # join函数作用是把目录和文件名合成一个路径
        # os.path中有split函数可以将路径和文件名称分隔开
        path = os.path.join(rootdir, list[i])
        # 注意append和extend的区别
        # isdir判断是否为路径，isfile判断是否为文件
        if os.path.isdir(path):
            _files.extend(list_all_files(path))
        if os.path.isfile(path):
            _files.append(path)
    return _files

def set_style(name,height,bold=False):
    style = xlwt.XFStyle()
    font = xlwt.Font()
    font.name = name
    font.bold = bold
    font.color_index = 4
    font.height = height
    style.font = font
    return style

def write_excel():
    f = xlwt.Workbook()
    sheet1 = f.add_sheet('data', cell_overwrite_ok=True)
    row0 = ["日期", "车次","车站","时间","上车人数"]
    #写第一行
    for i in range(0,len(row0)):
        sheet1.write(0, i, row0[i], set_style('Times New Roman',220,True))
    # for i in range(1, 5):
    #     for j in range(12):
    #         sheet1.write(i, j, 3)
    f.save(savefile)

# 读取excel中的数据
def read_excel(file):
    outData = []#存储了所有合并单元格的数据，因为特征名字也合并了，所以也在这里
    outClo1 = []#用于返回的数据
    outCloLog = []#进过log处理后用于返回的数据
    wb = xlrd.open_workbook(file)
    sheet1 = wb.sheet_by_index(0)
    #处理合并单元格的问题
    merge = []
    for (rlow, rhigh, clow, chogh) in sheet1.merged_cells:
        merge.append((rlow, clow))
    for index in merge:
        outData.append(sheet1.cell_value(index[0], index[1]))
    return outClo1

if __name__ == '__main__':
    write_excel()
    file = list_all_files(xpath)
    for i in range(len(file)):
        print(file[i])
        colsData = read_excel(file[i])
        add_excel(i + 1, colsData, savefile)