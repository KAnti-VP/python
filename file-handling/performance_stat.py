import json
import csv


def get_data_from_csv(file: str) -> tuple[list, list]:
    csv_data: list = []
    with open(file, 'r') as f:
        for row in f:
            if row[0].isdigit():
                csv_data.append(list(map(int, row.strip().split(';'))))
            else:
                csv_head = (row.strip().split(';'))
    return csv_data, csv_head


def get_data_from_csv_with_csv(file: str) -> tuple[list, list]:
    csv_data: list = []
    with open(file, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        csv_head = next(csvreader)[0].split(';')
        for row in csvreader:
            csv_data.append(list(map(int, row[0].split(';'))))
    return csv_data, csv_head


def average(arr: list) -> float:
    return sum(arr) / len(arr)


def get_averages(arr: list) -> list:
    result: list = []
    for row in arr:
        result.append(average(row[1:]))
    return result


def print_averages(arr: list) -> None:
    for x in arr:
        print(x)


def difference(aver: float, arr: list) -> list:
    res: list = []
    for x in arr:
        res.append(round(x - aver, 2))
    return res


def get_deviation(aver: list, arr: list) -> list:
    res: list = []
    for i in range(len(arr)):
        res.append(difference(aver[i], arr[i][1:]))
    return res


def print_deviation(work: list, aver: list, diff: list) -> None:
    for i in range(len(work)):
        print('performanve:', end=' ')
        print(" ".join([str(x) for x in work[i][1:]]), end=' ')
        print('average:', aver[i], end=' ')
        print('deviation:', " ".join([str(x).rjust(5) for x in diff[i]]))


def create_csv_file(header: list, perf: list, aver: list, file: str) -> None:
    with open(file[:-4] + '_average.csv', 'w') as f:
        cont: str = ';'.join(header) + ';average\n'
        f.write(cont)
        for i in range(len(perf)):
            line: str = ';'.join([str(x) for x in perf[i]])
            line += ';' + str(aver[i]) + '\n'
            f.write(line)


def create_dictionary(perf: list, aver: list, diff: list) -> list:
    dict_list: list = []
    for i in range(len(perf)):
        dict_list.append({
            'week': perf[i][0],
            'productivity': perf[i][1:],
            'average': aver[i],
            'differences': diff[i]
        })
    return dict_list


def create_json_file(dict_list: list, file: str) -> None:
    with open(file[:-4] + '_data.json', 'w') as f:
        json.dump(dict_list, f, indent=2)


if __name__ == '__main__':
    file_path: str = './source/performance.csv'
    """
    data, head = get_data_from_csv(file_path)
    """
    data, head = get_data_from_csv_with_csv(file_path)
    averages: list = get_averages(data)
    differences: list = get_deviation(averages, data)
    print_deviation(data, averages, differences)
    create_csv_file(head, data, averages, file_path)
    dict_data: list = create_dictionary(data, averages, differences)
    create_json_file(dict_data, file_path)
