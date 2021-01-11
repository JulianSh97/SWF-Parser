from reliability.Other_functions import make_right_censored_data
import pickle
from reliability.Fitters import Fit_Everything
from reliability.Fitters import Fit_Weibull_3P

f=open('vars.pkl','rb')
PDF_Inter,CDF_Inter,PDR_Runtime,CDF_Runtimes=pickle.load(f)
f.close()
data = make_right_censored_data(CDF_Runtimes, threshold=0.9)  # right censor the data
results = Fit_Weibull_3P(failures=CDF_Runtimes)  # fit all the models
print('The best fitting distribution was', results.best_distribution_name, 'which had parameters', results.best_distribution.parameters)
