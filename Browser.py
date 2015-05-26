#coding:utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import time

class Browser(object):
	def __init__(self,type=1,threads=1):
		self.threads = threads
		if type ==1:
			self.driver = webdriver.Firefox()
		else:
			self.driver = webdriver.Chrome()

	def open(self,s):  
		try:
			self.driver.get(s)
			self.driver.maximize_window()
		except:
			save_pic(self.driver)   
		
	def click(self,s):
		em = self.driver.find_element_by_xpath(s)
		try:
			if "javascript:;" in em.get_attribute('href'):
				self.driver.execute_script("arguments[0].click();", em)
			else:
				em.click()
		except:
			em.click()     

	def find(self,s):
		try:
			em = self.driver.find_element_by_xpath(s)
			return em
		except:
			save_pic() 
			
	def finds(self,s):   
		try:
			ems = self.driver.find_elements_by_xpath(s)
			return ems
		except:
			save_pic()     

	def hover(self,s):
		try:
			em = self.driver.find_element_by_xpath(s)
			ActionChains(self.driver).move_to_element(em).perform()
		except:
			save_pic() 

	def rinput(self,s,word):   
		try:
			self.driver.find_element_by_xpath(s).send_keys(word)
		except:
			save_pic() 

	def input(self,s,word):   
		try:
			self.driver.find_element_by_xpath(s).clear()
			self.driver.find_element_by_xpath(s).send_keys(word)
		except:
			save_pic() 
		
	def switch_frame(self,frame):
		try:
			self.driver.switch_to_frame(frame)
		except:
			save_pic()       
		
	def switch_window(self,nowhandle):
		try:
			all_handles = self.driver.window_handles
			for handle in all_handles:
				if handle != nowhandle:
					self.driver.switch_to_window(handle)
		except:
			save_pic()   

	def save_pic(self):
		cur_time=time.strftime("%Y_%m_%d_%H_%M", time.localtime())    
		self.driver.get_screenshot_as_file('D:\\Work\\Web\\Selenium\\error\\'+ cur_time +'.png')

	def exec_script(self,script,args):
		self.driver.execute_script(script, args)
		
	def quit(self):
		self.driver.quit()