## selenium


* 显示等待

```

from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Chrome()
driver.get('http://mail.sina.net/login');
el =  WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id("loginfromemail"))
print(el.text)

```
