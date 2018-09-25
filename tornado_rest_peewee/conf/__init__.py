# @Author: xiewenqian <int>
# @Date:   2016-09-08T11:10:44+08:00
# @Email:  wixb50@gmail.com
# @Last modified by:   int
# @Last modified time: 2017-01-11T16:01:25+08:00


"""
配置文件
"""
import configparser
import os
import pytz
import socket

config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'conf.ini'))
profile = os.environ.get('RUN_ENV', 'dev') + '.'


def C(segm, field):
    return config[segm].get(profile + field.lower(), None)


# 自动根据conf生成配置信息
for section in config.sections():
    for key, val in config.items(section):
        if key.startswith(profile):
            globals()['{0}_{1}'.format(section, key.replace(profile, '').upper())] = val

# 系统配置
NOW_LOC = 'Asia/Shanghai'
NOW_TZ = pytz.timezone(NOW_LOC)
HOSTNAME = socket.gethostname()
