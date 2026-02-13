from jinja2 import Environment, FileSystemLoader
import yaml

ENV = Environment(loader=FileSystemLoader('.'))

template = ENV.get_template("task02_interface_template.j2")


with open("task02_interface_data.yml") as f:
    interfaces = yaml.safe_load(f)
    print(template.render(interface_list=interfaces))