import numpy as np
import matplotlib.pyplot as plt
from scipy.special import factorial

def plot_poisson_pmf(lambda_param=8, max_l=20):
    """绘制泊松分布的概率质量函数
    
    参数:
        lambda_param (float): 泊松分布参数λ
        max_l (int): 最大的l值
    """
    l_values = np.arange(max_l)
    pmf = (lambda_param**l_values * np.exp(-lambda_param)) / factorial(l_values)
    
    plt.figure(figsize=(10, 6))
    plt.plot(l_values, pmf, 'bo-', label='Theoretical Distribution')
    plt.title(f'Poisson Probability Mass Function (λ={lambda_param})')
    plt.xlabel('l')
    plt.ylabel('p(l)')
    plt.grid(True)
    plt.legend()
    return pmf

def simulate_coin_flips(n_experiments=10000, n_flips=100, p_head=0.08):
    """模拟多组抛硬币实验
    
    参数:
        n_experiments (int): 实验组数N
        n_flips (int): 每组抛硬币次数
        p_head (float): 正面朝上的概率
        
    返回:
        ndarray: 每组实验中正面朝上的次数
    """
    results = []  #记录硬币正面朝上的次数
    for i in range(n_experiments):
        coins = np.random.choice([0,1],n_flips, p=[1-p_head,p_head]) #抛硬币100次
        results.append(coins.sum())

    return np.array(results)

def compare_simulation_theory(n_experiments=10000, lambda_param=8):
    """比较实验结果与理论分布
    
    参数:
        n_experiments (int): 实验组数
        lambda_param (float): 泊松分布参数λ
    """
    # 进行实验模拟
    results = simulate_coin_flips(n_experiments)
    
    # 计算理论分布
    max_l = max(int(lambda_param * 2), max(results) + 1)
    l_values = np.arange(max_l)
    pmf = (lambda_param**l_values * np.exp(-lambda_param)) / factorial(l_values)
    

    plt.show()
