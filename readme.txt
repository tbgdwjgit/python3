 目录：

 注意事项：
包管理必备：Anaconda
强烈推荐 Anaconda ，它能帮你安装好许多麻烦的东西，包括： Python 环境、pip 包管理工具、常用的库、配置好环境路径等等。
这些事情小白自己一个个去做的话，容易遇到各种问题，带来挫败感。如果你想用 Python 搞数据方面的事情，就安装它就好了，
它甚至开发了一套 JIT 的解释器 Numba。所以 Anaconda 有了 JIT 之后，对线上科学计算效率要求比较高的东西也可以搞了。





bug汇总：
1.python中出现SyntaxError: Non-UTF-8 code 解决方法：修改文件编码方式,用UTF-8。
2.ValueError: bad marshal data            解决方法： pip uninstall flask 再安装。
3.IndentationError: unindent does not match any outer indentation level  解决方法： 缩进问题，或者是空格和Tab混用。




为已经检出的项目更换地址
修改项目中 .git/config文件中的[remote "origin"] ，
修改 url 的值为：url = git@.github.com:user_name/repos_name.git
设置完成后, 在这个工程目录 git push 会自动免密提交代码。
user_name 是指定 Github 账户名。