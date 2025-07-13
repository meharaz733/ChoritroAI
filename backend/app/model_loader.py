import tensorflow as tf

def load_my_model():
    model = tf.keras.models.load_model('model.keras')

    return model
