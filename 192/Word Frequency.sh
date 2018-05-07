# /usr/bin/python
# coding: utf-8


# Read from the file words.txt and output the word frequency list to stdout.
# Solution 1
cat words.txt | tr -s ' ' '\n' | sort | uniq -c | sort -nr | awk '{print $2, $1}'
# Solution 2
awk '{for (i=1;i<=NF;i++) {++D[$i];}} END {for (i in D) {print i, D[i]}}' words.txt | sort -nr -k 2