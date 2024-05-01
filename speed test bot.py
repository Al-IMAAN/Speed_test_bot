from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
ch_op = webdriver.ChromeOptions()
ch_op.add_experimental_option("detach", True)

url = "https://www.speedtest.net/"

driver = webdriver.Chrome(ch_op)
driver.get(url)

# continue with privacy policy (id="onetrust-button-group", class="ot-sdk-row", id="onetrust-button-group")

driver.implicitly_wait(20)
ok_privacy = driver.find_element(By.ID, "onetrust-button-group")
ok_privacy.click()

# start button
start_button = driver.find_element(By.CLASS_NAME, "start-button")
start_button.click()

sleep(50)

# download_speed value
driver.implicitly_wait(15)
Download_value = driver.find_element(By.CLASS_NAME, "download-speed")
d_speed = Download_value.text

# upload_speed value
driver.implicitly_wait(15)
Upload_speed = driver.find_element(By.CLASS_NAME, "upload-speed")
u_speed = Upload_speed.text

print(f"⤵️ {d_speed}, ⤴️ {u_speed}")

driver.quit()
