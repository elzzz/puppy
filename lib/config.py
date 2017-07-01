import sys
import toml
sys.dont_write_bytecode = True


def get_config(conf_path):
    with open(conf_path) as conffile:
        config = toml.loads(conffile.read())
    return config
