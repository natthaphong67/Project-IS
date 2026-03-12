import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

IMG_SIZE = 200
BATCH_SIZE = 32

# path โมเดล
model_path = "/Users/mac/Programming/Project AI/AI Card/card_classifier.h5"

# path test dataset
test_dir = "/Users/mac/Programming/Project AI/AI Card/dataset/test"

# โหลดโมเดล
model = tf.keras.models.load_model(model_path)

# เตรียม test data
test_gen = ImageDataGenerator(rescale=1./255)

test_data = test_gen.flow_from_directory(
    test_dir,
    target_size=(IMG_SIZE, IMG_SIZE),
    batch_size=BATCH_SIZE,
    class_mode="categorical",
    shuffle=False
)

# ประเมินโมเดล
loss, accuracy = model.evaluate(test_data)

print("\nTest Accuracy:", accuracy)
print("Test Loss:", loss)