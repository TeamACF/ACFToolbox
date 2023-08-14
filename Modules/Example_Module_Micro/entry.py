"""
此Module名为Example Module Micro, 你应该也能够理解其含义, 这意味着：
    1.此Module只是个示例
    2.此Module不是什么正式发布的功能性Module
    3.你可以善用此Module, 例如复制粘贴此Module, 从而改出属于你自己的Module
    4.如果你的双亲逝世了, 你可以尝试出售此Module
接下来, 请跟随文档与代码, 熟悉ACFToolbox的Module结构
"""

"""
你目前处于Modules文件夹中的Example_Module_Micro文件夹中的entry.py文件中。让我来给你解释下这一切: 
    Modules文件夹: 用于存储ACFToolbox的所有模块的文件夹, 这基本上就是ACFToolbox的命根子, 删了它你会得到一个没有任何功能 (甚至可能根本没法运行) 的ACFToolbox
    Example_Module_Micro文件夹: 用于存储名为"Example_Module_Micro"的模块的文件夹, 文件夹名称就是模块的名称
    entry.py: 被ACFToolbox默认导入的py文件, 这个模块的一切从这里开始, 此文件被导入后, 会执行其中的start()函数, 然后基本上, 你的模块就发挥作用了。
"""

import dearpygui.dearpygui as dpg #先引入dearpygui，方便操控UI，dpg很重要，基本涉及UI都要用
import sys
sys.path.append("./Core")#增加import路径，不然识别不到
import Core.guiexpress
"""
如果你要新增新的东西, 比如你自己的图片, 请一定要在你自己的模块里放置图片文件, 然后再使用
无论在任何时候, 千 ! 万 ! 不 ! 要 ! 尝试修改ACFToolbox的本体代码 (除非你的修改最终将提交到代码仓库, 或只是供自己修改使用) , 尤其是在当你会把你的模块分享给其它人或会公开发布的时候
因为!!! 请 !!! 绝对不要 !!! 让你的用户 !!! 在使用你的模块之前 !!! 还要对ACFToolbox的本体代码进行修改 !!!
这会导致一些严重的后果, 无论是你还是我们, 都不希望看到"一个没有任何编程基础的小白正在使用WPS修改一个.py文件并且由于打错了一个字母导致程序崩溃随后说你的模块和ACFToolbox都是垃圾"这样的场景
所以无论你懂不懂我的意思, 都千万不要尝试这么去做。
另外, dearpygui不支持在窗口初始化后再去加载更多的字体文件, 所以你是没法导入更多字体的
"""

"""
当然, 你现在应该注意到了，对于ACFToolbox中的任何地方而言, 相对路径的起始点都是ACFToolbox的根目录 (ACFToolbox.py的所在目录) , 所以如果要调用什么文件的话, 请注意这一点。
"""

def testbtn_callback():
    Core.guiexpress.show_info("testbtn_callback","Wow!\nThis is a MessageBox from testbtn_callback!")

#这就是所谓的start函数了，一切从这里开始
def start():
    print("Example_Module Here!")#我们一般会在模块的起始点打印一些信息，这样能够让用户知道自己做了什么，排查起问题来也会方便些
    """
    基本上, 我们没有什么别的是需要做的, 我们已经进到了start()函数内, 并打印了一条信息
    对于UI来说, 主窗口之类的东西ACFToolbox本体已经为我们准备好了, 所以我们只需要创建一个属于我们自己的在dearpygui内的窗口就好了
    就像是这样：
    """
    with dpg.window(label="ExampleModuleWindow") as ExampleModuleWindow:
        ExampleModuleWindow_TopText = dpg.add_text("Example Module Micro Window",label="ExampleModuleWindow_TopText")
        #现在，我们已经创建了一个文本，接着创建一个按钮，并设置callback
        ExampleModuleWindow_TestButton = dpg.add_button(label="Click it~",callback=testbtn_callback)