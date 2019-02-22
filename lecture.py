import tensorflow as tf

# This is creates the structure
node_first = tf.constant(10.0, tf.float32)
node_second = tf.constant(20.0, tf.float32)
division = node_first / node_second

with tf.Session() as sess:
    output = sess.run([node_first, node_second])
    # output = sess.run(division)
    print(output)

