#!/usr/bin/env bash
yaf -i capture.pcap —-uniflow —-flow-stats —-idle-timeout 2 —-active-timeout 5 | \
yafscii —-tabular  —-print-header | \
sed 's/ //g' | sed 's/|/,/g' > out.csv && \
python3 analyze.py > out.txt && \
rm out.csv

