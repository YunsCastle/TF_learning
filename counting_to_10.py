import tensorflow as tf

# create a variable, reger to it as 'state' and set it to 0
state = tf.Variable(0)

# set one to a constant set to 1
one = tf.constant(1)

# update phase adds state and one and then assigns to state
addition = tf.add(state, one)
update = tf.assign(state, addition)

# create a sesion
with tf.Session() as sess:
    # initialize session variables
    sess.run(tf.global_variables_initializer())
    print('The starting state is', sess.run(state))

    print('Run the update 10 times...')
    for _ in range(10):
        # execute the update
        sess.run(update)
    print('The ende state is', sess.run(state))


