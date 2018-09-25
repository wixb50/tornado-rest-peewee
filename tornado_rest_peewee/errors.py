# @Author: xiewenqian <int>
# @Date:   2016-10-25T09:46:55+08:00
# @Email:  wixb50@gmail.com
# @Last modified by:   int
# @Last modified time: 2016-10-25T13:46:18+08:00


class BaseError(Exception):
    """base error"""

    def __init__(self, value="Exception"):
        self.value = value

    def __str__(self):
        return repr(self.value)


class TimeoutError(BaseError):
    """server time out"""
    pass
