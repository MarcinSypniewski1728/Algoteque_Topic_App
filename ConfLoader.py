import json

class ConfLoader():
    '''
    Class to handle preparing provider's configuration
    '''
    def __init__(self, conf_file_name):
        '''
        conf_file_name (str): path to the configuration file
        '''
        self.conf_file_name = conf_file_name

    def prepare_provider_conf(self):
        '''
        Load provider's configuration

        return (dict): dictionary containing data of provider's available topics
        '''
        # Get configuration provider's available topics
        with open(self.conf_file_name, 'r') as file:
            conf = json.load(file)
            provider_topics = conf['provider_topics']
            return provider_topics