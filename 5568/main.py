import time
from datetime import datetime

def main():
    print("✅ 本地运行成功！")
    print("当前时间:", datetime.now().strftime("%H:%M:%S"))

    # 保持窗口不闪退
    input("\n按回车键退出...")

if __name__ == "__main__":
    main()
