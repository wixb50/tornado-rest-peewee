# @Author: xiewenqian <int>
# @Date:   2016-08-26T17:54:26+08:00
# @Email:  wixb50@gmail.com
# @Last modified by:   int
# @Last modified time: 2017-01-04T09:55:18+08:00


import collections
import copy
import os
import json
import base64
import urllib
import traceback

from errno import EEXIST

from .mylogging import MyLogger

logger = MyLogger.getLogger()


class ReturnData(object):
    def __init__(self, code=200, message='', data=None, total=-1):
        self.code, self.message, self.data, self.total = code, message, data, total

    @property
    def value(self):
        returnMap = {
            "meta": {
                "code": self.code,
                "message": self.message,
                **({'total': self.total} if self.total != -1 else {}),
            },
            "data": self.data,
        }
        return returnMap


def Metrics(fn):
    """获取接口错误处理
    """
    def operater(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except json.decoder.JSONDecodeError:
            return ReturnData(301, 'json格式解析出错')
        except Exception as e:
            logger.error(traceback.format_exc())
            return ReturnData(500, '服务器错误', str(e))
    return operater


def mapUpdate(d, u):
    for k, v in u.items():
        if isinstance(v, collections.Mapping):
            r = mapUpdate(d.get(k, {}), v)
            d[k] = r
        else:
            d[k] = u[k]
    return d


def ensure_directory(path):
    """
    Ensure that a directory named "path" exists.
    """
    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno == EEXIST and os.path.isdir(path):
            return
        raise


def ensure_directory_containing(path):
    """
    Ensure that the directory containing `path` exists.

    This is just a convenience wrapper for doing::

        ensure_directory(os.path.dirname(path))
    """
    ensure_directory(os.path.dirname(path))


def ensure_file(path):
    """
    Ensure that a file exists. This will create any parent directories needed
    and create an empty file if it does not exists.

    Parameters
    ----------
    path : str
        The file path to ensure exists.
    """
    ensure_directory_containing(path)
    open(path, 'a+').close()  # touch the file


def xml_dictify(r, root=False):
    """xml to dict
    """
    if root:
        return {r.tag: xml_dictify(r, False)}
    d = copy.copy(r.attrib)
    if r.text:
        d["_text"] = r.text.strip()
    for x in r.findall("./*"):
        if x.tag not in d:
            d[x.tag] = []
        d[x.tag].append(xml_dictify(x, False))
    return d


def fix_str_len(chunk, length=8):
    chunk = chunk.encode('utf-8')
    return chunk.decode('utf-8') + '\0' * (-len(chunk) % length)
