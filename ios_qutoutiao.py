# coding=utf-8
import wda
import time
import random

bundle_id = 'com.jifen.qukan'

c = wda.Client('http://localhost:8100')

s = c.session(bundle_id)

time.sleep( 10 )

def swipe_article_list( dis ):
    org = 0
    for num in range(0,13):
        hulueExt = s(name=u'忽略', type='Button').exists
        if hulueExt:
            s(name=u'忽略', type='Button').tap()
        x1 = random.randint(150,280)
        x2 = random.randint(150,280)
        y1 = random.randint(350,490)
        y2 = random.randint(90,150)
        print "x1:%d y1:%d x2:%d y2:%d" %(x1, y1, x2, y2)
        s.swipe(x1, y1, x2, y2, 0.1)
        org = org + y1 - y2
        if org > dis:
            break

def click_article_item():
    s.tap(250,410)


def go_back():
    back1Ext = s(name='home content back', type='Button').exists
    if back1Ext:
        s(name='home content back', type='Button').tap()
        print 'home content back'
        return
    back2Ext = s(name='home content back white', type='Button').exists
    if back2Ext:
        s(name='home content back white', type='Button').tap()
        print 'home content back white'
        return
    back3Ext = s(name=u'完成', type='Button').exists
    if back3Ext:
        s(name=u'完成', type='Button').tap()
        print '完成'
        return
    s.swipe(0, 300, 300, 301, 0.5)
    print 'swipe back'
#s.swipe(50, 420, 320 , 410, 0.1)


def read():
    dis = random.randint(500,2000)
    swipe_article_list( dis )
    click_article_item()
    time.sleep( 5 )
    swipe_article_list(1500)
    go_back()

def recom_test():
    for num in range(0,20):
        read()
        time.sleep( 1 )

#s.tap(541,671)



#recom_test()
#explore_test()

print s.window_size()


recom_test()

time.sleep( 10 )

s.close()
