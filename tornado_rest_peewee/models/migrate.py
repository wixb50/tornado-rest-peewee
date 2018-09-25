from tornado_rest_peewee.models.base import db
from tornado_rest_peewee.models.tables import Teacher


def create_table(table):
    """
    如果table不存在，新建table
    """
    if not table.table_exists():
        table.create_table()


def drop_table(table):
    """
    table 存在，就删除
    """
    if table.table_exists():
        table.drop_table()


if __name__ == '__main__':
    create_table(Teacher)
    tem = {
        'name': 'zhang',
        'teacher_id': 0,
    }
    with db.atomic():
        for i in range(0, 100):
            tem['teacher_id'] = i
            Teacher.create(**tem)
