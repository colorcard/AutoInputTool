import tkinter as tk
from pykeyboard import *
from pymouse import *
import time

class AutoInputApp:
    def __init__(self, root):
        self.root = root
        self.root.title("自动输入工具")  # 设置窗口标题
        self.root.geometry("600x400")  # 设置窗口大小
        self.root.config(bg="#f0f0f0")  # 设置背景颜色

        # 创建顶部标签
        self.label = tk.Label(root, text="自动输入工具", font=("Arial", 18, "bold"), bg="#f0f0f0", fg="#333")
        self.label.pack(pady=20)

        # 创建说明标签
        self.info_label = tk.Label(root, text="请在下面的文本框中输入或粘贴文本", font=("Arial", 12), bg="#f0f0f0", fg="#666")
        self.info_label.pack(pady=5)

        # 创建文本输入框
        self.textbox = tk.Text(root, height=10, width=50, font=("Arial", 12), wrap="word", bg="#ffffff", fg="#333")
        self.textbox.pack(pady=10)

        # 创建开始输入按钮
        self.input_button = tk.Button(root, text="开始输入", command=self.start_input, font=("Arial", 14), bg="#4CAF50", fg="white", relief="raised", height=2, width=20)
        self.input_button.pack(pady=15)

        # 创建底部提示标签
        self.bottom_label = tk.Label(root, text="提示：请确保文本框内容格式正确", font=("Arial", 10), bg="#f0f0f0", fg="#999")
        self.bottom_label.pack(pady=10)

    def start_input(self):
        """从文本框中获取输入内容并模拟键盘输入"""
        str_in = self.textbox.get("1.0", "end-1c")  # 获取文本框中的内容

        if str_in:
            m = PyMouse()  # 创建鼠标对象
            k = PyKeyboard()  # 创建键盘对象

            time.sleep(3)  # 延迟几秒钟，给用户准备时间

            # 可选：处理文本（例如去除多余的空格）
            str_in = str_in.replace('  ', '')

            # 模拟键盘输入
            k.type_string(str_in)


# 创建主窗口
root = tk.Tk()
app = AutoInputApp(root)

# 运行主事件循环
root.mainloop()