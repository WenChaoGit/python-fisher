"""
created by 朝文天下 on 2018/6/17

"""
import time

__author__ = '朝文天下'
import threading
from werkzeug.local import LocalStack

my_stack = LocalStack()
my_stack.push(1)

print('i am main stack,push后的值为' + str(my_stack.top))


# worker 新线程
def my_worker():
    print('新线程push之前,值是' + str(my_stack.top))
    my_stack.push(2)
    print('新线程push后,值是' + str(my_stack.top))


new_thread = threading.Thread(target=my_worker, name='wen_chao_thread')
new_thread.start()
time.sleep(1)

print('最终,主线程的值是' + str(my_stack.top))
