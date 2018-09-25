# @Author: xiewenqian <int>
# @Date:   2016-08-26T17:54:26+08:00
# @Email:  wixb50@gmail.com
# @Last modified by:   int
# @Last modified time: 2016-09-09T16:41:04+08:00


import logging
import logging.handlers


# 我的日志输入类
class MyCustomLogger:

    logger = None

    levels = {"n": logging.NOTSET,
              "d": logging.DEBUG,
              "i": logging.INFO,
              "w": logging.WARN,
              "e": logging.ERROR,
              "c": logging.CRITICAL}

    log_level = "d"

    @staticmethod
    def getLogger():
        if MyLogger.logger is not None:
            return MyLogger.logger

        MyLogger.logger = logging.Logger("loggingmodule.MyLogger")
        log_handler = logging.StreamHandler()
        log_fmt = logging.Formatter(
            "%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s")
        log_handler.setFormatter(log_fmt)
        MyLogger.logger.addHandler(log_handler)
        MyLogger.logger.setLevel(
            MyLogger.levels.get(MyLogger.log_level))
        return MyLogger.logger

# 输出文件日志类


class MyFileLogger:

    logger = None

    levels = {"n": logging.NOTSET,
              "d": logging.DEBUG,
              "i": logging.INFO,
              "w": logging.WARN,
              "e": logging.ERROR,
              "c": logging.CRITICAL}

    log_level = "d"
    log_file = "my_logger.log"
    log_max_byte = 10 * 1024 * 1024
    log_backup_count = 5

    @staticmethod
    def getLogger():
        if MyFileLogger.logger is not None:
            return MyFileLogger.logger

        MyFileLogger.logger = logging.Logger("loggingmodule.MyFileLogger")
        log_handler = logging.handlers.RotatingFileHandler(
            filename=MyFileLogger.log_file, maxBytes=MyFileLogger.log_max_byte, backupCount=MyFileLogger.log_backup_count)
        log_fmt = logging.Formatter(
            "%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s")
        log_handler.setFormatter(log_fmt)
        MyFileLogger.logger.addHandler(log_handler)
        MyFileLogger.logger.setLevel(
            MyFileLogger.levels.get(MyFileLogger.log_level))
        return MyFileLogger.logger


# 设置使用的日志类
MyLogger = MyCustomLogger

if __name__ == "__main__":
    logger = MyLogger.getLogger()
    logger.debug("this is a debug msg!")
    logger.info("this is a info msg!")
    logger.warn("this is a warn msg!")
    logger.error("this is a error msg!")
    logger.critical("this is a critical msg!")
