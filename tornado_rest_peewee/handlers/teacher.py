# @Author: xiewenqian <int>
# @Date:   2016-09-07T16:59:36+08:00
# @Email:  wixb50@gmail.com
# @Last modified by:   int
# @Last modified time: 2016-12-20T09:47:12+08:00


import tornado

from playhouse.shortcuts import model_to_dict
from pyrestful import mediatypes
from pyrestful.rest import get, post, put, delete

from .base import unblock, BaseHandler
from tornado_rest_peewee.utils.util import ReturnData, Metrics
from tornado_rest_peewee.models.tables import Teacher
from tornado_rest_peewee.jsons.teacher import TeacherSchema


class TeacherService(BaseHandler):

    # 获取所有
    @get(_path="/teachers", _produces=mediatypes.APPLICATION_JSON)
    @unblock
    @Metrics
    def get_all(self):
        # 排序和分页
        page = int(self.get_argument("p", "0"))
        number = int(self.get_argument("n", "10"))
        query = Teacher.select()
        models = [model_to_dict(x) for x in query.paginate(page, number)]
        return ReturnData(200, '获取数据成功', models, query.count())

    # 获取单个
    @get(_path="/teachers/{sys_id}", _produces=mediatypes.APPLICATION_JSON)
    @unblock
    @Metrics
    def get_one(self, sys_id):
        query = Teacher.get_one(id=int(sys_id))
        if query is None:
            return ReturnData(301, '该用户不存在')
        model = model_to_dict(query)
        return ReturnData(200, '获取数据成功', model)

    # 删除单个
    @delete(_path="/teachers/{sys_id}", _produces=mediatypes.APPLICATION_JSON)
    @unblock
    @Metrics
    def delete_one(self, sys_id):
        query = Teacher.get_one(id=int(sys_id))
        if query is None:
            return ReturnData(301, '该用户不存在')
        if query.delete_instance():
            return ReturnData(200, '删除数据成功')
        else:
            return ReturnData(301, '删除数据失败')

    # 新建单个
    @post(_path="/teachers", _produces=mediatypes.APPLICATION_JSON)
    @unblock
    @Metrics
    def create_one(self):
        teacher_info = tornado.escape.json_decode(self.request.body)
        valiResult = TeacherSchema().validator(teacher_info, 'create')
        if valiResult is not None:
            return ReturnData(301, valiResult)
        try:
            query = Teacher.create(**teacher_info)
        except Exception as e:
            return ReturnData(301, '新增失败', str(e))
        model = model_to_dict(query)
        return ReturnData(200, '新增数据成功', model)

    # 更改单个
    @put(_path="/teachers/{sys_id}", _produces=mediatypes.APPLICATION_JSON)
    @unblock
    @Metrics
    def update_one(self, sys_id):
        sys_id = int(sys_id)
        teacher_info = tornado.escape.json_decode(self.request.body)
        valiResult = TeacherSchema().validator(teacher_info, 'update')
        if valiResult is not None:
            return ReturnData(301, valiResult)
        query = Teacher.update(**teacher_info).where(Teacher.id == sys_id).execute()
        if query:
            model = model_to_dict(Teacher.get_one(id=sys_id))
            return ReturnData(200, '更改数据成功', model)
        else:
            return ReturnData(301, '数据不存在')
