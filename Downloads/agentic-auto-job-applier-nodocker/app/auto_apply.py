from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def auto_fill_job_form(job_url, resume_path, linkedin_email, linkedin_password):
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.linkedin.com/login")
    time.sleep(2)
    driver.find_element(By.ID, "username").send_keys(linkedin_email)
    driver.find_element(By.ID, "password").send_keys(linkedin_password)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(5)
    driver.get(job_url)
    time.sleep(5)
    try:
        apply_btn = driver.find_element(By.CLASS_NAME, "jobs-apply-button")
        apply_btn.click()
        time.sleep(2)
    except Exception as e:
        print("Error during apply:", e)
    driver.quit()