import logging

logging.basicConfig(
    format='%(filename)s[LINE:%(lineno)d]# \
    %(levelname)-8s [%(asctime)s] %(message)s',
    level=logging.DEBUG
)
# debug
# info
# warning
# error
# critical


def fails():
    logging.info('Entered fails')
    1 / 0


try:
    fails()
    # 1 / 0
    # print('Zero')
    # '42' + 10
    # print('Type')
    # [1, 2][2]
    # print('Index')
    # exc = Exception()
    # print(exc)
    # raise exc
except Exception:
    # print('Got Exception', type(e), e.args, type(e.args))
    # logging.error('Got exception %s, %s', type(e), e.args, exc_info=e)
    logging.exception('Got exception')
# print('I\'m working')
# logging.info('Working!')
logging.error('Working!')
# logging.critical('Working!')
# logging.warning('Working!')
# logging.debug('Working!')
