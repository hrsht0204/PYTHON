import os
import cv2
import mediapipe as mp
import math
import pyautogui  # Library to simulate keyboard events
import pygetwindow as gw  # To interact with the window

# Initialize MediaPipe and drawing utilities
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Function to calculate angle between three points
def calculate_angle(p1, p2, p3):
    angle = math.degrees(math.atan2(p3.y - p2.y, p3.x - p2.x) - math.atan2(p1.y - p2.y, p1.x - p2.x))
    if angle < 0:
        angle += 360
    return angle

# Function to detect "All Fingers Open" gesture
def is_all_fingers_open(landmarks):
    # Check if all fingers are raised and not spread too far like a "V"
    if landmarks[8].y < landmarks[6].y and landmarks[12].y < landmarks[10].y and landmarks[16].y < landmarks[14].y and landmarks[20].y < landmarks[18].y:
        thumb_angle = calculate_angle(landmarks[0], landmarks[2], landmarks[4])
        if 60 < thumb_angle < 120:  # Not too wide open like a "V"
            return True
    return False

# Function to focus YouTube window
def focus_youtube_window():
    try:
        youtube_window = gw.getWindowsWithTitle("YouTube")[0]  # Get the first window with 'YouTube' in the title
        if youtube_window:
            youtube_window.activate()  # Bring YouTube window into focus
    except IndexError:
        print("No YouTube window found.")

# Start video capture for hand gestures
cap = cv2.VideoCapture(0)

# To keep track of video playback state (playing or paused)
is_paused = False

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            landmarks = hand_landmarks.landmark

            # Detect the "All Fingers Open" gesture
            if is_all_fingers_open(landmarks):
                if not is_paused:
                    print("All fingers open detected! Pausing the YouTube video.")
                    focus_youtube_window()  # Ensure YouTube window is in focus
                    pyautogui.press('space')  # Simulate pressing the spacebar (pauses YouTube video)
                    is_paused = True
            else:
                if is_paused:
                    print("Gesture not detected. Resuming the YouTube video.")
                    focus_youtube_window()  # Ensure YouTube window is in focus
                    pyautogui.press('space')  # Simulate pressing the spacebar (resumes YouTube video)
                    is_paused = False

    # Show the hand gesture frame
    cv2.imshow("Hand Gesture Recognition", frame)

    # Stop the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
hands.close()
