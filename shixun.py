# coding=utf-8
import wda
import time
import random

bundle_id = 'com.tian.shixunkuaibao'

c = wda.Client('http://localhost:8100')

s = c.session(bundle_id)

time.sleep( 10 )

def swipe_article_list( dis ):
    org = 0
    for num in range(0,13):
        x1 = random.randint(150,310)
        x2 = random.randint(150,310)
        y1 = random.randint(350,490)
        y2 = random.randint(90,150)
        print "x1:%d y1:%d x2:%d y2:%d" %(x1, y1, x2, y2)
        s.swipe(x1, y1, x2, y2, 0.1)
        org = org + y1 - y2
        if org > dis:
            break

def click_article_item():
    s.tap(301,410)


def go_back():
    s.swipe(50, 420, 320 , 410, 0.1)


def read():
    dis = random.randint(500,2000)
    swipe_article_list( dis )
    click_article_item()
    time.sleep( 5 )
    swipe_article_list(5000)
    go_back()

def recom_test():
    s(name=u'推荐', type='Button').tap()
    for num in range(0,10):
        read()
        time.sleep( 1 )

#s.tap(541,671)

def explore_test():
    s(name=u'发现', type='Button').tap()
    swipe_article_list( 400 )

    x = random.randint(150,300)
    y = random.randint(100,500)
    s.tap(x,y)

    time.sleep( 3 )

    swipe_article_list( 400 )

    x = random.randint(150,300)
    y = random.randint(100,500)
    s.tap(x,y)

    for num in range(0,10):
        read()
        time.sleep( 1 )

    go_back()
    go_back()

#recom_test()
#explore_test()

print s.window_size()
#s.tap(541,671)
#time.sleep( 3 )
#s.tap(212,671)
#time.sleep( 3 )
#s.tap(159,671)
#time.sleep( 3 )
#s.tap(108,671)
#time.sleep( 3 )
#s.tap(53,671)

recom_test()
explore_test()

time.sleep( 10 )

s.close()
