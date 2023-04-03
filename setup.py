from setuptools import setup, find_packages

setup(
    name='ClipboardToText',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pyperclip'
    ],
    entry_points={
        'console_scripts': [
            'clip_to_text = ClipboardToText.main:main'
        ]
    }
)
