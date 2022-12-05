#scikit-learning
import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt
#準備訓練與測試的資料
x_value=pd.DataFrame([0,1,2])
y_value=pd.DataFrame([0,0.3,0.6])
x_test=pd.DataFrame([-1,3,5])

body_reg=linear_model.LinearRegression()
body_reg.fit(x_value,y_value)

y_test_predict=body_reg.predict(x_test)
print("body_reg.predict(x_test)",y_test_predict)
print('------------------')
print(x_test)
#gif
plt.scatter(x_value,y_value)
plt.scatter(x_test,y_test_predict,color='red')
plt.plot(x_test,y_test_predict,color='green')
plt.show()

