from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
import os
import time


def setup_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-extensions")

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    wait = WebDriverWait(driver, 10)

    return driver, wait


def go_home(driver, wait):
    driver.get("https://the-internet.herokuapp.com/")
    wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()='Dropdown']")))


def main():
    driver, wait = setup_driver()

    try:
        # =====================================================
        # HOME
        # =====================================================
        go_home(driver, wait)

        # =====================================================
        # DROPDOWN
        # =====================================================
        driver.find_element(By.XPATH, "//a[text()='Dropdown']").click()

        dropdown = Select(wait.until(EC.visibility_of_element_located((By.ID, "dropdown"))))
        dropdown.select_by_visible_text("Option 2")
        print("✅ Dropdown passed")

        go_home(driver, wait)

        # =====================================================
        # JAVASCRIPT ALERTS
        # =====================================================
        driver.find_element(By.XPATH, "//a[text()='JavaScript Alerts']").click()

        driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()
        wait.until(EC.alert_is_present())
        Alert(driver).accept()

        driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
        wait.until(EC.alert_is_present())
        Alert(driver).dismiss()

        driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()
        wait.until(EC.alert_is_present())
        alert = Alert(driver)
        alert.send_keys("Selenium Test")
        alert.accept()

        print("✅ JavaScript alerts passed")

        go_home(driver, wait)

        # =====================================================
        # DYNAMIC LOADING
        # =====================================================
        driver.find_element(By.XPATH, "//a[text()='Dynamic Loading']").click()
        driver.find_element(By.XPATH, "//a[contains(text(),'Example 1')]").click()

        driver.find_element(By.CSS_SELECTOR, "#start button").click()

        wait.until(EC.visibility_of_element_located((By.XPATH, "//h4[text()='Hello World!']")))
        print("✅ Dynamic loading passed")

        go_home(driver, wait)

        # =====================================================
        # FILE UPLOAD
        # =====================================================
        driver.find_element(By.XPATH, "//a[text()='File Upload']").click()

        file_path = os.path.abspath("upload_test.txt")
        with open(file_path, "w") as f:
            f.write("Selenium upload test")

        driver.find_element(By.ID, "file-upload").send_keys(file_path)
        driver.find_element(By.ID, "file-submit").click()

        wait.until(EC.visibility_of_element_located((By.TAG_NAME, "h3")))
        print("✅ File upload passed")

        time.sleep(3)

    finally:
        driver.quit()


if __name__ == "__main__":
    main()
