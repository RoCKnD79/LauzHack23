from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout

def build_model(sequence_length, num_features):
    """
    Builds and compiles a Keras model for a LSTM network, with the following architecture:
        - 1 (or more) LSTM layer(s) with 128 units
        - 1 (or more) additional LSTM layer(s) with 64 units (optional)
        - 1 final LSTM layer with 64 units
        - 1 Dense output layer with 4 units (for multiclass classification)
    :param sequence_length: The length of our sequence (i.e. the number of timesteps)
    :param num_features: The number of features in our dataset
    :return: A Keras model instance
    """

    # Define the LSTM model
    model = Sequential()

    # Add LSTM layer(s)
    model.add(LSTM(units=128, input_shape=(sequence_length, num_features), return_sequences=True))
    model.add(Dropout(0.2))  # Dropout for regularization

    # Add more LSTM layers if needed
    # model.add(LSTM(units=64, return_sequences=True))  # Example additional LSTM layer

    # Add a final LSTM layer
    model.add(LSTM(units=64))  # The final LSTM layer
    model.add(Dropout(0.2))  # Dropout for regularization

    # Output layer for multiclass classification
    model.add(Dense(units=4, activation='softmax'))  # 4 classes (Angry, Stressed, Focused, Sleepy)

    # Compile the model
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    return model