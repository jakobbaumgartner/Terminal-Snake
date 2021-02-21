import json

def SaveScores(score, size, name):
    data = {}
    with open('data.txt') as json_file:
        data = json.load(json_file)
    
    data.append({
        'name': name, 
        'score': score,
        'size': size
    })

    with open('data.txt', 'w') as outfile:
        json.dump(data, outfile)

def ReadScores():
    with open('data.txt') as json_file:
        data = json.load(json_file)
    
    
    return data

