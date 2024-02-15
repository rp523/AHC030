# 1点占い縛り
## 質問した情報として、その地点に油田があるかのboolean情報しか保持しない
過去に質問した情報と矛盾なく配置できるパターンを試し、質問せずとも有無が判明した箇所は質問しない
## 質問した情報として、その地点の油田数も保有する
状態として油田ごとの左上位置を確率ベクトルとして持ち、結果として発言する油田マップはDPする。
そもそもp0と期待値しかやらなくていい。特に期待値はいもすやれば低コストで計算できる。

採択率が低すぎる。10/500程度。もっと貪欲な繊維を目指したい  
gradient方向の更新をかけることで採択率上がったけど、ノイズなしだと不安定。局所解があるとも思えない。油田位置の確率分布の自由度を考慮したらいい？そしたら和が一になる制約が自動的にみたされる。

効果小さいけどやった方がいいこと  
誤回答を覚えておいて2回数誤答しない  
predictと矛盾する回答ださない
greedy演算をいもすで少しだけ高速化  

