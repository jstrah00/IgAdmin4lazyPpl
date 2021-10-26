from selenium import webdriver
import time
import requests

class IgLazyBot():
    def __init__(self):
        import local_settings
        self.ig_username = local_settings.ig_username
        self.ig_password = local_settings.ig_password
        self.webdriver_path = local_settings.webdriver_path 
        self.ig_base_url = "https://www.instagram.com/"
        self.image_density = 1 #Value for Get_images, high value, more photos
        self.download_directory = 'downloaded_images' #Directory for de downloaded images

    def start_driver(self):
        self.driver = webdriver.Chrome(self.webdriver_path)

    def login_instagram(self):
        self.driver.get(self.ig_base_url + "accounts/login/")
        time.sleep(1)
        self.driver.find_element_by_name("username").send_keys(self.ig_username)
        self.driver.find_element_by_name("password").send_keys(self.ig_password)
        time.sleep(1)
        self.driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(4)

    def download_images(self, url_list, directory):
        for href in url_list:
            self.driver.get(str(href))
            
            ####### Test image

            nombre_tipo = self.driver.find_elements_by_class_name("sqdOP yWX7d     _8A5w5   ZIAjV")#[0].get_attribute('innerHTML')
            print(href)
            print(nombre_tipo)

            text_to_save = str(self.driver.page_source).split("{\"text\":\"")[1].split("\"}}]},")[0]
            name = str(href.split("/")[-2])
            f = open(name + ".txt", "x")
            f.write(text_to_save)

            ##########
            img_src = self.driver.find_element_by_xpath('//div/img').get_attribute("src")
            try:
                r = requests.get(img_src)
                filename = name + '.jpg'
                with open(directory + '/' + filename, 'wb') as fp:
                    fp.write(r.content)
            except Exception:
                pass

    def scroll_down(self, density):
        for i in range(density):
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)

    def get_href_images(self, density):
        self.driver.get("https://www.instagram.com/explore/")
        time.sleep(2)
        self.scroll_down(density)
        images = self.driver.find_elements_by_class_name("pKKVh")
        images_href = []
        for img in images:
            try:
                href = img.find_element_by_tag_name("a").get_attribute("href")
                images_href.append(href)
            except Exception:
                pass
        return images_href

    def get_images(self):
        self.start_driver()
        self.login_instagram()
        images_href = self.get_href_images(self.image_density)
        self.download_images(images_href, self.download_directory)
        self.driver.close()
        
