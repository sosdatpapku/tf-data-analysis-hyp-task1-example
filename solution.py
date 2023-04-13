import pandas as pd
import numpy as np
from statsmodels.stats.proportion import proportions_ztest


chat_id = 1188007817 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    prop_control = x_success / x_cnt
    prop_test = y_success / y_cnt

# Сравниваем доли продаж с помощью z-теста
    count = [x_success, y_success]
    nobs = [x_cnt, y_cnt]
    stat, pval = proportions_ztest(count, nobs, alternative='larger')

# Проверяем значимость различий между группами
    if pval < 0.04:
        return True
    else:
        return False
