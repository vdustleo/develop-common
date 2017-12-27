import os
import datetime
from functools import reduce
import time


class Metric:
    def __init__(self):
        self.id = ''
        self.name = ''
        self.timestamp = datetime.datetime()
        self.value = ''
        self.scope = ''

class MetricMeta:
    def __init__(self):
        self.id = ''
        self.op_type = ''
        self.op_period = ''

class OpContext:
    def __init__(self):
        self.op_type = None
        self.period = 5
        self.count_pre = None
        self.count_orig = None

class OpResult:
    def __init__(self):
        self.id = ''
        self.value = ''
        self.timestamp = ''
        self.count_orig = ''
        self.value_type = None

OP_TYPE = ( 'avg', 'sum', 'min', 'max', 'count')
OP_PERIOD = ( 5, 30, 60, 60 * 24, 60 * 24 * 7 ) # unit is (minute)

def get_operator(OP_TYPE):
    def avg( metrics ): return sum(metrics) / len(metrics)
    def _sum(metrics): return sum(metrics)
    def _min(metrics): return min(metrics)
    def _max(metrics): return max(metrics)
    def count(metrics): return len(metrics)
    return {'avg': avg, 'sum' : sum, 'min':_min, 'max':_max, 'count' : count}

def process_values( metrics, operator):
    #for one time-type
    for _metric in metrics:
            operator
        # just for one metric
        value = operator(_metric)

metric_to_values = {}
def init_values(metrics):
    global metric_to_values
    # merge data by id's
    for m in metrics:
        L = metric_to_values.setdefault(m.id, [])
        L.append(m)

    # select the data by time-interval
    start_time = time.time()
    end_time = time.time()

    for metric_id in metric_to_values.keys():
        for m in metric_to_values.get(metric_id):
            pass

#process base on the value;
# last time is
becoming_time = int(time.time() / 60 / 30 ) * 30
true_process_time = becoming_time + 2


if __name__ == '__main__':
    print("hello")