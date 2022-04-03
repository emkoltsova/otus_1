import argparse
import json
import re
import shlex
from os import listdir
from os.path import isdir, isfile


def create_stat(file_name):
    res = []
    ip_dict = {}
    method_dict = {"GET": 0, "POST": 0, "PUT": 0, "DELETE": 0, "HEAD": 0, "CONNECT": 0, "OPTIONS": 0, "TRACE": 0}
    search_exp = "(POST|GET|PUT|DELETE|HEAD|CONNECT|OPTIONS|TRACE)"
    with open(file_name) as file:
        for line in file:
            res_line = shlex.split(line)
            res.append(res_line)
            if res_line[0] in ip_dict.keys():
                ip_dict[res_line[0]] += 1
            else:
                ip_dict[res_line[0]] = 1
            method = re.search(search_exp, res_line[5])
            method_dict[method.group(1)] += 1

    longest_req = [{"ip": req[0],
                    "date": req[3] + ' ' + req[4],
                    "method": re.search(search_exp, req[5]).group(1),
                    "url": req[8],
                    "duration": int(req[10])} for req in sorted(res, key=lambda x: int(x[10]), reverse=True)[:3]]

    result = {
        "total_requests": len(res),
        "total_stat": method_dict,
        "top_ips": dict(sorted(ip_dict.items(), key=lambda x: x[1], reverse=True)[:3]),
        "top_longest": longest_req
    }
    print(f"Statistics for file {file_name}")
    print(json.dumps(result, indent=4))
    with open(file_name[:-4] + "_stat.json", "w") as f:
        f.write(json.dumps(result, indent=4))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', dest='option', action='store', help='Path or log file')
    args = parser.parse_args()

    if isdir(args.option):
        for file in listdir(args.option):
            if file.endswith(".log"):
                create_stat(args.option + file)
            else:
                pass

    elif isfile(args.option):
        create_stat(args.option)
    else:
        print('Nothing to parse!')
