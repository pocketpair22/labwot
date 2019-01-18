# labwot
研究室スマートホーム化計画で作ったものを入れていきます。

## remote_controller_servient.py
Raspberry Piと[学習リモコン基盤](http://bit-trade-one.co.jp/product/module/adrsir/)を使用したWoT Servient。
赤外線リモコンの機能をAPI化する。
### 使い方
operation_listに操作を追加した物理ボタン順に操作名を追加する。
"operation"キーの値を操作名にしたJSONをPOSTすると、リモコン信号が送出される。
