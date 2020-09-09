#!/bin/bash
# -n オプションを使用しないと文字列ソートになる
cut -f 3 ./popular-names.txt | sort -n