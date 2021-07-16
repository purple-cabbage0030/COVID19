import requests
from selenium import webdriver 
from bs4 import BeautifulSoup 
import time
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import numpy as np
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import os
from openpyxl import load_workbook


# 방역본부 백신 일일 접종 현황 다운로드 + pandas로 전처리 
def download():
    main_url = "https://ncv.kdca.go.kr/board.es?mid=a11710000000&bid=0037#content"
    driver = webdriver.Chrome("C:/driver/chromedriver")
    driver.get(main_url)
    time.sleep(2)  
    driver.implicitly_wait(1) 
    driver.find_element_by_xpath('//*[@id="listView"]/ul/li[2]/a').click()
    time.sleep(2)  
    driver.implicitly_wait(2) 
    driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div[3]/div[2]/ul/li/a').click()
    time.sleep(4)  
    driver.close()

    file_name = os.listdir("C:/Users/YEIN/Downloads")

    for file in file_name:
        if file.startswith('코로나바이러스'):
            file_name = file

    datas = pd.read_excel(r'C:/Users/YEIN/Downloads/{}'.format(file_name))

    d_columns = ['일자','ALL(1)','ALL(FIN)','아제(1)','아제(FIN)','화이자(1)','화이자(FIN)','얀센','모더나']

    datas = datas.drop(index=[0,1,2,3,4,5], axis=0)
    datas.columns = d_columns
    datas = datas.reset_index()
    del datas['index']
    datas.to_csv("kor_vaccine.csv", index = False)

if __name__ == '__main__':
    download()