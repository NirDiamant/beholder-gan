parser = argparse.ArgumentParser()
parser.add_argument('--results_dir', '-results_dir', help='name of training experiment folder', default='dean_cond_batch16', type=str)
G, D, Gs = misc.load_network_pkl(args.results_dir, None)
image_name = 'test.png'
start_img = Image.open(image_name)
start_img.resize((128, 128), Image.ANTIALIAS)
start_img_np = np.array(start_img)/255
fz = tf.Variable(start_img_np, tf.float32)
fz = tf.expand_dims(fz, 0)
fz = tf.transpose(fz,perm=[0,3,2,1])
fz = tf.cast(fz,tf.float32)

# Define the optimization problem
# generator = hub.Module("https://tfhub.dev/google/progan-128/1")
generator = Gs
latents = misc.random_latents(1, Gs, random_state=np.random.RandomState(100))
zp = latents

# print("latents shape: {}".format(latents.shape))
# print("latents type: {}".format(type(latents)))

latents_tf =tf.Variable(latents)
# print("latents_tf type: {}".format(type(latents_tf)))



labels = np.zeros([1, 10], np.float32)
labels[0][5] = 1.0

fzp = generator.run(zp, labels, minibatch_size=1, num_gpus=1, out_mul=127.5, out_add=127.5, out_shrink=1, out_dtype=np.uint8)
print("fzp shape: {}".format(fzp.shape))
fzp = tf.Variable(fzp)
fzp = tf.cast(fzp,tf.float32)

zp = tf.Variable(zp)
# fzp = generator.run(zp)
loss = tf.losses.mean_squared_error(labels=fz, predictions=fzp)

# Decayed gradient descent
global_step = tf.Variable(0, trainable=False)
starter_learning_rate = 0.99
learning_rate = tf.train.exponential_decay(starter_learning_rate,
                                           global_step,
                                           10000, 0.005)
opt = tf.train.GradientDescentOptimizer(learning_rate)
# Optimize on the variable zp
train = opt.minimize(loss, var_list=zp, global_step=global_step)

sess = tf.Session()
sess.run(tf.global_variables_initializer())
for i in range(200): # Use more iterations (10000)
  # If we know the original latent vector, we can also compute
  # how far the recovered vector is from it
  _, loss_value, zp_val, eta = sess.run((train, loss, zp, learning_rate))
  # z_loss = np.sqrt(np.sum(np.square(zp_val - start_zp))/len(zp_val[0]))
  # print("%03d) eta=%03f, loss = %f, z_loss = %f" % (i, eta, loss_value, z_loss))
  print("%03d) eta=%03f, loss = %f" % (i, eta, loss_value))
# Save the recovered latent vector
zp_val = sess.run(zp)
np.save("zp_rec", zp_val)

sess = tf.Session()
with sess.as_default():
    zp = zp.eval()


# Print out the corresponding image out of the recovered
# latent vector
# imgs = sess.run(generator(zp)
imgs = sess.run(generator(zp, labels, minibatch_size=1, num_gpus=1, out_mul=127.5, out_add=127.5, out_shrink=1, out_dtype=np.uint8))
imgs = (imgs * 255).astype(np.uint8)
Image.fromarray(imgs[0]).save("foo_rec.png")
#