import os
import json


def config_manager():
    config_name = None

    onlyfiles = [f for f in os.listdir("configs") if os.path.isfile(os.path.join("configs", f))]

    list_config(config_name)
    """Todo: create config manager to print out configurations and to be selected by the user"""


def config_file(args):
    config_file_name = "{0}.txt".format(input("Name of Config: "))
    if config_file_name is not None:
        if os.path.isdir('configs') == False:
            os.mkdir('configs')
        else:
            if os.path.isfile(config_file_name) == False:
                open('configs/{0}'.format(config_file_name), 'x')
    with open('configs/{0}'.format(config_file_name), 'a') as config_file:
        arg_dictionary = vars(args)

        config_file.write("{0}\n".format(json.dumps(arg_dictionary)))
        print('Wrote {0} to config file'.format(config_file_name))

        config_file.close()
        print('Configuration File Saved')

    list_config(config_file_name)


def list_config(config_file_name="configs.txt"):
    with open('configs/{0}'.format(config_file_name, 'r')) as config_file:
        configs = []

        print(json.load(config_file))

        print(configs)
