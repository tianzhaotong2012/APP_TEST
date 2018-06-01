# coding=utf-8
import subprocess
import os
import random
import time
from multiprocessing import Pool

def start_app(dev):
    package_name = 'com.tian.news'
    activity_name = '.ui.activity.AdsplashActivity'
    action='adb -s ' + dev + ' shell am start ' + '%s/%s'%(package_name, activity_name)
    print action
    pi= subprocess.Popen(action,shell=True,stdout=subprocess.PIPE)

def stop_app(dev):
    package_name = 'com.tian.news'
    action='adb -s ' + dev + ' shell am force-stop ' + package_name
    print action
    pi= subprocess.Popen(action,shell=True,stdout=subprocess.PIPE)

def get_wm_size(dev):
    action='adb -s ' + dev + ' shell wm size'
    print action
    sizes = subprocess.Popen(
                               action.split(),
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE
                               ).communicate()[0]

    sizeList = sizes.split()
    size = sizeList[2].split('x')
    ret = []
    ret.append(int(size[0]))
    ret.append(int(size[1]))
    return ret

def swipe_to(dev, dis):
    wm_size = get_wm_size(dev)
    W = wm_size[0]
    H = wm_size[1]
    org = 0
    for num in range(0,13):
        x1 = random.randint(W-30,W)
        x2 = random.randint(W-20,W)
        y1 = random.randint(H-300,H-200)
        y2 = random.randint(H-700,H-600)
        print "x1:%d y1:%d x2:%d y2:%d" %(x1, y1, x2, y2)
        action='adb -s ' + dev + ' shell input swipe ' + '%d %d %d %d'%(x1, y1, x2, y2)
        print action
        pi= subprocess.Popen(action,shell=True,stdout=subprocess.PIPE)
        org = org + y1 - y2
        time.sleep( 1 )
        if org > dis:
            break

def click_article_item(dev):
    wm_size = get_wm_size(dev)
    W = wm_size[0]
    H = wm_size[1]
    x= random.randint(W/2-100,W/2+100)
    y =  random.randint(H/2-100,H/2+100)
    action='adb -s ' + dev + ' shell input tap ' + '%d %d'%(x, y)
    print action
    pi= subprocess.Popen(action,shell=True,stdout=subprocess.PIPE)


def go_back(dev):
    action='adb -s ' + dev + ' shell input keyevent 4'
    print action
    pi= subprocess.Popen(action,shell=True,stdout=subprocess.PIPE)

def read(dev):
    wm_size = get_wm_size(dev)
    W = wm_size[0]
    H = wm_size[1]
    dis = random.randint(H*2,H*6)
    swipe_to(dev, dis)
    click_article_item(dev)
    sleep_time = random.randint(3,10)
    time.sleep( sleep_time )
    swipe_to(dev, H*5)
    go_back(dev)


def test_device(dev):
    start_app(dev)
    time.sleep( 10 )

    for num in range(0,10):
        read(dev)
        sleep_time = random.randint( 2, 8 )
        time.sleep( sleep_time )

    time.sleep( 3 )
    stop_app(dev)


devices = subprocess.Popen(
                           'adb devices'.split(),
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE
                           ).communicate()[0]

serial_nos = []
for item in devices.split():
    filters = ['list', 'of', 'device', 'devices', 'attached']
    if item.lower() not in filters:
        serial_nos.append(item)

print serial_nos


#wm_size = get_wm_size(serial_nos[0])
#print wm_size
#exit(0)

p = Pool(4)
for dev in serial_nos:
    print('Parent process %s.' % os.getpid())
    p.apply_async(test_device, args=(dev,))

print('Waiting for all subprocesses done...')
p.close()
p.join()
print('All subprocesses done.')
