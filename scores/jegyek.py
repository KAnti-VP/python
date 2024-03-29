import json
import os


def get_json_data(file):
    with open(file, 'r', encoding='utf-8') as f:
        return json.load(f)

def get_dict_from_json(file = 'scores.json'):
    jason = get_json_data(file)
    return jason['scores']

def save_as_json(dic):
    with open('scores.json', 'w', 2) as jf:
        json.dump({'scores': dic}, jf, sort_keys=True)

def reset_json_file():
    save_as_json({})

def scores_to_dict(file):
    with open(file, 'r') as f:
        dic = {}
        end_file = f.seek(0, 2)
        f.seek(0)
        task_number = f.name.split('.')[0]
        max_score = int(f.readline().strip())
        while f.tell() < end_file:
            item = f.readline().strip()
            score = int(f.readline().strip().split()[0])

            if item in dic:
                if task_number in dic[item]:
                    dic[item][task_number] = [score, max_score]
                else:
                    dic[item] = {task_number: [score, max_score]}
            else:
                dic[item] = {task_number: [score, max_score]}
    return dic

def dict_union(dic1, dic2):
    for k in dic2.keys():
        if k in dic1:
            for kk in dic2[k].keys():
                dic1[k].setdefault(kk, dic2[k][kk])
        else:
            dic1[k] = dic2[k]
    return dic1

def add_scores(file):
    json_dict = get_dict_from_json('scores.json')
    scores_dict = scores_to_dict(file)
    dic = dict_union(json_dict, scores_dict)
    save_as_json(dic)

def set_json_file(files):
    reset_json_file()
    for file in files:
        add_scores(file)

def get_sum_max_scores(files):
    max_score = 0
    for file in files:
        with open(file, 'r', encoding='utf-8') as f:
            max_score += int(f.readline().strip())
    return max_score

def get_course_scores(tasks):
    files = tasks_to_files(tasks)
    set_json_file(files)
    dic = get_dict_from_json()
    max_score = get_sum_max_scores(files)
    res = {}
    for k in dic.keys():
        scores = 0
        for kk in dic[k].keys():
            scores += dic[k][kk][0]
        res[k] = round(scores / max_score * 100, 1)
    return res

def tasks_to_files(tasks):
    files = []
    for i in tasks:
        files.append(f'{i}.txt')
    return files

def display_ressults(res):
    import __init__
    students = __init__.diakok
    for k in students.keys():
        # 40 55 70 85
        jegy = 1
        percent = 0.0
        if k in res:
            if res[k] >= 85:
                jegy = 5
            elif 70 <= res[k] < 85:
                jegy = 4
            elif 55 <= res[k] < 70:
                jegy = 3
            elif 40 <= res[k] < 55:
                jegy = 2
            percent = res[k]
        print(f'{students[k].ljust(26)} {str(percent).ljust(5)}% > jegy: {jegy}')


module_get_post = [1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
module_get = [24, 25, 26, 27, 28, 29, 30, 31, 33, 34, 35, 36, 37, 38, 39, 40]
module_secutity = [41, 44, 45, 46, 47, 48, 49, 50, 51]
module_put = [53, 55, 56, 57, 58]
module_delete = [59, 61, 62, 63, 64, 65, 66]
os.chdir(os.getcwd() + '/springboot')

res = get_course_scores(module_delete)
display_ressults(res)