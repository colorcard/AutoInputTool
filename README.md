# 自动输入工具使用文档

## 简介
此工具使用 Python 和 Tkinter 库创建了一个简单的自动输入应用。用户可以在应用的文本框中输入或粘贴文本，并点击“开始输入”按钮，程序将模拟键盘输入这些文本。   

可以用来规避例如头歌平台此类**禁止粘贴**的场景，欢迎各位提交 **issue** 和 **Pr**，觉得有用的话留下一个 **Star⭐️** 吧！




## 功能
1. 提供一个文本框，允许用户输入或粘贴文本。
2. 点击“开始输入”按钮后，程序会模拟键盘输入文本框中的内容。
3. 具有 3 秒的延迟，给用户一些准备时间。

## !! 面向小白 !!
如果你不具备进行构建和运行Python脚本的能力，此工具也已经构建了现有的直接可执行程序，请在此进行下载 [Windows & macOS下载](https://github.com/ColorCard/AutoInputTool/releases/tag/%E6%AD%A3%E5%BC%8F%E7%89%88)。

## 环境要求
- Python 3.12 及以上版本
- Tkinter：Python 自带的 GUI 库
- pyautogui：用于模拟键盘输入
- 其他依赖项在 `requirements.txt` 中列出

## 安装与运行

### 1. 安装 Python 和依赖

确保你已经安装了 Python 3.12 或更高版本。如果尚未安装，请访问 [Python 官网](https://www.python.org/downloads/) 下载安装。

克隆此项目并安装所需的依赖：

```bash
git clone <项目仓库地址>
cd <项目目录>
pip install -r requirements.txt
```

### 2. 安装依赖
项目的依赖项包括 `pyautogui` 和 `tkinter`。如果 `tkinter` 没有预装，可以通过以下命令安装：

```bash
pip install pyautogui
```

**注意**：`tkinter` 通常已经包含在标准 Python 安装中，如果遇到缺少问题，请参考 [tkinter 安装指南](https://tkdocs.com/tutorial/install.html)。

### 3. 运行程序
在安装完所有依赖后，运行以下命令启动程序：

```bash
python auto_input_tool.py
```

此命令将启动图形界面，您可以在文本框中输入或粘贴文本并点击“开始输入”按钮。

### 4. 功能使用
- **输入文本**：在文本框中输入或粘贴要模拟输入的文本。
- **开始输入**：点击“开始输入”按钮后，程序会模拟键盘输入文本框中的内容。输入前会有 3 秒的准备时间。

## 生成 Windows 可执行文件（EXE）

如果你需要将此工具打包成独立的 Windows 可执行文件（EXE），可以使用 PyInstaller 进行打包。执行以下命令：

```bash
pyinstaller --onefile --noconsole auto_input_tool.py
```

生成的 EXE 文件将位于 `dist` 目录下。

## 生成 macOS 应用（.app）

如果你在 macOS 上运行此工具，并希望打包成 macOS 应用（.app），同样可以使用 PyInstaller：

```bash
pyinstaller --onefile --windowed auto_input_tool.py
```

生成的 .app 文件将位于 `dist` 目录下。

## 打包与部署

如果你希望在 GitHub Actions 上自动构建和打包 EXE 或 .app 文件，可以使用以下 `build.yml` 工作流文件：

```yaml
name: Build EXE and APP

on:
  push:
    branches:
      - main
  workflow_dispatch:

jobs:
  build_windows:
    runs-on: windows-latest
    steps:
    - name: Checkout code
      uses: actions/checkout@v3
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.12'
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    - name: Install PyInstaller
      run: pip install pyinstaller
    - name: Build EXE for Windows
      run: pyinstaller --onefile --hidden-import pyautogui --noconsole auto_input_tool.py
    - name: Upload Windows EXE artifact
      uses: actions/upload-artifact@v3
      with:
        name: auto-input-tool-exe
        path: dist/auto_input_tool.exe

  build_macos:
    runs-on: macos-latest
    steps:
    - name: Checkout code
      uses: actions/checkout@v3
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.12'
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    - name: Install PyInstaller
      run: pip install pyinstaller
    - name: Build APP for macOS
      run: pyinstaller --onefile --hidden-import pyautogui --windowed auto_input_tool.py
    - name: Upload macOS APP artifact
      uses: actions/upload-artifact@v3
      with:
        name: auto-input-tool-app
        path: dist/auto_input_tool.app
```

## 常见问题

1. **程序未响应或输入错误**：
   - 确保你已正确安装 `pyautogui`。
   - 如果输入内容过长，程序可能会变慢，建议分批次输入。

2. **如何调试 PyInstaller 打包问题**：
   - 如果你遇到 PyInstaller 打包后的问题，可以尝试去掉 `--noconsole` 参数以查看错误日志。

## 许可证
本项目遵循 MIT 许可证。更多信息请查看 [LICENSE](./LICENSE)。