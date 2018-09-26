md全称markdown
Markdown是一种可以使用普通文本编辑器编写的标记语言，通过简单的标记语法，它可以使普通文本内容具有一定的格式。
当然打开markdown文件最专业的还是markdownPad软件。左边是源码，右边可以看展示效果。



内建函数：
dir()
dir（module）是一个非常有用的指令，可以通过它查看任何模块中所包含的工具。
help()  help(math.pow) 使用方法和相关说明。



代码调试：

一般来说，python下面要么使用log，要么使用pdb。
import logging
logging.basicConfig(filename='123.log',level=logging.INFO)  #允许定义输出信息的级别：debug, info, warning, error,

logging.info("ee")

使用PDB的方式有两种:

1. 单步执行代码,通过命令 python -m pdb xxx.py 启动脚本，进入单步执行模式

2. pdb单步执行太麻烦了，所以第二种方法是import pdb 之后，直接在代码里需要调试的地方放一个
pdb.set_trace()，就可以设置一个断点， 程序会在pdb.set_trace()暂停并进入pdb调试环境，
可以用pdb 变量名查看变量，或者c继续运行


常用命令

命令	        用途
break 或 b	设置断点
continue 或 c	继续执行程序, 或是跳到下个断点
list 或 l	查看当前行的代码段
step 或 s	进入函数
return 或 r	执行代码直到从当前函数返回
exit 或 q	中止并退出
next 或 n	执行下一行
p 或!	        打印变量的值，例如p a
help 或 h	帮助