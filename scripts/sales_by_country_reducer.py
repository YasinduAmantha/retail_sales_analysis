#!/usr/bin/env python3
import sys

# country_sales = defaultdict(float)

current_tag = None
current_count = 0

for line in sys.stdin:
    tag, count = line.strip().split("\t")
    count = float(count)

    if current_tag == tag:
        current_count += count
    else:
        if current_tag:
            print(f"{current_tag}\t{current_count}")
        current_tag = tag
        current_count = count

if current_tag:
    print(f"{current_tag}\t{current_count}")
