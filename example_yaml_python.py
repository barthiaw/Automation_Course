import yaml

with open("example.yml") as f:
    result = yaml.load(f, Loader=yaml.FullLoader)
    print(result)
    print(type)