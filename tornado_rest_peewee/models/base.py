from peewee import (
    Model,
    DoesNotExist,
)
from playhouse.db_url import connect

# 初始化数据库
from tornado_rest_peewee.conf import MYSQL_DB
db = connect(MYSQL_DB)


class BaseModel(Model):
    """
    基础类
    可以在此处制定一些大家都需要的列，
    然后每个继承的子类（表）中都会有这么固定的几列
    """

    class Meta:
        """指定数据库."""
        database = db

    @classmethod
    def get_one(cls, *query, **kwargs):
        try:
            return cls.get(*query, **kwargs)
        except DoesNotExist:
            return None
