#!/bin/bash
# cutでカラムを取得、sortで並び替えてuniqで重複カウント、再度数値で降順に並び替える
cut -f 1 ./popular-names.txt | sort | uniq -c | sort -n -r