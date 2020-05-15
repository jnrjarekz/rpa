from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import clipboard

driver = webdriver.Ie()
wait = WebDriverWait(driver, 10)
driver.get('https://docs.google.com/forms/d/1_XyTRmCotkVFmU_V83Mma9uGUMY460CDFEe64-QgYM0/viewform?edit_requested=true')
clipboard.copy('Stephen Anokye Boateng')
driver.find_element_by_css_selector('[aria-label="Name"]').send_keys(Keys.CONTROL,'v')
driver.find_element_by_css_selector('[aria-label="Male"]').click()
clipboard.copy('s.anokye76@gmail.com')
driver.find_element_by_css_selector('[type=email]').send_keys(Keys.CONTROL,'v')
driver.find_element_by_css_selector('[type=email]').send_keys(Keys.TAB,Keys.ENTER)
clipboard.copy('KNUST')
driver.find_element_by_css_selector('[aria-label="School of Completion"]').send_keys(Keys.CONTROL,'v')
clipboard.copy('Kumasi')
driver.find_element_by_css_selector('[aria-label="Address"]').send_keys(Keys.CONTROL,'v')
clipboard.copy('0268800762')
driver.find_element_by_css_selector('[aria-label="Phone number"]').send_keys(Keys.CONTROL,'v')
clipboard.copy('hello world')
driver.find_element_by_css_selector('[aria-label="Comments"]').send_keys(Keys.CONTROL,'v')
driver.find_element_by_css_selector('[aria-label="Comments"]').send_keys(Keys.TAB, Keys.TAB, Keys.ENTER)