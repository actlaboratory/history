# History Module

履歴管理モジュール

# 動作

- コンストラクタで指定した数の履歴を保持
- それを超えてaddされると古いものから削除
- コンストラクタでallowDuplication=trueにしている場合、重複する要素の追加を試みると最新の1つのみを残して古いものを削除
- getPrivious()、getNext()を用いて履歴内を移動可能
- 履歴移動後にadd()すると、それ以降の履歴をすべて破棄してから追加を試みる

## テスト

- python -m unittest discover tests
