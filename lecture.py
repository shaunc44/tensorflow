import tensorflow as tf

# This is creates the structure
# node_first = tf.constant(10.0, tf.float32)
# node_second = tf.constant(20.0, tf.float32)
# division = node_first / node_second

# with tf.Session() as sess:
#     output = sess.run([node_first, node_second])
#     # output = sess.run(division)
#     print(output)


place_a = tf.placeholder(tf.float32)
place_b = tf.placeholder(tf.float32)
addition = place_a + place_b

with tf.Session() as sess:
    output = sess.run(addition, {place_a:[1,2,3], place_b:[4,5,6]})
    print(output)


"""
Add weights and biases
"""
import tensorflow as tf

W = tf.Variable([0.5], tf.float32)
b = tf.Variable([-0.1], tf.float32)
x = tf.placeholder(tf.float32)

model = W * x + b

initializer = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(initializer)
    output = sess.run(model, {x:[5,6,7,8]})
    print(output)




























