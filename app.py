from flask import Flask, render_template, request, jsonify
from selenium import webdriver 
from bs4 import BeautifulSoup 
import time
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import numpy as np
import platform
import requests
import pyautogui
import os
from openpyxl import load_workbook
from wordcloud import WordCloud
from PIL import Image
import stylecloud

app = Flask(import_name=__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/', methods=['get'])
def index():
    return render_template('index_02.html')


@app.route('/covidchart', methods=['get'])
def get_covid():
    return ""

@app.route('/confirm', methods=['post'])
def confirm():
    confirm_visual = {}
    conf = pd.read_csv('merge_vaccine.csv')
    for i in range(len(conf)):
        confirm_visual[conf.iloc[i,0]] = conf.iloc[i,1]
    stylecloud.gen_stylecloud(text=confirm_visual,icon_name="fas fa-certificate",
                        palette="colorbrewer.diverging.Spectral_11",background_color='black',
                        gradient="horizontal",output_name="./static/img/confirm.jpg")
    return "confirm.jpg"

@app.route('/death', methods=['post'])
def death():
    confirm_visual = {}
    conf = pd.read_csv('merge_vaccine.csv')
    for i in range(len(conf)):
        confirm_visual[conf.iloc[i,0]] = conf.iloc[i,3]
    stylecloud.gen_stylecloud(text=confirm_visual,icon_name="fas fa-skull-crossbones",
                        palette="colorbrewer.diverging.Spectral_11",background_color='black',
                        gradient="horizontal",output_name="./static/img/death.jpg")
    return "death.jpg"

@app.route('/vaccine', methods=['post'])
def vaccine():
    confirm_visual = {}
    conf = pd.read_csv('merge_vaccine.csv')
    for i in range(len(conf)):
        confirm_visual[conf.iloc[i,0]] = conf.iloc[i,13]
    stylecloud.gen_stylecloud(text=confirm_visual,icon_name="fas fa-thermometer",
                        palette="colorbrewer.diverging.Spectral_11",background_color='black',
                        gradient="horizontal",output_name="./static/img/vaccine.jpg")
    return "vaccine.jpg"

@app.route('/gdp', methods=['post'])
def gdp():
    confirm_visual = {}
    conf = pd.read_csv('merge_vaccine.csv')
    for i in range(len(conf)):
        confirm_visual[conf.iloc[i,0]] = conf.iloc[i,9]
    stylecloud.gen_stylecloud(text=confirm_visual,icon_name="fas fa-money-check-alt",
                        palette="colorbrewer.diverging.Spectral_11",background_color='black',
                        gradient="horizontal",output_name="./static/img/gdp.jpg")
    return "gdp.jpg"

@app.route('/population', methods=['post'])
def population():
    confirm_visual = {}
    conf = pd.read_csv('merge_vaccine.csv')
    for i in range(len(conf)):
        confirm_visual[conf.iloc[i,0]] = conf.iloc[i,8]
    stylecloud.gen_stylecloud(text=confirm_visual,icon_name="fas fa-certificate",
                        palette="colorbrewer.diverging.Spectral_11",background_color='black',
                        gradient="horizontal",output_name="./static/img/population.jpg")
    return "population.jpg"


if __name__ == '__main__':
    app.run(debug=True, host="127.0.0.1", port=5000)
