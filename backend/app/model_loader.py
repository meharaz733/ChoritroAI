import tensorflow as tf

def load_my_model():
    model = tf.keras.models.load_model('Model/bangla_character_model_acc_95_89.h5')

    return model
