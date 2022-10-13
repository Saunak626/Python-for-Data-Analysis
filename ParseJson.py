# Author: shiwq
# CreatTime: 2022-07-16
# FileName: ParseJson
# Description:

from nbformat import read, NO_CONVERT

openfile = '第3章 Python的数据结构、函数和文件'
savefile = 3
codeBlockMode = 0  # 开启代码块模式: 1


with open("{}.ipynb".format(openfile), 'rb') as fp:
    notebook = read(fp, NO_CONVERT)

cells = notebook['cells']
code_cells = [c for c in cells if c['cell_type'] == 'code']

# 打开一个文件
fo = open("{}.py".format(savefile), "w")
# 支持中文注释
fo.write('# coding=gbk\n')

# 读取codecell
for i, cell in enumerate(code_cells):
    if codeBlockMode == 1:
        fo.write('# region codecell {}\n'.format(i))

    fo.write(cell['source'])
    fo.write('\n')

    if codeBlockMode == 1:
        fo.write('# endregion')
        fo.write('\n')

    fo.write('\n')

# 关闭打开的文件
fo.close()
