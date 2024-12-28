# Real-Time-Paint
This project implements a hand tracking and drawing application using OpenCV and Mediapipe's hand detection model. The application enables users to draw, erase, and select different brush colors based on hand gestures.

Features:
Hand Gesture Recognition: Detects finger positions and gestures to control drawing actions.
Brush and Eraser: Switches between drawing and erasing modes using hand gestures.
Color Palette: Allows users to select different brush colors using hand gestures to interact with a predefined menu bar.
Real-time Drawing: Users can draw or erase on the screen in real-time, making the app suitable for digital whiteboarding or creative expression.

# Technologies Used:
Python: Programming language used for development.
OpenCV: For capturing video and image processing.
Mediapipe: Used for hand tracking and gesture detection.
NumPy: For handling image arrays and manipulation.

# How It Works:
The webcam captures the live video feed, which is processed frame by frame.
Hand landmarks are detected and tracked using Mediapipe's hand detection model.
Based on the position of specific finger landmarks, the app detects whether the user is in drawing mode or erasing mode.
The app also detects gestures to select brush colors from the menu bar displayed at the top of the screen.
The user can draw or erase lines on the canvas by moving their hand, with the color and thickness determined by the selected settings.
