from selenium import webdriver
import time

class my_test:
    def test1(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://erphub.soulltd.in/")
        time.sleep(5)
        driver.quit()
        s = "Chinmaya"
        print(s[::-1])
        for i in range(100):
            print("Hello World")




a = my_test()
a.test1()

