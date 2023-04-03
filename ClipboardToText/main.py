import os
import time
import pyperclip


def save_clipboard_image():
    # 現在時刻をファイル名に使用して画像を保存
    timestamp = time.strftime('./work/%Y%m%d_%H%M%S', time.localtime())
    filename = f"{timestamp}.png"

    # クリップボードにコピーされた画像を保存
    os.system(f"pngpaste {filename}")

    print(f"{filename} に画像を保存しました。")

if __name__ == '__main__':
    while True:
        try:
            # 監視間隔を1秒に設定
            time.sleep(1)

            # クリップボードに画像があるかチェック
            clipboard_content = pyperclip.paste()
            if clipboard_content.startswith('PNG'):
                # クリップボードにコピーされた画像を保存
                save_clipboard_image()

                # クリップボードの内容をクリア
                pyperclip.copy('')
            else:
                print("クリップボードに画像がありません。")

        except KeyboardInterrupt:
            break

        except Exception as e:
            print(f"ERR2: {e}")
            pass
