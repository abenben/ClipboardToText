import os
import time

def take_screenshot():
    # 現在時刻をファイル名に使用して画像を保存
    timestamp = time.strftime('./work/%Y%m%d_%H%M%S', time.localtime())
    filename = f"{timestamp}.png"

    # スクリーンショットを撮影して画像を保存
    os.system(f"screencapture -i {filename}")

    print(f"{filename} に画像を保存しました。")

if __name__ == '__main__':
    try:
        take_screenshot()
    except Exception as e:
        print(f"エラーが発生しました: {e}")
