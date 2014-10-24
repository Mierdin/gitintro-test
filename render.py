#/usr/bin/env python
""" jinja2 demo script

"""

import sys
from jinja2 import Environment, FileSystemLoader
import yaml

ENV = Environment(loader=FileSystemLoader('./'))


def get_config(configfile):
    """Pulls YAML configuration from file and returns dict object"""
    with open(configfile) as _:
        return yaml.load(_)


def gen_snippet(config):
    """Renders a config snippet.
    "config" represents the portion of the YAML
    file applicable to this snippet"""

    template = ENV.get_template("template.j2")
    return template.render(config=config)


def run():
    """Function docstring"""
    try:
        yamlfile = sys.argv[1]
    except IndexError:
        print "Please refer to documentation for proper arguments"
    configdict = get_config(yamlfile)

    #Generate configurations for the core snippets
    print gen_snippet(configdict)

    #TODO: consider doing some kind of check for core stuff before features

if __name__ == "__main__":
    run()
