import logging
from logging.handlers import SMTPHandler
import sys


def main():
    # 1. 创建 logger 实例
    logger = logging.getLogger('test-smtphandler')
    # 2. 设置 logger 实例的日志级别，默认是 logging.WARNING
    logger.setLevel(logging.INFO)

    # 3. 创建 Handler
    # 注意 163 邮箱要求 fromaddr 和你发送邮件的邮箱(即你的邮箱账号)要一致
    mail_handler = SMTPHandler(
        mailhost=('smtp.126.com', 25),
        fromaddr='zyanhe@126.com',
        toaddrs='347834800@qq.com',
        subject='[madmalls.com] 服务器出错了',
        credentials=('zyanhe@126.com', 'ZSIWXRRYTBTWVOZD'))
    # 4. 单独设置 mail_handler 的日志级别为 ERROR
    mail_handler.setLevel(logging.ERROR)


    # 5. 将 Handler 添加到 logger 中
    logger.addHandler(mail_handler)

    # 6. 应用的业务代码(故意出错)
    try:
        x = 1 / 0
    except Exception:
        logger.error('[计算出错了] x = 1 / 0', exc_info=sys.exc_info())


if __name__ == '__main__':
    main()