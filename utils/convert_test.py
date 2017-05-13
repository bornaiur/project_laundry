import tensorflow as tf
import os


def _get_filenames():

  photo_filenames = []

  for filename in os.listdir('downloaded'):
      path = os.path.join('downloaded', filename)
      photo_filenames.append(path)

  return photo_filenames

if __name__ == "__main__":
  p = _get_filenames()
  #print(p)

  decode_jpeg_data = tf.placeholder(dtype=tf.string)
  decode_jpeg = tf.image.decode_jpeg(decode_jpeg_data, channels=3)

  sess = tf.Session()
  sess.run(tf.global_variables_initializer())
  for filename in p:
    image_data = tf.gfile.FastGFile(filename, 'r').read()
    try:
      image = sess.run(decode_jpeg, feed_dict={decode_jpeg_data: image_data})
    except:
      print(filename)
      pass  

