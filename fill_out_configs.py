import json

with open('configs/config.json', 'w') as f:
    json.dump({
        'results': "good job!"
    }, f)

jihadUpdate