# %%
import io
import os
import os.path
import traceback
from typing import Union
import sys
import jsonpickle
import selenium.common.exceptions
# from IPython.display import clear_output
import pandas as pd
import pickle
import matplotlib as plt0
from matplotlib import pyplot as plt
import seaborn as sns
from re import RegexFlag
# import pyautogui as pyautogui
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import time
import re
import json
import putils
import copy
from enum import Enum
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
# %mathplotlib inline
from webdriver_manager.firefox import GeckoDriverManager
import requests
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import platform
from urllib.parse import urlparse
from dataclasses import dataclass
import random
import argparse

os_name = platform.system()
os_windows = False
os_linux = False
os_darwin = False

if os_name == "Windows":
    os_windows = True
elif os_name == "Linux":
    os_linux = True
elif os_name == "Darwin":
    os_darwin = True
os_name = os_name.lower()

# %%
""" class InstagramAccount:
    def __init__(self, username, password):
        igbot.username = username
        igbot.password = password
        igbot.cookies = []

    def say_hello(self):
        print('hello!')
"""



class Proxy0:
    def __init__(self, type, ip, port):
        self.type = type
        self.ip = ip
        self.port = port
        self.ping = 0

    def say_hello(self):
        print('hello!')

    def __str__(self):
        return f"Proxy0(type={self.type}, ip={self.ip}, port={self.port}, ping={self.ping})"
    
def extract_domain(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    return domain


def test_proxies0(all_proxies, url_output=False, randomize = False, timeout = 3):

    if isinstance(all_proxies, Proxy0):
        all_proxies = [all_proxies]

    if randomize:
        random.shuffle(all_proxies)

    for index, proxy in enumerate(all_proxies):
        print(f'{index+1}/{len(all_proxies)}  ')

        if proxy.type == "http":
            proxies = {
                'http': f"http://{proxy.ip}:{proxy.port}",
                'https': f"http://{proxy.ip}:{proxy.port}",
            }
        elif proxy.type == "socks":
            proxies = {
                'http': f"socks5://{proxy.ip}:{proxy.port}",
                'https': f"socks5://{proxy.ip}:{proxy.port}",
            }
            # socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, proxy.ip, int(proxy.port))
            # socket.socket = socks.socksocket
            # proxies = None
        else:
            proxies = {
                'http': f"{proxy.type}://{proxy.ip}:{proxy.port}",
                'https': f"{proxy.type}://{proxy.ip}:{proxy.port}",
            }

        try:
            start_time = time.time()
            response = requests.get(Urls.ipify, proxies=proxies, timeout=timeout)
            end_time = time.time()
            proxy.ping = int(1000 * (end_time - start_time))
            if url_output:
                print(response.text)
            print(f"Proxy {proxy.ip}:{proxy.port} - Ping: {proxy.ping:.2f} ms")
        except Exception as e:
            print(f"Proxy {proxy.ip}:{proxy.port} - Error: {e}")
            proxy.ping = -1

def get_args():
    parser = argparse.ArgumentParser(description='Parse command line arguments')
    parser.add_argument('args', metavar='args', type=str, nargs='+', help='args')
    args = parser.parse_args()

    return args.args

class Element0:
    def __init__(self, by, query):
        self.by = by
        self.query = query


class Elements:
    html_body = Element0(By.TAG_NAME, "body")
    instagram_login_username = Element0(By.XPATH, "//input[@class='_aa4b _add6 _ac4d _ap35'][@type='text'][@name='username']")
    instagram_login_password = Element0(By.XPATH, "//input[@class='_aa4b _add6 _ac4d _ap35'][@type='password'][@name='password']")
    instagram_login_button = Element0(By.XPATH, "//button[@class=' _acan _acap _acas _aj1- _ap30'][@type='submit']")
    instagram_login_button_small_top_right = Element0(
        By.XPATH,
        "//a[@class='x1i10hfl xjqpnuy xa49m3k xqeqjp1 x2hbi6w x972fbf xcfux6l x1qhh985 xm0m39n xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli xexx8yu x18d9i69 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1q0g3np x1lku1pv x1a2a7pz x6s0dn4 xjyslct x1lq5wgf xgqcy7u x30kzoy x9jhf4c x1ejq31n xd10rxx x1sy0etr x17r0tee x9f619 x9bdzbf x1ypdohk x1f6kntn xwhw2v2 x10w6t97 xl56j7k x17ydfre x1swvt13 x1pi30zi x1n2onr6 x2b8uid xlyipyv x87ps6o x14atkfc xcdnw81 x1i0vuye x1tu34mt xzloghq xe81s16 x3nfvp2'][text()='Log In']",
    )
    instagram_button_save_info = Element0(By.XPATH, "//button[@class='_acan _acap _acas _aj1- _ap31' and @type='button']")
    instagram_left_menu = Element0(By.XPATH, "//div[@class='x1iyjqo2 xh8yej3']")
    instagram_button_not_now = Element0(By.XPATH, "//button[@class='_a9-- _ap36 _a9_1' and text()='Not Now']")
    instagram_something_went_wrong = Element0(
        By.XPATH,
        "//span[@class='x1lliihq x1plvlek xryxfnj x1n2onr6 x193iq5w xeuugli x1fj9vlw x13faqbe x1vvkbs x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x1i0vuye x1ms8i2q xo1l8bm x5n08af x4zkp8e xw06pyt x10wh9bi x1wdrske x8viiok x18hxmgj'][contains(text(), 'Something went wrong')]",
    )
    instagram_page_not_available = Element0(
        By.XPATH,
        "//span[@class='x1lliihq x1plvlek xryxfnj x1n2onr6 x193iq5w xeuugli x1fj9vlw x13faqbe x1vvkbs x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x1i0vuye x133cpev x1s688f x5n08af x2b8uid x4zkp8e x41vudc x10wh9bi x1wdrske x8viiok x18hxmgj'][contains(text(), 'Sorry')]",
    )

    instagram_some_page_username = Element0(
        By.XPATH,
        "//h2[@class='x1lliihq x1plvlek xryxfnj x1n2onr6 x193iq5w xeuugli x1fj9vlw x13faqbe x1vvkbs x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x1i0vuye x1ms8i2q xo1l8bm x5n08af x10wh9bi x1wdrske x8viiok x18hxmgj']",
    )

    instagram_account_3_dot_menu = Element0(
        By.XPATH,
        "//div[@class='x1i10hfl x972fbf xcfux6l x1qhh985 xm0m39n x9f619 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz x6s0dn4 xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x1ypdohk x78zum5 xl56j7k x1y1aw1k x1sxyh0 xwib8y2 xurb0ha xcdnw81'][@role='button']",
    )

    instagram_report_red_button = Element0(
        By.XPATH,
        "//button[@class='_a9-- _ap36 _a9-_'][text()='Report']"
    )

    instagram_report_account_button = Element0(
        By.XPATH,
        "//div[@class='x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1n2onr6 x1plvlek xryxfnj x1iyjqo2 x2lwn1j xeuugli xdt5ytf xqjyukv x1qjc9v5 x1oa3qoh x1nhvcw1'][text()='Report Account']"
    )

    instagram_report_options = Element0(
        By.XPATH,
        "//div[@class='x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh xyamay9 x1pi30zi x1l90r2v x1swvt13 x1n2onr6 x1plvlek xryxfnj x1c4vz4f x2lah0s x1q0g3np xc26acl x6s0dn4 x1oa3qoh x1nhvcw1']"
    )

    instagram_report_radio_buttions = Element0(
        By.XPATH,
        "//div[@class='x1i10hfl xjbqb8w xjqpnuy xa49m3k xqeqjp1 x2hbi6w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619 xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 x16tdsg8 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1o1ewxj x3x9cwd x1e5q0jg x13rtm0m x1q0g3np x87ps6o x1lku1pv x1a2a7pz x6s0dn4 x1ypdohk x78zum5 xh8yej3']"
    )

    instagram_report_submit_button = Element0(
        By.XPATH,
        "//button[@class=' _acan _acap _acas _aj1- _ap30'][@type='button'][text()='Submit report']"
    )

    instagram_report_close_button = Element0(
        By.XPATH,
        "//button[@class=' _acan _acap _acas _aj1- _ap30'][@type='button'][text()='Close']"
    )

    instagram_report_block_button_1 = Element0(
        By.XPATH,
        "//div[@class='x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1n2onr6 x1plvlek xryxfnj x1iyjqo2 x2lwn1j xeuugli xdt5ytf xqjyukv x1qjc9v5 x1oa3qoh x1nhvcw1'][contains(text(), 'Block ')]"
    )

    instagram_report_block_button_2 = Element0(
        By.XPATH,
        "//button[@class='xjbqb8w x1qhh985 xcfux6l xm0m39n x1yvgwvq x13fuv20 x178xt8z x1ypdohk xvs91rp x1evy7pa xdj266r x11i5rnm xat24cr x1mh8g0r x1wxaq2x x1iorvi4 x1sxyh0 xjkvuk6 xurb0ha x2b8uid x87ps6o xxymvpz xh8yej3 x52vrxo x4gyw5p xkmlbd1 x1xlr1w8'][text()='Block']"
    )


class Urls:
    insta_main = 'https://www.instagram.com/'
    insta_login = 'https://www.instagram.com/accounts/login/'
    insta_dummy = 'https://www.instagram.com/1/2/3/'
    google = 'https://www.google.com'
    ipify = 'https://api.ipify.org'

    @staticmethod
    def some_page(page_id):
        return f'https://www.instagram.com/{page_id}/'


class IGBot:
    def __init__(self):
        pass

    def organize_accounts(self, input_file_path: str, output_file_path: str, randomizer=False):
        accounts_organized = list()
        with open(input_file_path, 'r', encoding='utf8') as input_file:
            i = 0
            for line in input_file:
                line = line.strip()
                if line:
                    if i % 2 == 0:
                        username = line
                    else:
                        password = line
                        accounts_organized.append([username, password])
                    i += 1

        if randomizer:
            random.shuffle(accounts_organized)
            
        putils.write_list(output_file_path, accounts_organized)

    # def process_accounts(self, input_file_path: str):

    # def read_accounts(self):
    # self.accounts = putils.read_obj(os.path.join(self.working_dir, 'accounts.json'))

    def organize_proxies(self, proxy_type, input_file_path, output_file_path=None) -> list[Proxy0]:
        proxies = []
        with open(input_file_path, 'r', encoding='utf8') as file:
            for line in file:
                line = line.strip()
                ip, port = line.strip().split(':')
                proxy = Proxy0(proxy_type, ip, port)
                proxies.append(proxy)
        if output_file_path:
            putils.write_list(output_file_path, proxies)
        return proxies

    def read_proxies(self, file_path):
        self.proxies : list[Proxy0]= putils.read_list(file_path)
        return self.proxies

    def read_cookies(self, file_path):
        self.cookies : list= putils.read_list(file_path)
        return self.cookies

    def process_proxies(self, proxy_type, input_file_path, output_file_path):
        proxies = self.organize_proxies(proxy_type, input_file_path)
        test_proxies0(proxies, True)
        proxies = [proxy for proxy in proxies if proxy.ping > 0]
        putils.write_list(output_file_path, proxies)

    def set_proxy_before_running_browser(self, proxy: Proxy0 = None):
        if proxy:
            proxy_s = f'{proxy.ip}:{proxy.port}'
            proxy_capabality = {"proxyType": "manual"}
            if 'http' in proxy.type:
                proxy_capabality['httpProxy'] = proxy_s
                proxy_capabality['sslProxy'] = proxy_s
            if 'socks' in proxy.type:
                proxy_capabality['socksProxy'] = proxy_s
        else:
            proxy_capabality = {"proxyType": "manual"}

        capabilities = DesiredCapabilities.FIREFOX
        capabilities["proxy"] = proxy_capabality

    def set_proxy_dynamically(self, proxy: Proxy0 = None):
        http_addr = http_port = ssl_addr = ssl_port = socks_addr = socks_port = ''
        if proxy:
            if 'http' in proxy.type:
                http_addr = proxy.ip
                http_port = proxy.port

                ssl_addr = proxy.ip
                ssl_port = proxy.port

            if 'socks' in proxy.type:
                socks_addr = proxy.ip
                socks_port = proxy.port

        self.driver.execute("SET_CONTEXT", {"context": "chrome"})
        try:
            self.driver.execute_script(
                """
            Services.prefs.setIntPref('network.proxy.type', 1);
            Services.prefs.setCharPref("network.proxy.http", arguments[0]);
            Services.prefs.setIntPref("network.proxy.http_port", arguments[1]);
            Services.prefs.setCharPref("network.proxy.ssl", arguments[2]);
            Services.prefs.setIntPref("network.proxy.ssl_port", arguments[3]);
            Services.prefs.setCharPref('network.proxy.socks', arguments[4]);
            Services.prefs.setIntPref('network.proxy.socks_port', arguments[5]);
            """,
                http_addr,
                http_port,
                ssl_addr,
                ssl_port,
                socks_addr,
                socks_port,
            )
        finally:
            self.driver.execute("SET_CONTEXT", {"context": "content"})

    # def read_cookies(self):
    # self.cookies = putils.read_obj(os.path.join(self.working_dir, 'cookies.json'))

    def kill_driver(self):
        try:
            self.driver.quit()
        except BaseException as e:
            # print(f'exception when quiting driver: {e}')
            pass
        print('driver closed')
        try:
            os.system('pkill firefox')
        except BaseException as e:
            # print(f'exception when killing firefox: {e}')
            pass
        print('firefox killed')

    def prepare_driver(self, kill_first=True):
        """
        if proxy:
            proxy_s = f'{proxy.ip}:{proxy.port}'

            proxy_capabality = {"proxyType": "MANUAL"}
            if 'http' in proxy.type:
                proxy_capabality['httpProxy'] = proxy_s
            if 'socks' in proxy.type:
                proxy_capabality['socksProxy'] = proxy_s

            capabilities = DesiredCapabilities.FIREFOX
            capabilities["proxy"] = proxy_capabality
        """
        if kill_first:
            self.kill_driver()

        firefox_profile = webdriver.FirefoxProfile()
        # if os_windows:
        #     firefox_profile = webdriver.FirefoxProfile(r'C:\Users\EBRAHIM\AppData\Roaming\Mozilla\Firefox\Profiles\dzg5lsxn.default-release')
        firefox_profile.set_preference('permissions.default.image', 1)
        # firefox_profile.set_preference("browser.shell.checkDefaultBrowser", False)
        # firefox_profile.set_preference('app.update.auto', False)
        # firefox_profile.set_preference('app.update.enabled', False)
        # firefox_profile.set_preference('dom.webdriver.enabled', False)
        # firefox_profile.set_preference('useAutomationExtension', False)
        # firefox_profile.update_preferences()
        # firefox_profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')

        firefox_options = FirefoxOptions()
        if os_linux:
            firefox_options.add_argument('--headless')
            firefox_options.add_argument('--no-sandbox')
        # firefox_options.add_argument("start-maximized")
        firefox_options.profile = firefox_profile
        if os_windows:
            firefox_options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
        # firefox_options.add_argument("--no-default-browser-check")
        # firefox_options.add_argument("--disable-blink-features=AutomationControlled")

        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=firefox_options)
        self.driver.maximize_window()
        # handles = self.driver.window_handles
        # desired_handle = handles[0]
        # self.driver.switch_to.window(desired_handle)
        # self.driver.get('https://www.instagram.com/accounts/login/')

    def save_page(self):
        with open("source.html", "w", encoding="utf-8") as f:
            f.write(self.driver.page_source)

    def go_to_tab(self, tab_index=0):
        handles = self.driver.window_handles
        desired_handle = handles[tab_index]
        self.driver.switch_to.window(desired_handle)

    def go_to_url(self, link):
        self.go_to_tab(0)
        self.driver.get(link)

    def wait_for_page_load(self, interval=3, timeout=10.0):
        t = time.time()
        WebDriverWait(self.driver, 10).until(lambda wd: wd.execute_script("return document.readyState") == 'complete')
        old_html = 'o'
        new_html = 'n'

        while True:
            html_body = self.find_first_element(Elements.html_body)
            if html_body:
                new_html = html_body.get_attribute('outerHTML')
                if old_html == new_html:
                    break
                else:
                    old_html = new_html
            if time.time() - t > timeout:
                break
            time.sleep(interval)

    def wait_for_element_presense(self, element: Element0, timeout=10):
        try:
            element_found = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((element.by, element.query)))
        except BaseException:
            return None
        return element_found

    def wait_for_any_of_elements_presense(self, elements: list[Element0], timeout=10):
        try:
            elements = [EC.presence_of_element_located((element.by, element.query)) for element in elements]
            element_found = WebDriverWait(self.driver, timeout).until(EC.any_of(*elements))
        except BaseException:
            return None
        return element_found

    # def wait_for_element(self, wait_for_event, parameters):
    #     try:
    #         WebDriverWait(self.driver, 10).until(wait_for_event(parameters))
    #     except BaseException:
    #         return None

    def find_single_element(self, element: Element0):
        elements = self.driver.find_elements(element.by, element.query)
        if len(elements) == 1:
            return elements[0]
        else:
            raise Exception(f'elements found is not exactly one {len(elements)}')

    def find_first_element(self, element: Element0):
        try:
            return self.driver.find_element(element.by, element.query)
        except BaseException:
            return None

    def find_elements(self, element: Element0):
        return self.driver.find_elements(element.by, element.query)

    def bypass_question(self):
        button = self.find_first_element(Elements.instagram_button_not_now)
        if button:
            button.click()
            time.sleep(2)

    def set_instagram_cookies(self, cookies: dict):
        if 'instagram.com' not in extract_domain(self.driver.current_url):
            self.go_to_url(Urls.insta_dummy)
            self.wait_for_element_presense(Elements.instagram_page_not_available)
        self.driver.delete_all_cookies()
        for cookie in cookies:
            self.driver.add_cookie(cookie)

    def check_if_instagram_cookies_valid(self, cookies):
        self.set_instagram_cookies(cookies)
        self.go_to_url(Urls.insta_dummy)
        # self.wait_for_page_load()
        self.wait_for_any_of_elements_presense([Elements.instagram_login_button_small_top_right, Elements.instagram_left_menu])
        if not self.find_first_element(Elements.instagram_login_button_small_top_right) and self.find_first_element(Elements.instagram_left_menu):
            return True
        else:
            return False


    def check_accounts_and_create_cookies(self, accounts_file_path, output_cookies_file_path, previous_cookies_file_path=None, proxies_file_path=None, max_retries=2, force_renew_cookies=True, account_randomizer=False):
        print('reading info...')
        if proxies_file_path:
            proxies: list[Proxy0] = putils.read_list(proxies_file_path)
        accounts_list = putils.read_list(accounts_file_path)
        
        print(f'account randomizer is {account_randomizer}')
        if account_randomizer:
            random.shuffle(accounts_list)
        preview_cookies_dict = dict()
        all_cookies = list()

        if previous_cookies_file_path:
            last_cookies_list = putils.read_list(previous_cookies_file_path)
            for item in last_cookies_list:
                preview_cookies_dict[item[0]] = item[1]

        # print(preview_cookies_dict)
        print('start checking accounts...')
        for username, password in accounts_list:
            print(f'username: {username}')
            if proxies_file_path:
                proxy = random.choice(proxies)
                self.set_proxy_dynamically(proxy)
                print(f'using proxy: {proxy.type}: {proxy.ip}:{proxy.port}')

            preview_cookie = preview_cookies_dict.get(username, None)
            if not force_renew_cookies and preview_cookie and self.check_if_instagram_cookies_valid(preview_cookie):
                print("this account's previous cookie is valid, skip loging in")
                all_cookies.append([username, preview_cookie])
                putils.write_list(output_cookies_file_path, all_cookies)
                continue

            for retry_index in range(max_retries):
                print('trying to login')
                self.driver.delete_all_cookies()
                self.go_to_url(Urls.insta_login)
                self.wait_for_element_presense(Elements.instagram_login_button)
                # time.sleep(2)

                element = self.find_first_element(Elements.instagram_login_username)
                element.send_keys(username)
                time.sleep(1.5)

                element = self.find_first_element(Elements.instagram_login_password)
                element.send_keys(password)
                time.sleep(1.5)

                button = self.find_first_element(Elements.instagram_login_button)
                button.click()

                self.wait_for_any_of_elements_presense([Elements.instagram_left_menu, Elements.instagram_something_went_wrong])
                # self.wait_for_page_load()

                if self.find_first_element(Elements.instagram_something_went_wrong):
                    # break
                    pass

                if self.find_first_element(Elements.instagram_left_menu):
                    print('loging is successful, saving cookie...')
                    self.driver.get(Urls.insta_dummy)
                    self.wait_for_element_presense(Elements.instagram_page_not_available)
                    # self.wait_for_element_presense(Elements.instagram_left_menu)
                    cookies = self.driver.get_cookies()
                    print(f'cookies length: {len(cookies)}')
                    all_cookies.append([username, cookies])
                    putils.write_list(output_cookies_file_path, all_cookies)
                    self.driver.delete_all_cookies()
                    break
                else:
                    pass

    def report_accounts(self, accounts_to_report:list[str], report_options:list[int], block, cookies_file_path, proxies_file_path=None):
        print('reading info...')
        if proxies_file_path:
            proxies: list[Proxy0] = putils.read_list(proxies_file_path)
        all_cookies = putils.read_list(cookies_file_path)
        
        print('start...')
        for username, cookies in all_cookies:
            print(f'username: {username}')
            if proxies_file_path and proxies:
                proxy = random.choice(proxies)
                self.set_proxy_dynamically(proxy)
                print(f'using proxy: {proxy.type}: {proxy.ip}:{proxy.port}')

            for usernaem in accounts_to_report:
                print(f'reporting {usernaem}')
                self.driver.delete_all_cookies()
                self.set_instagram_cookies(cookies)
                self.go_to_url(Urls.some_page(usernaem))
                result = self.wait_for_any_of_elements_presense([Elements.instagram_something_went_wrong, Elements.instagram_account_3_dot_menu, Elements.instagram_login_button_small_top_right, Elements.instagram_page_not_available])
                if not result:
                    print('this account has some problems')
                    continue
                time.sleep(1)
                self.bypass_question()

                element_username = self.wait_for_element_presense(Elements.instagram_some_page_username)
                if element_username:
                    print(f'user: {element_username.text}')
                    element = self.wait_for_element_presense(Elements.instagram_account_3_dot_menu)
                    element.click()
                    time.sleep(1)
                    element = self.wait_for_element_presense(Elements.instagram_report_red_button)
                    element.click()
                    time.sleep(1)
                    element = self.wait_for_element_presense(Elements.instagram_report_account_button)
                    element.click()
                    time.sleep(2)
                else:
                    print('error finding username element')
                    continue
                # 3
                # It's posting content that shouldn't be on Instagram
                # It's pretending to be someone else
                # It may be under the age of 13
                elements_options = self.find_elements(Elements.instagram_report_options)
                elements_options[report_options[0]].click()
                time.sleep(2)

                for i in range(1,10):
                    try:
                        action = report_options[i]
                    except BaseException:
                        action = -10
                    try:
                        if action >= 0:
                            elements = self.find_elements(Elements.instagram_report_options)
                            if not elements:
                                elements = self.find_elements(Elements.instagram_report_radio_buttions)
                                if not elements:
                                    print('error 5')
                            
                            elements[action].click()
                            time.sleep(2)
                            continue

                        # if action == -1:
                        submit_button = self.find_first_element(Elements.instagram_report_submit_button)
                        if submit_button:
                            submit_button.click()
                            time.sleep(2)
                            continue

                        if block:
                            element_block_button = self.find_first_element(Elements.instagram_report_block_button_1)
                            if element_block_button:
                                element_block_button.click()
                                element_block_button2 = self.wait_for_element_presense(Elements.instagram_report_block_button_2, 5)
                                time.sleep(1)
                                if element_block_button2:
                                    element_block_button2.click()
                                    time.sleep(2)
                                    continue
                        
                        close_button = self.find_first_element(Elements.instagram_report_close_button)
                        if close_button:
                            try:
                                close_button.click()
                            except BaseException:
                                pass
                            continue
                            
                            
                    except BaseException:
                        pass
args_backup = list(sys.argv)
print(sys.argv)

# %%

if os_windows:
    try:
        if args_backup:
            sys.argv = list(args_backup)
    except BaseException:
        pass
    sys.argv.pop()
    # sys.argv += 'account ./accounts2.txt ./accounts2.json true'.split(' ')
    sys.argv += 'cookie ./accounts2.json ./cookies2.json null null 2 true false'.split(' ')
# sys.argv += 'cookie ./accounts.json ./cookies.json null ./proxy_t_processed.json 2 true'.split(' ')

args = [arg.strip() for arg in get_args()]
print(30*'-')
for index, arg in enumerate(args):
    print(f'{index}, {arg}')
print(30*'-')

# %%
try:
    igbot.kill_driver()
except BaseException:
    pass
igbot = IGBot()

if args[0] == 'account':
    igbot.organize_accounts(args[1], args[2], args[3] == 'true')
elif args[0] == 'proxy':
    igbot.process_proxies(args[1], args[2], args[3])
elif args[0] == 'cookie':
    igbot.prepare_driver()
    igbot.check_accounts_and_create_cookies( \
                                        accounts_file_path=args[1], 
                                        output_cookies_file_path=args[2],
                                        previous_cookies_file_path=args[3] if args[3] != 'null' else None,
                                        proxies_file_path=args[4] if args[4] != 'null' else None,
                                        max_retries=int(args[5]),
                                        force_renew_cookies=(args[6] == 'true'),
                                        account_randomizer=args[7] == 'true'
                                        )
elif args[0] == 'report':
    igbot.prepare_driver()
    igbot.report_accounts( \
                    accounts_to_report=str(args[1]).split(','),
                    report_options=[int(i) for i in str(args[2]).split(',')],
                    block=args[3] == 'true',
                    cookies_file_path=args[4],
                    proxies_file_path=(args[5] if args[5] != 'null' else None)
                    )
else:
    print('enter correct function name!')

exit(0)

# %%


# %%
try:
    igbot.kill_driver()
except BaseException:
    pass
igbot = IGBot()

# %%
# igbot.process_proxies('http', './proxy_t.txt', './proxy_t_processed.json')
# igbot.organize_accounts('./accounts.txt','./accounts_processed.json')

# %%
igbot.prepare_driver()

# %%
igbot.driver.delete_all_cookies()
igbot.report_accounts( \
                    accounts_to_report=['mahnaz_afshar'],
                    report_options=[0,4,0],
                    block=True,
                    cookies_file_path='./cookies_new5.json',
                    proxies_file_path='./proxy_t_processed.json'
                    )

# %%
igbot.read_cookies('./cookies_new5.json')
igbot.set_instagram_cookies(igbot.cookies[2][1])

# %%
element_block_button2 = igbot.wait_for_element_presense(Elements.instagram_report_block_button_2, 3)
time.sleep(1)
element_block_button2

# %%
# igbot.read_proxies('./proxy_t_processed.json')
# igbot.set_proxy_dynamically(igbot.proxies[1])

# %%
e = igbot.wait_for_element_presense(Elements.instagram_report_red_button)
e

# %%
igbot.check_accounts_and_create_cookies( \
                                        accounts_file_path='./accounts_processed.json', 
                                        output_cookies_file_path='./cookies_new5.json',
                                        previous_cookies_file_path='./cookies_new4.json',
                                        proxies_file_path='./proxy_t_processed.json',
                                        max_retries=2,
                                        force_renew_cookies=False
                                        )

# %%


# %%
e = igbot.find_first_element(Elements.instagram_report_block_button_1)

# %%
elements_options = igbot.find_elements(Elements.instagram_report_block_button_2)
for element in elements_options:
    print(element.text)

# %%
igbot.proxies

# %%


# %%
# igbot.prepare_driver(Proxy0('http', '154.6.98.146',3128))
igbot.prepare_driver()
igbot.go_to_url(Urls.insta_main)
igbot.wait_for_page_load()
element = igbot.find_first_element(Elements.html_body)
with open("source.html", "w", encoding="utf-8") as f:
    f.write(igbot.driver.page_source)
igbot.kill_driver()

# %%
igbot.check_if_instagram_cookies_valid(igbot.cookies['ebrahim.shami.a'])
# igbot.check_if_instagram_cookies_valid(igbot.cookies['test'])
# igbot.create_accounts_cookies()

# %%
igbot.set_proxy_dynamically(Proxy0('http', '127.0.0.1', 2081))
# igbot.set_proxy()

# %%
igbot.go_to_tab(0)
# e = igbot.driver.find_elements(By.XPATH, "//span[@class='x1lliihq x1plvlek xryxfnj x1n2onr6 x193iq5w xeuugli x1fj9vlw x13faqbe x1vvkbs x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x1i0vuye x1ms8i2q xo1l8bm x5n08af x4zkp8e xw06pyt x10wh9bi x1wdrske x8viiok x18hxmgj'][contains(text(), 'Sorry')]")
# e = igbot.driver.find_elements(By.XPATH, "//span[@class='x1lliihq x1plvlek xryxfnj x1n2onr6 x193iq5w xeuugli x1fj9vlw x13faqbe x1vvkbs x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x1i0vuye x133cpev x1s688f x5n08af x2b8uid x4zkp8e x41vudc x10wh9bi x1wdrske x8viiok x18hxmgj'][contains(text(), 'Sorry')]")
e = igbot.find_elements(Elements.instagram_something_went_wrong)
e

# %%
# igbot.go_to_page('https://youtube.com')
igbot.wait_for_page_load(0.1)

# %%
igbot.driver.delete_all_cookies()

# %%
igbot.cookies

# %%
igbot.driver.delete_all_cookies()
igbot.go_to_url('https://instagram.com')
for cookie in igbot.cookies['ebrahim.shami.a']:
    print(cookie)
    igbot.driver.add_cookie(cookie)
igbot.go_to_url('https://instagram.com')

# %%
# igbot.go_to_page(IgPAges.login)
t = time.time()
html_body = igbot.wait_for_element_presense(Elements.instagram_left_menu)
t = time.time() - t
print(html_body)
print(t)


