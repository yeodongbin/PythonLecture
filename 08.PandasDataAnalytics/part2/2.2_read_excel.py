# -*- coding: utf-8 -*-
# xlrd

import pandas as pd
import os
#print(__file__)
#print(os.getcwd())  
#print("\n\n")

file_path = os.path.dirname(os.path.realpath(__file__))
file_path += '\\korea_power_generation.xlsx'

# read_excel() 함수로 데이터프레임 변환 
df1 = pd.read_excel(file_path)               # header=0 (default )
df2 = pd.read_excel(file_path, header=None)  # header=None 
# 데이터프레임 출력
print(df1)
print('\n')
print(df2)