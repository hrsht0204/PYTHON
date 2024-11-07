import os
import cv2
import mediapipe as mp
import math

# Path to the gestures folder where images will be saved
gestures_folder = "C:/Users/Hari krishan/Pictures/python/Hand gesture machine/Gestures"

# Create the 'gestures' folder if it doesn't exist
if not os.path.exists(gestures_folder):
    os.makedirs(gestures_folder)

# Initialize MediaPipe and drawing utilities
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Start video capture
cap = cv2.VideoCapture(0)

# Function to calculate angle between three points
def calculate_angle(p1, p2, p3):
    angle = math.degrees(math.atan2(p3.y - p2.y, p3.x - p2.x) - math.atan2(p1.y - p2.y, p1.x - p2.x))
    if angle < 0:
        angle += 360
    return angle

# Function to detect "Victory" sign (index and middle fingers forming a "V")
def is_victory_sign(landmarks):
    # Check if the index and middle fingers are both up and making a V shape
    # Angle between index and middle finger should be roughly 90 degrees
    # Calculate the angle between the thumb, index, and middle finger
    angle_index_middle = calculate_angle(landmarks[5], landmarks[9], landmarks[13])
    
    # Check if the index and middle fingers form a "V" shape (angle should be around 90°)
    if angle_index_middle < 50 or angle_index_middle > 140:
        return False

    # Also check if index and middle fingers are raised (relative to their base joints)
    if landmarks[8].y < landmarks[6].y and landmarks[12].y < landmarks[10].y:
        return True

    return False

# Start the video loop
while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    # Convert to RGB for MediaPipe
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks, hand_info in zip(results.multi_hand_landmarks, results.multi_handedness):
            # Draw landmarks and connections on the hand
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Extract the positions of the key finger landmarks
            landmarks = hand_landmarks.landmark

            # Detect if the Victory sign is detected
            if is_victory_sign(landmarks):
                print("Victory sign detected!")
                # Save the image to the 'gestures' folder
                image_filename = f"{gestures_folder}/victory_sign_picture.jpg"
                success = cv2.imwrite(image_filename, frame)

                # Check if the image was saved successfully
                if success:
                    print(f"Victory sign picture saved successfully: {image_filename}")
                else:
                    print("Failed to save picture")
            
            # Hand Label - Left or Right
            hand_label = hand_info.classification[0].label
            label = f"Hand: {hand_label}"

            # Display the label on the frame
            cv2.putText(frame, label, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2)

    # Show the frame with the hand landmarks and labels
    cv2.imshow("Hand Gesture Recognition", frame)

    # Stop the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
hands.close()
