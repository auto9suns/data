import sys, json


def python_object_from_file(filepath):
    data = []
    with open(filepath, 'r') as f:
        for line in f:
            data.append(line.strip())
    print (json.dumps(data))


if __name__ == "__main__":
    python_object_from_file(sys.argv[1])
