import datetime
import time
import pytz
import os
import subprocess

timezone = pytz.timezone('Asia/Shanghai')
base_path = '/home/applezjm/static'
path = '/data/hftdata/CryptoExchanges/static/cryptocurrency'
tmr = datetime.datetime.fromtimestamp(time.time(), timezone)
base_filepath = '%s/%4d/%02d/%02d' % (base_path, tmr.year, tmr.month, tmr.day)
filepath = '%s/%4d/%02d/%02d' % (path, tmr.year, tmr.month, tmr.day)
if not os.path.exists(filepath):
    os.makedirs(filepath)

subprocess.call('scp applezjm@47.75.121.181:%s/static_file.csv %s/'
                % (base_filepath, filepath), shell=True)

