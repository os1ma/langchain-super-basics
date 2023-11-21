# langchain-super-basics

勉強会「[ChatGPT/LangChain によるチャットシステム構築［実践］入門
](https://forkwell.connpass.com/event/301152/)」で使用したソースコード。

## 依存関係

- Python
- Poetry

バージョンは [.tool-verisons](.tool-versions) に書かれています。

> [!NOTE]
> .tool-verisons は [asdf](https://asdf-vm.com/) の設定ファイルです。

## 実行手順

Python のパッケージは Poetry で管理しています。
以下のコマンドでインストールしてください。

```console
poetry install
```

.env ファイルを以下の内容で作成してください。

```
OPENAI_API_KEY=<your-openai-api-key>
```

各サンプルコードは以下のコマンドで実行できます。

```console
poetry run python src/<ファイル名>
```
