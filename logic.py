from selenium import webdriver
import time

driver = webdriver.Firefox()


def get_data():
    url = input('Enter URL without the page number (www.example.com/page=)\n')
    pages_amount = int(input('Enter amount of pages\n'))
    div_name = input('Enter div name\n')
    user_pref = dict(url=url, pages_amount=pages_amount, div_name=div_name)
    return user_pref


def download_content(user_pref):
    for i in range(0, user_pref['pages_amount']):
        driver.get(user_pref['url'] + f'{i}')
        time.sleep(5)
        driver.execute_script(f""" 
        var link = document.createElement('a');
        link.download = 'filename.png';
        link.href = document.getElementById('{user_pref['div_name']}').toDataURL()
        link.click();
    """)
