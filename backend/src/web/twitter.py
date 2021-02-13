#!/usr/bin/python3 -B
# twitter.py

import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options


def get_tweets(username, threshold, headless=False):
    options = Options()
    options.headless = headless
    profile = webdriver.FirefoxProfile('/home/ashish/.mozilla/firefox/3kv6pmol.default-release')
    browser = webdriver.Firefox(firefox_profile=profile, options=options)
    browser.get(f'https://twitter.com/{username}')
    sleep(3)

    name = browser.find_element_by_css_selector('div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-dnmrzs > div.css-901oao.r-18jsvk2.r-1qd0xha.r-1b6yd1w.r-1vr29t4.r-ad9z0x.r-bcqeeo.r-qvutc0 > span.css-901oao.css-16my406.r-poiln3.r-bcqeeo.r-qvutc0').text.strip()
    picture = browser.find_element_by_css_selector('div.css-1dbjc4n.r-sdzlij.r-1p0dtai.r-1mlwlqe.r-1d2f490.r-1udh08x.r-u8s1d.r-zchlnj.r-ipm5af.r-417010 > img.css-9pa8cd').get_attribute('src').replace('_200x200', '', 1)

    tweets = set(x.text.replace('\n', ' ') for x in browser.find_elements_by_css_selector('div.css-901oao.r-18jsvk2.r-1qd0xha.r-a023e6.r-16dba41.r-ad9z0x.r-bcqeeo.r-bnwqim.r-qvutc0'))

    body = browser.find_element_by_tag_name('body')
    page_end = 0
    while len(tweets) < threshold and page_end < 2:
        body.send_keys(Keys.END)
        sleep(3)
        previous_len = len(tweets)
        tweets.update(set(x.text.replace('\n', ' ') for x in browser.find_elements_by_css_selector('div.css-901oao.r-18jsvk2.r-1qd0xha.r-a023e6.r-16dba41.r-ad9z0x.r-bcqeeo.r-bnwqim.r-qvutc0')))
        if previous_len == len(tweets):
            page_end += 1
        else:
            page_end = 0

    browser.close()
    if os.path.exists('geckodriver.log'):
        os.remove('geckodriver.log')

    return name, picture, list(tweets)[:threshold]
