from jinja2 import Template

import yaml

with open("task02_interface_data.yml") as f:
    interfaces = yaml.safe_load(f)
    print(Template.render(interface_list=interfaces))