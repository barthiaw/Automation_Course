from jinja2 import Environment, FileSystemLoader
import yaml

ENV = Environment(loader=FileSystemLoader('.'))

def get_interface_speed(interface_name):
    """ get_interface_speed returns the default Mbps value for a given
        network interface by looking for certain keywords in the name
    """

    if 'gigabit' in interface_name.lower():
        return 1000
    if 'fast' in interface_name.lower():
        return 100

ENV.filters['get_interface_speed'] = get_interface_speed  

template = ENV.get_template("task02_interface_template.j2")

with open("task02_interface_data.yml") as f:
    interfaces = yaml.safe_load(f)
    print(template.render(interface_list=interfaces))