import streamlit as st
import cv2
from deepface import DeepFace

st.title('Emotion Detection with Streamlit')


models = {
    'emotion': 'EmotionRecognition'
}

# Create a VideoCapture object
cap = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not cap.isOpened():
    st.error("Cannot open webcam.")
else:
    while True:
        # Read a frame from the webcam
        ret, frame = cap.read()

        if not ret:
            st.error("Error reading a frame from the webcam.")
            break

        # Perform emotion analysis
        result = DeepFace.analyze(frame, actions=models)

        # Detect faces
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        faces = faceCascade.detectMultiScale(gray, 1.1, 4)

        # Draw rectangles around faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Display the frame in Streamlit
        st.image(frame, channels="BGR", use_column_width=True)

        if st.button("Quit"):
            break

# Release the camera and close OpenCV window
cap.release()
cv2.destroyAllWindows()

