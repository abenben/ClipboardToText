# 画像スクリーンキャプチャ

---

# セットアップ方法

```bash
$ tree ./ -I "*venv|*.git|*.idea|work|__pycache__"
./
├── ClipboardToText
│   ├── __init__.py
│   ├── main.py
│   └── test.py
├── README.md
├── requirements.txt
└── setup.py

2 directories, 6 files

$ pip install -e .    
Obtaining file:///Users/k.abe/PycharmProjects/ClipboardToText
  Preparing metadata (setup.py) ... done
Requirement already satisfied: pyperclip in ./venv/lib/python3.10/site-packages (from ClipboardToText==0.1) (1.8.2)
Installing collected packages: ClipboardToText
  Running setup.py develop for ClipboardToText
Successfully installed ClipboardToText-0.1

$ clip_to_text
Text from clipboard: clip_to_text
```

# アンインストール方法

```bash
$ pip uninstall ClipboardToText
Proceed (Y/n)? y       
  Successfully uninstalled ClipboardToText-0.1
```

# インストールの確認方法

```bash
pip list
```

# （補足）treeコマンドで確認する

MacOSにtreeコマンドをインストールする

```bash
brew install tree
```

```bash
 tree ./ -I "*venv|*.git|*.idea|work|__pycache__"
```