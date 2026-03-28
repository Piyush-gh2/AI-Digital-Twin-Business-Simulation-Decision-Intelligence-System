import json

def save_memory(data):
    try:
        with open("data/memory.json", "r") as f:
            mem = json.load(f)
    except:
        mem = []

    mem.append(data)

    with open("data/memory.json", "w") as f:
        json.dump(mem, f, indent=4)