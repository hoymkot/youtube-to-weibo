import time 
import os
import mouse
import keyboard
import logging
import logging.config

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import config 


logging.config.fileConfig('logging.conf')
logger = logging.getLogger()

def wait_and_type(browser, selector, text):
	WebDriverWait(browser,timeout=config.TimeOut).until(lambda d: d.find_element_by_css_selector(selector)).send_keys(text)

def wait(browser, selector):
	return WebDriverWait(browser,timeout=config.TimeOut).until(lambda d: d.find_element_by_css_selector(selector))


def upload_video_to_weibo(video, thumbnail, title):
	caps = DesiredCapabilities().FIREFOX
	caps["pageLoadStrategy"] = "eager"  #  complete

	browser = webdriver.Firefox(desired_capabilities=caps
				, firefox_profile=config.FirefoxProfileFolder 
				)

	logger.info("go to landing page")
	browser.get(config.LandingPage)

	logger.info("open tweet dialog box")
	wait(browser, ".Pub_icon_3Vue-").click()

	logger.info("click video tweet button")
	wait(browser, ".woo-font--video").click()

	logger.info("select video to upload")
	os.system('upload_file.exe ' + os.path.abspath(os.getcwd()) + '\\' + config.VideoDir+ '\\' + video)
	time.sleep(10)

	logger.info("click the 'change cover' link")
	wait(browser, ".Picture_btn_1ZYTW").click()

	logger.info("click the 'upload cover picture from local' link")
	wait(browser, ".VideoEdit_lt2_2f1nq").click()

	logger.info("select thumbnail to upload")
	# TODO: find image type from content
	os.system('upload_file.exe ' + os.path.abspath(os.getcwd()) + '\\' + config.CoverDir + '\\' + thumbnail)
	time.sleep(1)

	logger.info("click submit button")
	browser.find_element_by_css_selector(".VideoEdit_tab_2O-Y_+.woo-box-justifyCenter .wbpro-layer-btn-item").click()


	logger.info("wait for video to be fully uploaded")
	WebDriverWait(browser,timeout=config.TimeOut).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".VideoUpload_box2_1bjDZ .VideoUpload_box2b_1voLe[style=''] > span"), "上传成功"))


	logger.info("enter title")
	# weibo prevents people from programmatically interacting with the input box for video title. 
	# therefore control the mouse and keyboard to do the job
	mouse.move(config.InputBoxX, config.InputBoxY)
	mouse.click(button='left')
	if  len(title) < 11 :
		title = title + "          "
	keyboard.write(title)

	logger.info("confirm upload")
	browser.find_element_by_css_selector(".wbpro-layer-btn-item+.wbpro-layer-btn-item").click()


	logger.info("enter tweet text")
	wait_and_type(browser, ".Form_input_2gtXx", title)

	logger.info("confirm tweet")
	wait(browser, ".Visible_limits_11OKi+.woo-button-main").click()
