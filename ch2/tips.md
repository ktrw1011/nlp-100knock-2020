# 11
sedコマンドのタブ扱いはOSによって異なるらしい
https://rcmdnk.com/blog/2016/09/13/computer-gnu-bsd-linux-mac/  

なので`tr`コマンドを使用  
ただし文字列としては置換できない
https://farmedgeek.hateblo.jp/entry/20150223/1424696622  

# 12
一つ目のフィールドを取り出す  
デフォルトのデリミタは`タブ`  
変更したい時は`--delim=`オプション
```sh
cut -f 1
```

# 16
ファイルの分割  
`-l`で行数  
`-n`で個数  
指定
```sh
split -l ファイル 分割後ファイル名の接頭辞
```