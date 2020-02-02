# 牛顿法求 x^3 - 6 的根

# 初始值
x = 3
## 随便初始化一个值
x_1 = 100
# 误差值
d = 0.0000001
# 函数
def fun_y(x):
  return x ** 10 - 100

# 计算导数
def fun_grad(x):
  return 10 * x**9

# 记录迭代次数
n = 1

while True:
  # 计算y关于x的导数
  x_1 = x - fun_y(x) / fun_grad(x)
  if (abs(x_1 - x) > d):
    x = x_1
  else: 
    break
  print('n: ', n)
  n = n + 1
print('x', x)