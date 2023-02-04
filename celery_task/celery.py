import os
from celery import Celery
from django.conf import settings

# 加载django环境
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LuffyAPI.settings.dev')

# broker任务队列
broker = 'redis://:%s@%s:%s/1' % (os.getenv('REDIS_PASSWORD'), settings.REDIS_HOST, settings.REDIS_PORT)
# 结构存储，执行完的结果存在这
backend = 'redis://:%s@%s:%s/2' % (os.getenv('REDIS_PASSWORD'), settings.REDIS_HOST, settings.REDIS_PORT)
app = Celery(__name__, broker=broker, backend=backend, include=[
    'home.task.update_banner_cache'
])

# 执行定时任务
# 时区
app.conf.timezone = 'Asia/Shanghai'
# 是否使用UTC
app.conf.enable_utc = False
# 任务的定时配置
from datetime import timedelta
from celery.schedules import crontab

# app.conf.beat_schedule = {
#     'add-task': {
#         'task': 'home.task.update_banner_cache.update_banner_list',
#         'schedule': timedelta(seconds=5),
#         # 'schedule': crontab(hour=8, day_of_week=1),  # 每周一早八点
#         # 'args': ('', ),
#     }
# }

# 启动celery
# celery -A celery_task worker -l info -P eventlet
# 启动beat
# celery -A celery_task beat -l info

# 延迟执行
"""
# 提交延迟任务
from datetime import datetime, timedelta

from celery_task.task1 import add
from celery_task.task2 import multiply

#  提交异步
# task_id = add.delay(6, 6)
# print(task_id)
# task_id = multiply.delay(6, 6)
# print(task_id)

# 执行延迟任务
# 需要utc时间
eta = datetime.utcnow() + timedelta(seconds=10)
task_id = multiply.apply_async(args=(90, 90), eta=eta)
print(task_id)
"""
# 查看结果
"""
from celery_task.celery import app
from celery.result import AsyncResult

id = '2de7ee1d-c438-4277-8a2c-6c45a4e00454'

if __name__ == '__main__':
    async_result = AsyncResult(id=id, app=app)
    if async_result.successful():
        result = async_result.get()
        print(result)
    elif async_result.failed():
        print('任务失败')
    elif async_result.status == 'PENDING':
        print('任务等待中被执行')
    elif async_result.status == 'RETRY':
        print('任务异常后正在重试')
    elif async_result.status == 'STARTED':
        print('任务已经开始被执行')

"""
