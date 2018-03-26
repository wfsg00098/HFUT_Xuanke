from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

username = ""

password = ""

classname = "python"

delay = 1

chromedriver = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe"
browser = webdriver.Chrome(chromedriver)
browser.implicitly_wait(30)

try:
    url = "http://my.hfut.edu.cn/login.portal"
    browser.get(url)
except:
    pass


flag = 0
count = 0
while 1:
    print("尝试登录")
    while 1:
        try:
            browser.find_element_by_id("username").send_keys(username)
            browser.find_element_by_id("password").send_keys(password)
            print("输入验证码")
            code = input()
            browser.find_element_by_id("code").send_keys(code)
            break
        except:
            count = count + 1
            print("页面加载失败，刷新重试..." + str(count))
            if browser.current_url == url:
                try:
                    browser.refresh()
                except:
                    pass
            else:
                try:
                    browser.get(url)
                except:
                    pass
            continue

    try:
        browser.find_element_by_xpath("//*[@id=\"loginForm\"]/table[1]/tbody/tr[3]/td/input[1]").click()
        print("登陆成功！")
        flag = 1
    except:
        print("登录失败")

    if flag == 1:
        break

browser.implicitly_wait(120)

try:
    url2 = "http://jxglstu.hfut.edu.cn/eams5-student/wiscom-sso/login"
    browser.get(url2)
except:
    pass
sleep(2)


try:
    url2 = "http://jxglstu.hfut.edu.cn/eams5-student/for-std/course-select/"
    browser.get(url2)
except:
    pass

try:
    browser.find_element_by_xpath("/html/body/div/div[2]/div/div/div[3]/div/h4/a").click()
except:
    pass


try:
    browser.switch_to.window(browser.window_handles[1])
    browser.find_element_by_xpath("//*[@id=\"global_filter\"]").send_keys(classname)
except:
    print("无法输入内容")
    pass

count = 1

select = browser.find_element_by_xpath("//*[@id=\"suitable-lessons-table\"]/tbody/tr/td[10]/button")
browser.execute_script("$(arguments[0]).click()", select)
sleep(1)
while 1:
    message = browser.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/h1").text
    print("第" + str(count) + "次选课：\n\t" + message)
    if message == "选课成功":
        break
    sleep(delay)
    count = count + 1
    browser.execute_script("$(arguments[0]).click()", select)


