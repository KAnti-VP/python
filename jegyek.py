import json

def get_json_data(file):
    with open(file, 'r', encoding='utf-8') as f:
        return json.load(f)

def add_scores(file):
    with open(file, 'r') as f:
        dic = get_json_data('scores.json')
        end_file = f.seek(0, 2)
        f.seek(0)
        task_number = int(f.name.split('.')[0])
        max_score = int(f.readline().strip())
        while f.tell() < end_file:
            item = f.readline().strip()
            score = int(f.readline().strip().split()[0])
            #print(item, score)
            if item in dic:
                if task_number in dic[item]:
                    dic[item][task_number] = {task_number: [score, max_score]}
                else:
                    dic[item].append({task_number: [score, max_score]})
            else:
                dic[item] = [{task_number: [score, max_score]}]
        with open('scores.json', 'w', 2) as jf:
            json.dump({'scores': dic}, jf)


#dic = get_json_data('scores.json')
#print(dic)
add_scores('1.txt')
add_scores('2.txt')