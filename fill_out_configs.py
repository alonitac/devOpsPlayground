import json

with open('configs/config2.json', 'w') as f:
    json.dump({
        'results': "good job!",
        "results2": '2'
    }, f)


jihadUpdate