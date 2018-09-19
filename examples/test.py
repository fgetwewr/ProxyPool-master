from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import re
import time

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
browser = webdriver.Chrome(chrome_options=chrome_options)

# browser = webdriver.Chrome()
browser.maximize_window()


browser.get('https://free-proxy-list.net')
# browser.get('http://www.baidu.com')
print(browser.page_source)

ip_address = re.compile(r'<tr role="row" class="odd"><td>(.*?)</td><td>(\d+)</td><td>.*?</td><td class="hm">.*?</td><td>elite proxy</td><td class="hm">.*?</td><td class="hx">.*?</td><td class="hm">.*?</td></tr>', re.S)
re_ip_address = ip_address.findall(browser.page_source)
print(re_ip_address)
'''
for i in range(5):
    print('第%s页' %i)
    browser.get("https://www.xroxy.com/free-proxy-lists/?port=&type=Socks5&ssl=&country=&latency=&reliability=")
    # print(browser.page_source)
    ip_address = re.compile(r'<td tabindex="0" class="sorting_1">(.*?)</td>.*?<td>(\d+)</td>', re.S)
    re_ip_address = ip_address.findall(browser.page_source)
    print(re_ip_address)
    page_next = browser.find_element_by_xpath("//a[text()='2']")
    page_next.get_attribute("href")
    page_next.click()
    time.sleep(2)
browser.quit()
'''


