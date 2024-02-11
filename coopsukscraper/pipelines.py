import requests
from datetime import date
import urllib.parse
import os
import yaml


class WriteToFilesPipeline(object):


    def process_item(self, item, spider):
        with open(os.path.join("events", item['id']+".yaml"), "w") as fp:
            fp.write(yaml.dump(item['data']))
