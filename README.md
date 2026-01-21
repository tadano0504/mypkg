# mypkg
![test](https://github.com/tadano0504/mypkg/actions/workflows/test.yml/badge.svg)

本リポジトリは千葉工業大学 未来ロボティクス学科 2025年度 ロボットシステム学内で行った内容に基づいて作成された課題提出用リポジトリです。

## 概要
本パッケージは、数値ストリームを3段階（LOW / MID / HIGH）に分類する
汎用的な閾値判定ノードを提供します。
センサ値・スコア・確率など任意の Float32 データに対して使用できます。

## talkerノード
-数値データを一定周期で生成します 
-生成した値を /input_value トピックに送信します  
-メッセージ型は std_msgs/msg/Float32 を使用しています  
## listenerノード
-/input_value トピックを購読します  
-受信した数値を、あらかじめ設定された基準値と比較します  
-判定結果をログとして出力します  
## launchファイル
- talker ノードと listener ノードを同時に起動します。

## テスト環境
- Ubuntu-22.04(WSL2)  
- ROS 2: Humble  
- Python version: 3.10  

## 実行準備
以下のコマンドでリポジトリを取得し、ビルドを行います。

```shell
$ cd ~/ros2_ws/src 
$ git clone https://github.com/tadano0504/mypkg.git 
$ cd ~/ros2_ws 
$ colcon build 
$ source install/setup.bash
```

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
