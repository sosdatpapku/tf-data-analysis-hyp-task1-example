import pandas as pd
import numpy as np
from scipy.stats import ttest_ind
from scipy.stats import t


chat_id = 1188007817 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
  
    mean_X = np.mean(x_success)
    mean_Y = np.mean(y_success)
    std_X = np.std(x_success, ddof=1)
    std_Y = np.std(y_success, ddof=1)

    t_stat, p_value = ttest_ind(x_success, y_success)
    alpha = 0.04
    df = x_cnt + y_cnt - 2
    t_crit = abs(t.ppf(alpha/2, df))

    if (p_value < alpha/2) or (t_stat < -t_crit):
        return True
    else:
        return False
