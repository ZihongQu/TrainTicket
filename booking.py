# -*- coding: utf-8 -*-
"""
Created on Jan 2019

@author: Zihong Qu
"""

from splinter.browser import Browser
from time import sleep

class Buy_Tickets(object):    
    def __init__(self, username, passwd, order, passengers, dtime, starts, ends):
        self.username = username  
        self.passwd = passwd  
        self.order = order
        self.passengers = passengers
        self.starts = starts
        self.ends = ends
        self.dtime = dtime
        self.xb = xb
        self.pz = pz
        self.login_url = 'https://kyfw.12306.cn/otn/login/init'  
        self.initMy_url = 'https://kyfw.12306.cn/otn/view/index.html'  
        self.ticket_url = 'https://kyfw.12306.cn/otn/leftTicket/init' 
        self.driver_name = 'chrome'

# To login
    def login(self,browser):
        self.driver.visit(self.login_url) 
        self.driver.fill('loginUserDTO.user_name', self.username) 
        sleep(1)       

        self.driver.fill('userDTO.password', self.passwd)
        sleep(1)
        print('Verification code please:\n')
        while True:
            if self.driver.url != self.initMy_url:
                sleep(1)
            else:
                break
    def start_buy(self):
        self.driver = Browser(driver_name=self.driver_name)

        self.driver.driver.set_window_size(1000, 1000)
        self.login(self.driver)
        self.driver.visit(self.ticket_url)
        try:
            print('Purchasing tickets')

            self.driver.cookies.add({"_jc_save_fromStation": self.starts})
            self.driver.cookies.add({"_jc_save_toStation": self.ends})
            self.driver.cookies.add({"_jc_save_fromDate": self.dtime})
            self.driver.reload()
            count = 0
            if self.order != 0:
              while self.driver.url == self.ticket_url:
                self.driver.find_by_text('查询').click() 
                count += 1
                print('The %d time to look up' % count)
                try:
                    self.driver.find_by_text('预订')[self.order - 1].click()
                    sleep(10)
                except Exception as ret:
                     print(ret)
                     print('Booking failed with exceptions')
                     continue
            else:
              while self.driver.url == self.ticket_url:
                  self.driver.find_by_text('查询').click()
                  count += 1
                  print('The %d time to look up' % count)
                  try:
                      for i in self.driver.find_by_text('预订'):
                          i.click()
                          sleep(10)
                  except Exception as ret:
                      print(ret)
                      print('Booking failed with exceptions')
                      continue
            print('Booking in progress')
            sleep(1)
            print('Selecting passengers')
            for p in self.passengers:
                self.driver.find_by_text(p).last.click()
                sleep(2)
                print('Submitting')
                self.driver.find_by_id('submitOrder_id').click()
                sleep(2)
                print('Selecting Seats') #default seats for now
                self.driver.find_by_id('qr_submit_id').click()
                print('Booking is successful')
        except Exception as ret:
            print(ret)
if __name__ == '__main__':
    username = 'xwy_hong@sina.com'    
    password = 'Jgt51y'    
    order = 4   
    passengers = ['xxx']  #passenger name 
    dtime = '2020-01-30'  #date
    starts = '%u8861%u6C34%u5317%2CIHP'   #cookie value of starting station
    ends = '%u5E38%u5DDE%u5317%2CESH'  
    xb =['二等座']    #seat class
    pz=['成人票']  #type of tickets
    buy1 = Buy_Tickets(username, password, order, passengers, dtime, starts, ends)
    buy1.start_buy() 