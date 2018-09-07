import datetime
import os
import shutil
import argparse


def main():
    parser = argparse.ArgumentParser(description="Rewrite static file into specific folders.")
    parser.add_argument('-p', '--path', metavar='path', required=True, help='Src path.')
    parser.add_argument('-s', '--start', metavar='start', required=True, help='Start date.')
    parser.add_argument('-e', '--end', metavar='end', required=True, help='End date.')
    args = parser.parse_args()
    src_path, s, e = args.path, args.start, args.end
    path = '/data/hftdata/CryptoExchanges/static/cryptocurrency'
    start = datetime.datetime(int(s.split('/')[0]), int(s.split('/')[1]), int(s.split('/')[2]))
    end = datetime.datetime(int(e.split('/')[0]), int(e.split('/')[1]),
                            int(e.split('/')[2])) + datetime.timedelta(days=1)
    tmp = start
    while tmp != end:
        filepath = '%s/%4d/%02d/%02d' % (path, tmp.year, tmp.month, tmp.day)
        if not os.path.exists(filepath):
            os.makedirs(filepath)
        file = '%s/static_file.csv' % filepath
        if os.path.exists(file):
            os.remove(file)
        shutil.copyfile(src_path, file)
        tmp += datetime.timedelta(days=1)


if __name__ == '__main__':
    main()
