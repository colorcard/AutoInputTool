import pyautogui
import tkinter as tk
import time

class AutoInputApp:
    def __init__(self, root):
        self.root = root
        self.root.title("自动输入工具")
        self.root.geometry("600x400")
        self.root.config(bg="#f0f0f0")

        self.label = tk.Label(root, text="自动输入工具", font=("Arial", 18, "bold"), bg="#f0f0f0", fg="#333")
        self.label.pack(pady=20)

        self.info_label = tk.Label(root, text="请在下面的文本框中输入或粘贴文本", font=("Arial", 12), bg="#f0f0f0", fg="#666")
        self.info_label.pack(pady=5)

        self.textbox = tk.Text(root, height=10, width=50, font=("Arial", 12), wrap="word", bg="#ffffff", fg="#333")
        self.textbox.pack(pady=10)

        self.input_button = tk.Button(root, text="开始输入", command=self.start_input, font=("Arial", 14), bg="#4CAF50", fg="white", relief="raised", height=2, width=20)
        self.input_button.pack(pady=15)

        self.bottom_label = tk.Label(root, text="提示：请确保文本框内容格式正确", font=("Arial", 10), bg="#f0f0f0", fg="#999")
        self.bottom_label.pack(pady=10)

    def start_input(self):
        str_in = self.textbox.get("1.0", "end-1c")

        if str_in:
            time.sleep(3)

            str_in = str_in.replace('  ', '')

            # 模拟键盘输入
            pyautogui.typewrite(str_in)

root = tk.Tk()
app = AutoInputApp(root)
root.mainloop()