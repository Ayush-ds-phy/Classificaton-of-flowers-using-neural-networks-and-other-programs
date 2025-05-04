#Classification of flowers Using TensorFlow

import pandas as pd
import tensorflow as tf
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load the classic Iris dataset from sklearn
iris = load_iris()

# Pull out the features and labels
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = pd.Series(iris.target)

# Peek at the first few rows of the data
print("Here's what the data looks like:")
print(X.head())

# Let's scale the feature values so the model doesn't get confused by big/small numbers
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split the data so we can train on some and test on the rest
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

# Time to build a simple neural network with TensorFlow/Keras
model = tf.keras.Sequential([
    tf.keras.layers.Dense(10, activation='relu', input_shape=(X_train.shape[1],)),
    tf.keras.layers.Dense(8, activation='relu'),
    tf.keras.layers.Dense(3, activation='softmax')  # 3 types of flowers
])

# Compile the model with common settings for a classification task
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# Let’s train the model. This is where the magic happens!
print("\nTraining the model. Please wait...")
model.fit(X_train, y_train, epochs=30, verbose=1)

# Once it's trained, let's see how it performs on the test data
loss, accuracy = model.evaluate(X_test, y_test, verbose=0)
print(f"\nAccuracy on test data: {accuracy * 100:.2f}%")

# Try a prediction on a sample flower
new_flower = [[5.1, 3.5, 1.4, 0.2]]  # Looks like a Setosa maybe?
new_flower_scaled = scaler.transform(new_flower)
prediction = model.predict(new_flower_scaled)
predicted_class = tf.argmax(prediction[0]).numpy()

print(f"\nThis flower is most likely a: {iris.target_names[predicted_class].title()}")
