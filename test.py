# coding=utf-8
import wda
import time

#bundle_id = 'com.tian.shixunkuaibao'
bundle_id = 'com.jifen.qukan'

c = wda.Client('http://localhost:8100')

s = c.session(bundle_id)


time.sleep( 10 )

s.swipe(301, 420, 289, 93, 0.5)

s.tap(301,410)

time.sleep( 3 )

s.swipe(301, 470, 289, 93, 0.1)

s.swipe(50, 420, 320 , 410, 0.1)

#s.swipe_up()

time.sleep( 5 )

#s.tap(541,671)

#s(name=u'发现', type='Button').tap()

time.sleep( 10 )

s.close()
