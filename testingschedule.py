# import time
#
# def print_hello():
#     print("hello")
#
# while True:
#     print_hello()
#     time.sleep(2)

import schedule

def print_hello():
    print("hello")

schedule.every(2).seconds.do(print_hello)

while True:
    schedule.run_pending()