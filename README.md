# mypkg
![test](https://github.com/tadano0504/mypkg/actions/workflows/test.yml/badge.svg)

本リポジトリは千葉工業大学 未来ロボティクス学科 2025年度 ロボットシステム学内で行った内容に基づいて作成された課題提出用リポジトリです。

## CPU負荷チェッカー
CPU の 1分平均負荷 を定期的に取得し、ROS 2 トピック cpu_load に送信するノードです。
1秒ごとに負荷を計測して Float32 型で配信するため、他ノードはこのトピックを購読することで、システムの負荷状況をリアルタイムで監視できます。

## talker.py
- OS の 1分平均 CPU 負荷を定期的に取得します。
- 取得した負荷を cpu_load トピックとして配信します。
## listener.py
- cpu_load トピックを購読します。
- 受信した CPU 負荷をログとして表示します。
## talk_listen.launch.py
- talker ノードと listener ノードを同時に起動します。

## テスト環境
- Ubuntu-22.04(WSL2)  
- ROS 2: Humble  
- Python version: 3.10  

## 実行準備
下記のコマンドを使用し、クローンを行ってください。

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
[listener-2] [INFO] [1766940375.405980169] [listener]: CPU Load: 0.53
[listener-2] [INFO] [1766940376.405980169] [listener]: CPU Load: 0.49
[listener-2] [INFO] [1766940377.405980169] [listener]: CPU Load: 0.51

```

## 著作権・ライセンス
- このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布および使用が許可されています。
- この[README](https://github.com/tadano0504/mypkg/blob/main/README.md)は、[yagikai2112](https://github.com/yagikai2112/mypkg)の[mypkg](https://github.com/yagikai2112/mypkg/blob/main/README.md)(© 2025 yagikai2112)を参考に作られています。
- © 2025 Tadano Keito
