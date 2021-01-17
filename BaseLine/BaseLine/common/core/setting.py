# @Author  : jkl
# @Email   : 189156395@qq.com
# @Time    : 2020/12/25 10:50 上午
# @File    : setting.py
import os
from configparser import ConfigParser
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

parser = ConfigParser()
conf_path = ''

try:
    print(BASE_DIR)
    conf_path = os.path.join(BASE_DIR, "../../../config.ini")
except Exception as e:
    raise ValueError("请检查外部配置文件！！！！！！")

parser.read(conf_path)
default = parser.defaults()


class ToDict:
    def to_dict(self):
        result = dict()
        for key, value in self.__class__.__dict__.items():
            if not key.startswith('__') and not callable(key):
                result[key] = value
        return result


class BaseSetting:
    # mysql对象
    class DefaultMySQL:
        host = default['mariadb_ip']
        port = int(default['mariadb_port'])
        user = default['mariadb_user']
        password = default['mariadb_password']
        name = default['mariadb_db_name']

    # TODO: 后续需要配置 redis MongoDB， 需要的时候再做配置不然会报错
    # redis对象
    # class DefaultRedis(ToDict):
    #     host = default['redis_host']
    #     port = int(default['redis_port'])
    #     password = default['redis_password']
    #     default_db = 1
    #     secondary_db = 2
    #     celery_db = 4
    #     channels_db = 3

    # mongo对象
    # class DefaultMongoDB:
    #     host = parser.get('mongodb', 'host')
    #     port = parser.getint('mongodb', 'port')


class Settings(BaseSetting):
    pass


sys_setting = Settings()
