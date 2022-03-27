import datetime
import sys
from subprocess import (
    run, PIPE
)


def create_report():
    result = run(["ps", "aux"], stderr=PIPE, stdout=PIPE)
    result = result.stdout.decode().split('\n')
    result.pop(len(result) - 1)
    nfields = len(result[0].split()) - 1
    fin = []
    for row in result[1:]:
        fin.append(row.split(None, nfields))

    user_process = {}
    qty = len(result) - 1
    sum_cpu = 0
    sum_mem = 0
    max_mem = 0
    max_cpu = 0
    max_mem_id = 0
    max_cpu_id = 0
    i = 0

    while i < qty:

        sum_cpu += float(fin[i][2])
        sum_mem += float(fin[i][3])

        if float(fin[i][2]) > max_cpu:
            max_cpu = float(fin[i][2])
            max_cpu_id = i

        if float(fin[i][3]) > max_mem:
            max_mem = float(fin[i][3])
            max_mem_id = i

        if fin[i][0] in user_process.keys():
            user_process[fin[i][0]] += 1
        else:
            user_process[fin[i][0]] = 1

        i += 1

    out = sys.stdout
    file_name = datetime.datetime.now().strftime("%d-%m-%Y-%H:%M") + '-scan.txt'

    with open(file_name, 'w') as f:
        sys.stdout = f
        print('Отчёт о состоянии системы:')
        print(f'Пользователи системы:{[key for key in user_process.keys()]}'.replace('[', '').replace(']', ''))
        print('Процессов запущено:', qty)
        print('Пользовательских процессов:')
        for key, value in user_process.items():
            print(key, ':', value)
        print(f'Всего памяти используется:{round(sum_mem, 1)}%')
        print(f'Всего CPU используется:{round(sum_cpu, 1)}%')
        print(f'Больше всего памяти использует:{fin[max_mem_id][10][:20]}')
        print(f'Больше всего CPU использует:{fin[max_cpu_id][10][:20]}')

    sys.stdout = out
    print(open(file_name).read())


if __name__ == '__main__':
    create_report()
