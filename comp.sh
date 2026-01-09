#!/bin/bash
url="https://raw.githubusercontent.com/datasets/s-and-p-500-companies/refs/heads/main/data/constituents.csv"
echo "company name, location, founding year"
curl -s "$url" |
tail -n +2 |
awk -F',' '{print $2 ", " $5 ", " $NF}' |
sort -t',' -k3
