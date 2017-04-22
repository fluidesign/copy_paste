#! python
# config manager module use to :
# 1. load user configuration if such saved.
# 2. In case of empty configuration create default

try:
    import configparser
except ModuleNotFoundError:
    print("We were not able to load the required module when running : " + __name__)
    exit()

config_file_name = "copy_paste.cfg"


def get_config_value(section, key):
    global config_file_name
    try:
        config = configparser.ConfigParser()
        config.read(config_file_name)
        value = config[section][key]
        return value
    except (configparser.NoSectionError, configparser.NoOptionError) as error:
        print("We couldn't find this key " + key)
        print("error" + error)
        return None


def create_config(config):
    config['app-control'] = {}
    config['app-control'] = { 'safe_close_keystroke': 'ctrl-alt-a', 'number_of_clipboard_values_to_save': '10',
    'open_clipboard_list_keystroke': 'ctrl-z', 'save_clipboard_keystroke': 'ctrl-x'}
    with open(config_file_name, 'w') as configfile:
        config.write(configfile)


def verify_config_exist():
    global config_file_name
    config = configparser.ConfigParser()
    try:
        with open(config_file_name) as config_file:
            config.read_file(config_file)
    except IOError:
        print("Config file not found or invalid, creating new")
        create_config(config)


def main():
    verify_config_exist()
    
if __name__ == "__main__":
    print("This module executed only when imported")
    exit(2)
else:
    print(__name__ + " Loaded")
    main()