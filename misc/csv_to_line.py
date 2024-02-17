#!/usr/bin/python3
# .csv į .line konverteris

from influx_line_protocol import Metric
import csv
import datetime

with open('aktyvumas.csv', newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        date=row[0]
        count=0
        epoch=0
        valid=False
        try:
            epoch_ns = int(datetime.datetime.strptime(date, "%Y-%m-%d").timestamp()) * 1000000000
            count=int(row[1])
            valid=True
        except:
            pass
        if (valid):
            metric = Metric("trafikas")
            metric.with_timestamp(epoch_ns)
            metric.add_value('count', count)
            print(metric)
