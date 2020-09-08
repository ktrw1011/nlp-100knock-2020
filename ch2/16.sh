#!/bin/bash
# 行数を計算
# wc -l ./popular-names.txt | cut -f 1 -d ' ' ではダメだった
# どうやら連続するスペースではそこに空行が存在するためらしい
# なのでawkコマンドを使用する
count=`wc -l ./popular-names.txt | awk '{print $1}'`

# 行数を割る(割り算は切り捨てになる)
unit=$(($count / $1))
# 余り
remainder=$(($count % $1))
# gt=grater
if [ $remainder -gt 0 ] ; then
    unit=$(($unit+$remainder))
fi

#行数で分割
split -l $unit ./popular-names.txt ./popular-names.txt.