import tensorflow as tf

x = tf.Variable(initial_value=3.)
with tf.GradientTape() as tape:     # 在 tf.GradientTape() 的上下文内，所有计算步骤都会被记录以用于求导
    y = x ** 3 - 6
y_grad = tape.gradient(y, x)        # 计算y关于x的导数
print(y_grad)
print([y.numpy(), y_grad.numpy()])

y_grad = tape.gradient(y, tf.Variable(initial_value=2.))        # 计算y关于x的导数
print(y_grad)
print([y.numpy(), y_grad.numpy()])