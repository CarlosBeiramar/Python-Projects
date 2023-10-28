import json

questions = {}
# store all the data into questions dictionary
with open('data.json', "r") as f:
    data = json.load(f)
    for all_questions in data.values():
        for q in all_questions:
            if q['difficulty'] in questions:
                questions[q['difficulty']].append(q)
            else:
                questions[q['difficulty']] = [q]
f.close


