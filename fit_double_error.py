import bces.bces as bb
import nmmn.stats as ns
import numpy as np
import matplotlib.pyplot as plt

'''
这是一个对线性模型y = ax + b进行双边误差拟合的程式；
sigma为我们希望的置信度，默认取3sigma
mode可以在0,1,2,3中取值，0代表x独立变化，1代表y独立变化，2目前不推荐使用，3代表不知道哪个变量独立变化，默认取0
'''

def fit_double_error(x,y,xerr,yerr,sigma=3,mode=0,save=True):
    conf = ns.sig2conf(sigma)
    cov = np.zeros_like(x)
    a, b, aerr, berr, covab = bb.bcesp(x, xerr, y, yerr, cov)
    lcb, ucb, x1 = ns.confband(x, y, a[mode], b[mode], conf=conf)
    plt.errorbar(x, y, xerr=xerr, yerr=yerr, fmt='o', color='k')
    plt.plot(x1, a[mode] * x1 + b[mode], '-k')
    plt.fill_between(x1, lcb, ucb, alpha=0.3, facecolor='orange')
    plt.text(x.min(),y.max(), str('y = %.2f'%a[mode] + 'x' + '%+.2f'%b[mode] ))
    if save:
        plt.savefig('fit_double_error.eps')
    plt.show()

if __name__=='__main__':
    x = np.random.normal(10,5,30)
    y = np.random.normal(10,5,30)
    xerr = np.random.random(30)
    yerr = np.random.random(30)
    fit_double_error(x, y, xerr, yerr, sigma=3, save=False)

