# History Module

履歴管理モジュール


# 動作

- コンストラクタで指定した数の履歴を保持
- それを超えてaddされると古いものから削除
- コンストラクタでallowDuplication=falseにしている場合、重複する要素の追加を試みると最新の1つのみを残して古いものを削除
- getPrivious()、getNext()を用いて履歴内を移動可能
- 履歴移動後にadd()すると、それ以降の履歴をすべて破棄してから追加を試みる


## インストール

- pip install https://github.com/actlaboratory/history/archive/v1.1.0.zip


## テスト

- python -m unittest discover tests


## 変更履歴

- Version 1.1.0 2023.02.01
	- loadFileにオプション「auto_create」を追加
- Version 1.0.3 2020.08.31
	- readmeの誤植を修正
	- loadFile、saveFileを追加
- Version 1.0.2 2020.07.17
	- SyntaxErrorとtestのタイポを修正
- Version 1.0.1 2020.07.15
	- 最大保存件数を0に設定するとadd()でエラーとなる不具合を修正
- Version 1.0.0 2020.07.11
