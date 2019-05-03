from threading import Timer

time = 2.0
def hello():
    print('hello, world')
    Timer(time, hello).start()

Timer(time, hello).start() # after 30 seconds, "hello, world" will be printed