import tkinter as tk
import time
from pynput.keyboard import Controller, Key


class AutoInputApp:
    def __init__(self, root):
        self.root = root
        self.root.title("自动输入工具")
        self.root.geometry("600x400")
        self.root.config(bg="#f0f0f0")

        # 初始化键盘控制器
        self.keyboard = Controller()

        self.label = tk.Label(root, text="自动输入工具", font=("Arial", 18, "bold"), bg="#f0f0f0", fg="#333")
        self.label.pack(pady=20)

        self.info_label = tk.Label(root, text="请在下面的文本框中输入或粘贴文本", font=("Arial", 12), bg="#f0f0f0",
                                   fg="#666")
        self.info_label.pack(pady=5)

        self.textbox = tk.Text(root, height=10, width=50, font=("Arial", 12), wrap="word", bg="#ffffff", fg="#333")
        self.textbox.pack(pady=10)

        self.input_button = tk.Button(root, text="开始输入", command=self.start_input, font=("Arial", 14), bg="#4CAF50",
                                      fg="white", relief="raised", height=2, width=20)
        self.input_button.pack(pady=15)

        self.bottom_label = tk.Label(root, text="提示：请确保文本框内容格式正确", font=("Arial", 10), bg="#f0f0f0",
                                     fg="#999")
        self.bottom_label.pack(pady=10)

    def start_input(self):
        str_in = self.textbox.get("1.0", "end-1c")

        if str_in:
            # 显示倒计时提示
            self.bottom_label.config(text="准备中...3秒后开始")
            self.root.update()
            time.sleep(1)
            self.bottom_label.config(text="准备中...2秒后开始")
            self.root.update()
            time.sleep(1)
            self.bottom_label.config(text="准备中...1秒后开始")
            self.root.update()
            time.sleep(1)

            self.bottom_label.config(text="正在输入...")
            self.root.update()

            # 移除多余的空格
            str_in = str_in.replace('  ', '')

            try:
                # 使用pynput逐字符输入文本
                for char in str_in:
                    self.keyboard.type(char)
                    # 可以根据需要添加小延迟，避免输入太快
                    time.sleep(0.01)

                self.bottom_label.config(text="输入完成!")
            except Exception as e:
                self.bottom_label.config(text=f"输入失败: {str(e)}")


root = tk.Tk()
app = AutoInputApp(root)
root.mainloop()
