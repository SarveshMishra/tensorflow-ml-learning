# To use tensorflow use python 3.5 or 3.6

import tensorflow as tf

const_node_1 = tf.constant(1.0, dtype=tf.float32)

const_node_2 = tf.constant(2.0)
print(const_node_1)

session = tf.Session()
print(session.run([const_node_1, const_node_2]))

adder_node = tf.add(const_node_2, const_node_1)
print(session.run(adder_node))
