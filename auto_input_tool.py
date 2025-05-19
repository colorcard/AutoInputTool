import tkinter as tk
import time
import pyperclip  # 用于访问剪贴板
from pynput.keyboard import Controller, Key, Listener, KeyCode


class AutoInputApp:
    def __init__(self, root):
        self.root = root
        self.root.title("自动输入工具")
        self.root.geometry("600x450")  # 稍微增加高度以容纳新内容
        self.root.config(bg="#f0f0f0")

        # 初始化键盘控制器
        self.keyboard = Controller()

        # 热键监听状态
        self.ctrl_pressed = False
        self.shift_pressed = False

        # 创建键盘监听器
        self.listener = Listener(on_press=self.on_press, on_release=self.on_release)
        self.listener.start()

        self.label = tk.Label(root, text="自动输入工具", font=("Arial", 18, "bold"), bg="#f0f0f0", fg="#333")
        self.label.pack(pady=20)

        # 添加快捷键说明
        self.shortcut_label = tk.Label(root, text="快捷键: Ctrl+Shift+V - 直接从剪贴板读取并输入",
                                       font=("Arial", 12), bg="#f0f0f0", fg="#0066cc")
        self.shortcut_label.pack(pady=5)

        self.info_label = tk.Label(root, text="请在下面的文本框中输入或粘贴文本", font=("Arial", 12), bg="#f0f0f0",
                                   fg="#666")
        self.info_label.pack(pady=5)

        self.textbox = tk.Text(root, height=10, width=50, font=("Arial", 12), wrap="word", bg="#ffffff", fg="#333")
        self.textbox.pack(pady=10)

        self.input_button = tk.Button(root, text="开始输入", command=self.start_input, font=("Arial", 14), bg="#4CAF50",
                                      fg="white", relief="raised", height=2, width=20)
        self.input_button.pack(pady=15)

        self.bottom_label = tk.Label(root, text="提示：使用快捷键或文本框输入", font=("Arial", 10), bg="#f0f0f0",
                                     fg="#999")
        self.bottom_label.pack(pady=10)

        # 当窗口关闭时停止监听
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_press(self, key):
        # 检测Ctrl和Shift键是否被按下
        if key == Key.ctrl_l or key == Key.ctrl_r:
            self.ctrl_pressed = True
        elif key == Key.shift_l or key == Key.shift_r:
            self.shift_pressed = True
        # 检测V键并执行操作
        elif (key == KeyCode.from_char('v') or key == KeyCode.from_char(
                'V')) and self.ctrl_pressed and self.shift_pressed:
            self.clipboard_input()

    def on_release(self, key):
        # 重置键的状态
        if key == Key.ctrl_l or key == Key.ctrl_r:
            self.ctrl_pressed = False
        elif key == Key.shift_l or key == Key.shift_r:
            self.shift_pressed = False

    def clipboard_input(self):
        """从剪贴板读取内容并自动输入"""
        try:
            # 获取剪贴板内容
            clipboard_text = pyperclip.paste()
            if clipboard_text:
                # 显示状态
                self.bottom_label.config(text="正在从剪贴板读取并输入...")
                self.root.update()

                # 给用户时间切换到目标窗口
                time.sleep(1)

                # 移除多余的空格
                clipboard_text = clipboard_text.replace('  ', '')

                # 逐字符输入
                for char in clipboard_text:
                    self.keyboard.type(char)
                    time.sleep(0.01)  # 小延迟避免输入太快

                self.bottom_label.config(text="剪贴板内容输入完成!")
            else:
                self.bottom_label.config(text="剪贴板为空，没有可输入的内容!")
        except Exception as e:
            self.bottom_label.config(text=f"输入失败: {str(e)}")

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

    def on_closing(self):
        """窗口关闭时的清理工作"""
        if self.listener:
            self.listener.stop()
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = AutoInputApp(root)
    root.mainloop()
