#!/bin/bash
# sort -> unique で隣接文字をカウント
# 再度数値sortでリバース
# 先頭5行を出力
cat ans_45.txt | sort | uniq -c | sort -n -r | head -n 5
echo "============="
cat ans_45.txt | grep '行う' | sort | uniq -c | sort -n -r
echo "============="
cat ans_45.txt | grep 'なる' | sort | uniq -c | sort -n -r
echo "============="
cat ans_45.txt | grep '与える' | sort | uniq -c | sort -n -r