#! /usr/bin/env python

import numpy as np

DIM = ???




def generate_image(z):
	# generate image! :)
	pass
	## for reference: (from `DCGAN-tensorflow/utils.py`)
	# def visualize(sess, dcgan, config, option):
	#   image_frame_dim = int(math.ceil(config.batch_size**.5))
	#   if option == 0:
	#     z_sample = np.random.uniform(-0.5, 0.5, size=(config.batch_size, dcgan.z_dim))
	#     samples = sess.run(dcgan.sampler, feed_dict={dcgan.z: z_sample})
	#     save_images(samples, [image_frame_dim, image_frame_dim], './samples/test_%s.png' % strftime("%Y%m%d%H%M%S", gmtime()))


def main():
	z = np.rand(DIM)
	generate_image(z)

main()
