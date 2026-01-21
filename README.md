# mypkg
![test](https://github.com/tadano0504/mypkg/actions/workflows/test.yml/badge.svg)

本リポジトリは千葉工業大学 未来ロボティクス学科 2025年度 ロボットシステム学内で行った内容に基づいて作成された課題提出用リポジトリです。

## 概要
本パッケージは、数値ストリームを3段階（LOW / MID / HIGH）に分類する
汎用的な閾値判定ノードを提供します。
センサ値・スコア・確率など任意の Float32 データに対して使用できます。

## ノード一覧

- talkerノード
- listenerノード

## talkerノード
- 数値データを一定周期で生成します 
- 生成した値を /input_value トピックに送信します  
- メッセージ型は std_msgs/msg/Float32 を使用しています  
## listenerノード
- /input_value トピックを購読します  
- 受信した数値を、あらかじめ設定された基準値と比較します  
- 判定結果を /judge_result トピックとして publish します 
- メッセージ型は std_msgs/msg/String です 
## launchファイル
- talker ノードと listener ノードを同時に起動します。

## テスト環境
- Ubuntu-22.04(WSL2)  
- ROS 2: Humble  
- Python version: 3.10  

## インストール

本パッケージは GitHub から取得できます。

```shell
$ git clone https://github.com/tadano0504/mypkg.git 
```

本パッケージは ROS 2 ワークスペースに配置し、
通常の colcon ビルド手順でビルドしてください。

## 使い方

launch ファイルを使って talker と listener を同時に起動します。
```shell
$ ros2 launch mypkg talk_listen.launch.py
```

出力例
```shell
[listener] [INFO] Received value: 0.42 -> LOW 
[listener] [INFO] Received value: 0.78 -> HIGH 
[listener] [INFO] Received value: 0.55 -> LOW
```

## 著作権・ライセンス
- このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布および使用が許可されています。
- この[README](https://github.com/tadano0504/mypkg/blob/main/README.md)は、[yagikai2112](https://github.com/yagikai2112/mypkg)の[mypkg](https://github.com/yagikai2112/mypkg/blob/main/README.md)(© 2025 yagikai2112)を参考に作られています。
- © 2025 Tadano Keito
