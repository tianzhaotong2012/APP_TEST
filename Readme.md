https://github.com/facebook/WebDriverAgent
运行xcode
product-> test 或者（cd cd /Users/baidu/Downloads/WebDriverAgent/WebDriverAgent xcodebuild -project WebDriverAgent.xcodeproj -scheme WebDriverAgentRunner -destination "id=06af59e67df49d150a9357b1e5c9718c24c79f7e" test）(设备ID查看方法 终端 instruments -w devices)

iproxy 8100 8100

http://10.11.53.9:8100/status
http://localhost:8100/inspector

Q:如何查找APP的包名？
A:用WebDriverAgent，运行APP，控制台过滤包名


