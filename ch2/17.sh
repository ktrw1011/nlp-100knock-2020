#!/bin/bash
# uniqは隣り合った行しかみないので先にsortする
cut -f 1 ./popular-names.txt | sort | uniq