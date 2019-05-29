from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

from config import USERNAME,PASSWORD


class InstagramBot:
    def __init__(self):
        self.url = 'https://www.instagram.com/'
        self.username = USERNAME
        self.password = PASSWORD
        self.browser = webdriver.Chrome(
            'C:\\Users\\jagme\\Desktop\\projects\\igscrapper\\chromedriver'
        )

    def get_login_page(self):
        #Function to get login page.
        self.browser.get(self.url)

    def close_browser(self):
        self.browser.close()

    def login_me(self):
        #Function to login into instagram.

        driver = self.browser
        #get the login element and click it.
        login_element = driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/article/div[2]/div[2]/p/a'
        )
        login_element.click()
        sleep(3)
        #Get the username field and populate it.
        username_field = driver.find_element_by_name('username')
        username_field.send_keys(self.username)
        #Get the password field and populate it.'''
        password_field = driver.find_element_by_name('password')
        password_field.send_keys(self.password)
        '''Click the login button.'''
        login_button = driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]'
        )
        login_button.click()
        sleep(5)
        notifoffbutton = driver.find_element_by_xpath(
            '/html/body/div[3]/div/div/div[3]/button[2]'
        )
        notifoffbutton.click()

    def unfollow_user(self):
        #Function to unfollow user.

        driver = self.browser
        username = input('Enter username to unfollow: ')
        driver.get(self.url + username)
        unfollow_button = driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/span/span[1]/button'
        )
        unfollow_button.click()
        sleep(1)
        confirm_button = driver.find_element_by_xpath(
            '/html/body/div[3]/div/div/div[3]/button[1]'
        )
        confirm_button.click()
        sleep(2)



    def follow_user(self):
        #Function to follow user on instagram.

        driver = self.browser
        username = input('Enter username to follow: ')
        driver.get(self.url + username)
        follow_button = driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/span/span[1]/button'
        )
        follow_button.click() 
        sleep(2)


    def like_tag_photos(self):
        #Function to like photos of a page.

        tag = input('Enter tag to like photos: ')
        driver = self.browser
        hrefs = []
        driver.get(self.url + 'explore/tags/' + tag)
        '''recent_photos_area = driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/article/div[2]/div'
        )'''
        recent_photos_area_rows = driver.find_elements_by_css_selector(
            '#react-root > section > main > article > div:nth-child(3) > div > div '
        )
        for recent_photos_area_row in recent_photos_area_rows:
            recent_photos = recent_photos_area_row.find_elements_by_tag_name('a')
            for recent_photo in recent_photos:
                href = recent_photo.get_attribute("href")
                print(href)
                hrefs.append(href)
        count = 0
        for link in hrefs:
            driver.get(link)
            sleep(1)
            like_button = driver.find_element_by_xpath(
                '//*[@id="react-root"]/section/main/div/div/article/div[2]/section[1]/span[1]/button'
            )
            like_button.click()
            count = count + 1
        print('Total photos liked = ', count)
        
        

igbot = InstagramBot()
igbot.get_login_page()
igbot.login_me()
igbot.unfollow_user()
igbot.close_browser()