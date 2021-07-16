from selenium import webdriver 
from bs4 import BeautifulSoup 
import time
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import numpy as np
import platform
import requests

if platform.system() == 'Windows':
    path = 'c:/Windows/Fonts/malgun.ttf'
    font_name = font_manager.FontProperties(fname = path).get_name()
    rc('font', family = font_name)
elif platform.system() == 'Darwin':
    rc('font', family = 'AppleGothic')
else:
    print('Check your OS system')

class Crawling():
    def crawl_covid():
        browser = webdriver.Chrome("c:/driver/chromedriver.exe")
        results = []
        try:
            url = "https://www.worldometers.info/coronavirus/#countries" 
            browser.get(url)
            time.sleep(2)
            html = browser.page_source
            soup = BeautifulSoup(html, "html.parser")
            table_list = soup.select("#main_table_countries_today > tbody:nth-child(2) > tr")
            

            for i in range(0, len(table_list)):
                if table_list[i].select("a.mt_a"):
                    country  = table_list[i].select("a.mt_a")[0].text
                    tot_cases  = table_list[i].select("td.sorting_1")[0].text
                    new_cases  = table_list[i].select("tr > td:nth-child(4)")[0].text
                    tot_deaths = table_list[i].select("tr > td:nth-child(5)")[0].text
                    new_deaths = table_list[i].select("tr > td:nth-child(6)")[0].text
                    tot_recov = table_list[i].select("tr > td:nth-child(7)")[0].text
                    new_recov = table_list[i].select("tr > td:nth-child(8)")[0].text
                    tests = table_list[i].select("tr > td:nth-child(13)")[0].text
                    pop = table_list[i].select("tr > td:nth-child(15)")[0].text
                    data = [country, tot_cases, new_cases, tot_deaths, new_deaths, tot_recov, new_recov, tests, pop]
                    results.append(data)
                else:
                    continue


        except Exception as e:
            print("페이지 파싱 에러", e)
        finally:
            time.sleep(3)
            browser.quit()
            df = pd.DataFrame(results)
            df.columns = ["country", "tot_cases", "new_cases", "tot_deaths", "new_deaths", "tot_recov", "new_recov", "tests", "pop"]
            df.set_index("country", inplace=True)
            df.sort_index(ascending=True, inplace=True)
            df.reset_index(inplace=True)
            df.to_excel("./covid19.xlsx", index = False)


        try:
            url="https://www.un.org/en/about-us/member-states"
            res = requests.get(url)
            html = res.text
            soup = BeautifulSoup(html, "html.parser")

            country_names = soup.select(".mb-0")
            country_list = []
            for i in country_names:
                country_list.append(i.text)
                
            col = ["country"]
            country_df = pd.DataFrame(country_list, columns=col)

            # 영국의 경우 UN에 북아일랜드와 함께 가입되어있는데 gdp 자료는 영국 기준이라서 이름 변경
            country_df.iloc[182, 0] = "United Kingdom"

            # 국가별 2018, 2019 gdp 정보가 있는 엑셀 파일 read
            gdp_cap = pd.read_excel("gdp_per_capita.xls")
            gdp_df = pd.merge(left=country_df,
                            right=gdp_cap,
                            how="left",
                            left_on="country",
                            right_on="Country Name")

            # df_nulls = gdp_df.isnull().sum()
            # un 가입국이지만 gdp 정보가 없는 국가 3개
            # 2018년, 2019년 모두 gdp 정보가 없는 국가 drop 필요
            # thresh: 해당 row에서 NaN이 아닌 값이 최소 3개 이상 나와야 한다는 설정
            gdp_pop = gdp_df.dropna(axis = 0, thresh = 3)
            del gdp_pop["Country Name"]
            gdp_pop = gdp_pop.reset_index()
            del gdp_pop["index"]

            # gdp_pop[gdp_pop["2019"].isnull()]
            # 2019 nan값을 2018 정보로 대체
            gdp_pop.iloc[94, 2] = gdp_pop.iloc[94, 1]
            gdp_pop.iloc[183, 2] = gdp_pop.iloc[183, 1]
            del gdp_pop["2018"]

            # 데이터 타입 변환
            gdp_pop = gdp_pop.astype({"2019":"int64"})
        except Exception as e:
            print("페이지 파싱 에러", e)
        finally:
            time.sleep(3)
            browser.quit()
        
        try:
            df = pd.read_excel("covid19.xlsx")

            df["tot_cases"] = df["tot_cases"].str.replace(",", "")
            df["new_cases"] = df["new_cases"].str.replace("+", "")
            df["new_cases"] = df["new_cases"].str.replace(",", "")
            df["tot_deaths"] = df["tot_deaths"].str.replace(",", "")
            df["new_deaths"] = df["new_deaths"].str.replace("+", "")
            df["new_deaths"] = df["new_deaths"].str.replace(",", "")
            df["new_deaths"] = df["new_deaths"].str.replace(" ", "")
            df["tot_recov"] = df["tot_recov"].str.replace(",", "")
            df["new_recov"] = df["new_recov"].str.replace("+", "")
            df["new_recov"] = df["new_recov"].str.replace(",", "")
            df["tests"] = df["tests"].str.replace(",", "")
            df["pop"] = df["pop"].str.replace(",", "")
            df = df.replace(np.nan, 0)
            df = df.replace(" ", 0)
            df[['tot_cases', 'new_cases', 'tot_deaths', 'new_deaths', 'tot_recov', 'new_recov', 'tests', 'pop']] = df[['tot_cases', 'new_cases', 'tot_deaths', 'new_deaths', 'tot_recov', 'new_recov', 'tests', 'pop']].astype('int64')
        
            # 21개 데이터의 변경값 찾음
            df.loc[206,"country"] = "United States of America" #usa
            df.loc[160,"country"] = "Russian Federation" #Russia
            df.loc[205,"country"] = "United Kingdom" #UK
            df.loc[96,"country"] = "Iran (Islamic Republic of)" #Iran
            df.loc[51,"country"] = "Czech Republic" #Czechia
            df.loc[204,"country"] = "United Arab Emirates" #UAE
            df.loc[23,"country"] = "Bolivia (Plurinational State of)" #Bolivia
            df.loc[130,"country"] = "Republic of Moldova" #Moldova
            df.loc[163,"country"] = "Republic of Korea" #S. Korea
            df.loc[99,"country"] = "Côte D'Ivoire" #Ivory Coast 찾았다....
            df.loc[52,"country"] = "Democratic Republic of the Congo" #DRC
            df.loc[214,"country"] = "Viet Nam" # Vietnam
            df.loc[32,"country"] = "Central African Republic" # CAR
            df.loc[73,"country"] = "Gambia (Republic of The)" # Gambia
            df.loc[84,"country"] = "Guinea Bissau" # Guinea-Bissau
            df.loc[107,"country"] = "Lao People’s Democratic Republic" #Laos 찾음
            df.loc[188,"country"] = "Saint Vincent and the Grenadines" # St. Vincent Grenadines
            df.loc[196,"country"] = "United Republic of Tanzania" # Tanzania
            df.loc[28,"country"] = "Brunei Darussalam" # Brunei
            df.loc[79,"country"] = "Greenland" # Greenland
            df.loc[129,"country"] = "Micronesia (Federated States of)" #Micronesia

        except Exception as e:
            print("페이지 파싱 에러", e)
        
        finally:
            col = ["country", "tot_cases", "new_cases", "tot_deaths", "new_deaths", "tot_recov", "new_recov", "tests", "pop", "2019"]
            covid_gdp_1 = pd.merge(df, gdp_pop, how="left", on="country")
            covid_gdp_1 = covid_gdp_1.dropna(axis=0)
            covid_gdp_1 = covid_gdp_1.astype({"2019":"int64"})
            covid_gdp_1.columns = col
            covid_gdp_1.to_csv("covid_gdp.csv", index = False)
            

# if __name__ == "__main__":
#     Crawling.crawl_covid()
