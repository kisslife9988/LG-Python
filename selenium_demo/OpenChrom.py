import os
def open_chrome():
    #执行window系统的命令，打开调试模式的窗口
    str = 'chrome --remote-debugging-port=9222'
    os.system(str)
if __name__ == '__main__':
    open_chrome()
