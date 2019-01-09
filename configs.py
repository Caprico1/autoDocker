import os
import json


def config_manager():
    # TODO: create config manager to print out configurations and to be selected by the user
    config_name = None
    configs = [f for f in os.listdir("configs") if os.path.isfile(os.path.join("configs", f))]

    if len(configs) == 0:
        print("No Configurations saved.\n"
              "Use --config to save a configuartion")
    else:
        print("Configurations")
        config_args = {}
        config_number = 0
        for config in configs:
            config_number += 1
            print("\t{0} - {1}".format(config, config_number))

        config_selection = input("Select a Config: ")

        with open('configs/' + configs[int(config_selection ) - 1]) as config_file:
            json_config = json.load(config_file)


            for key, value in json_config.items():
                config_args[key] = value
        return config_args



def config_file(args):
    config_file_name = "{0}.txt".format(input("Name of Config: "))
    if config_file_name is not None:
        if os.path.isdir('configs') == False:
            os.mkdir('configs')
        else:
            if os.path.isfile(config_file_name) == False:
                open('configs/{0}'.format(config_file_name), 'x')
    with open('configs/{0}'.format(config_file_name), 'a') as config_file:
        arg_to_be_saved = {}
        arg_dictionary = vars(args)
        arg_to_be_saved = arg_dictionary

        #remove config arguments from saved configuration

        #write to configuration file
        config_file.write("{0}\n".format(json.dumps(arg_to_be_saved)))
        print('Wrote {0} to config file'.format(config_file_name))

        config_file.close()
        print('Configuration File Saved')

    list_config(config_file_name)


def list_config(config_file_name="configs.txt"):
    with open('configs/{0}'.format(config_file_name, 'r')) as config_file:
        configs = []

        print(json.load(config_file))

        print(configs)

def load_config(config_file_name):
    config_file = json.load(config_file_name)

    return config_file

