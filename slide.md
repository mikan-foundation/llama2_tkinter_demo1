---
marp: true
theme: default
header: "**Llama2でチャットアプリを作るハンズオン by未完Labo**"

size: 16:9
paginate: true

style: |
    section.title {
        --title-height: 130px;
        --subtitle-height: 70px;

        overflow: visible;
        display: grid;
        grid-template-columns: 1fr;
        grid-template-rows: 1fr var(--title-height) var(--subtitle-height) 1fr;
        grid-template-areas: "." "title" "subtitle" ".";
    }
    section.title header{
        color:white;
    }
    section.title h1,
    section.title h2 {
        margin: 0;
        padding: 0;
        text-align: center;
        height: var(--area-height);
        line-height: var(--area-height);
        font-size: 92px;
        color: white;

        border: 1px dashed gray; /* debug */
    }

    section.title h1 {
        grid-area: title;
        --area-height: var(--title-height);
    }

    section.title h2 {
        grid-area: subtitle;
        --area-height: var(--subtitle-height);
    }

    section {
        justify-content: start;
    }
    

---
<!-- _class: title -->

# 
![bg](Llama2ハンズオンサムネイル.png)

<!--
_color: black
-->
---

# 今日のイベントについて

最近話題の言語モデルとTkinterというライブラリを使ってチャットアプリを作ろう！という勉強会です。

全2回でこの第1回は言語モデルを自分のパソコンで動かし、かつTkinterを触ることができるというのがゴールになります。

第2回では第1回で学んだことを活かしてAIとの対話形式のチャットアプリを作っていきます。

本日のイベントは北海道でITエンジニアを目指すU-25のためのコミュニティ未完Laboが主催します

---
# 未完Laboについて
「技術で地域を良くする。」がコンセプトの未完Foundationが運営する、北海道・札幌のITに関わる全てのU-25のためのオンラインコミュニティです。

「技術を学ぶためには、まずは技術で遊び・研究・探求すること」をモットーに「技術を学び、技術で遊ぶ」というコンセプトで運勢されています。

---

# 自己紹介

#### 岩本宙士
#### Twitter:@Iwamoto_eng

 pythonでbotや管理システム・小規模なAIアプリを作成

 バックエンドが好き、データ・AI大好き

 別で生成AIコミュニティのマネージャーもしてます

![bg right](profile_image.jpg)

---

# LLMとは？
・大規模言語モデルという意味

多くのテキストデータから学習して文章を生成するAIモデル

・なぜ最近話題なのか？

自然な応答、問題発言をしない、使いやすいインターフェースのアプリ

このハンズオンでは使いやすいインターフェースの凄さとchatGPTの精度の高さを実感出来ます

Llama2はMetaとMicrosoftが開発したLLM


---
# 何故Llama2？

・オープンソースで誰でも使えて商用利用も可能


・最近の言語モデルのトレンドは大規模化、その中でノートパソコンでも動かせる軽めの言語モデル



| モデル名| パラメータ数|
|---------|-------------|
| GPT-4   | 100兆       |
| Bing AI | 1兆         |
| GPT-3   | 1750億      |


---
# Tkinterとは？

### GUIアプリケーションを作ることができるPythonの標準ライブラリ
TkinterでGUIアプリを作るときは

1.アプリ画面を作成
2.画面にボタンやフレームなどの部品を描画
3.mainloopメソッドで２をループし続ける
挿入図イメージ
![width:600px](image-1.png)

---
# Tkinterでチャットアプリを作るために必要な機能

<!-- _class: image -->

![width:500](llama2app.png)
1.メッセージ表示機能
2.メッセージ入力機能
3.ステータス表示機能
4.メッセージ送信機能
<!-- 横並びにしたい -->

---
# 開発環境を準備しよう

1.好きな場所に今日の作業フォルダを作成する
2.作成したフォルダをVSCodeで開く
3.VSCodeの Terminal > New Terminal からターミナルを開く
4.python -m venv .venv を実行します
5.Mac / Windowsで以下のコマンドを実行してください
Mac .venv/bin/activate Windows .venv/Scripts/activate

---
# 開発環境を準備しよう
1.VSCode上でmain.pyを作成
2.画面の右上を確認して以下のような表記があればOK
![](python_env_image.png)
3.でなければ、拡張機能を左のメニューのExtensionsからインストール
![](extensions_image.png)

---

# Llama2のモデルのダウンロードと環境構築

1.discordに送信したLlama2ライセンスのコピーを読んでください
2.discordに送信したモデルのダウンロードリンクからダウンロードしてください
3.VSCodeのターミナルから以下のコマンドを実行してください
pip install llama2-cpp-python

---

# 早速Llama2モデルを動かそう

![width:1200px](program1.png)

これだけでLlama2を動かして文章を生成することができます

---

# Tkinterでテキストを表示する

---

# ボタンの機能をつける

---