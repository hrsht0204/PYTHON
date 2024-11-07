import os
import cv2
import mediapipe as mp
import math

# Path to the gestures folder where images will be saved
gestures_folder = r"C:\Users\Hari krishan\Pictures\python\Hand gesture machine\Gestures"

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
    # Calculate the angle between index and middle finger (should form a "V" shape)
    angle_index_middle = calculate_angle(landmarks[5], landmarks[9], landmarks[13])
    
    # Check if the angle is within the acceptable range for a "V" shape
    if angle_index_middle < 50 or angle_index_middle > 140:
        return False

    # Check if both the index and middle fingers are raised above their base joints
    if landmarks[8].y < landmarks[6].y and landmarks[12].y < landmarks[10].y:
        # Ensure the other fingers are not raised (for clarity of victory sign)
        if landmarks[16].y > landmarks[14].y and landmarks[20].y > landmarks[18].y:
            return True
    return False

# Function to count raised fingers
def count_raised_fingers(landmarks, hand_info):
    raised_fingers = 0
    
    # Determine if it's left or right hand
    is_left_hand = hand_info.classification[0].label == 'Left'
    
    # Thumb (Landmarks 4, 2, 0) - Check if the thumb is open using angle
    thumb_angle = calculate_angle(landmarks[0], landmarks[2], landmarks[4])  # Angle between wrist, base, and tip of the thumb
    
    # Check thumb for left hand and right hand with different thresholds
    if is_left_hand:
        if thumb_angle > 160:  # Left hand thumb open angle check
            raised_fingers += 1
    else:
        if thumb_angle < 60:  # Right hand thumb open angle check (smaller angle)
            raised_fingers += 1

    # Index (Landmarks 8, 6)
    if landmarks[8].y < landmarks[6].y:  # Index tip (8) above the index base (6)
        raised_fingers += 1

    # Middle (Landmarks 12, 10)
    if landmarks[12].y < landmarks[10].y:  # Middle tip (12) above the middle base (10)
        raised_fingers += 1

    # Ring (Landmarks 16, 14)
    if landmarks[16].y < landmarks[14].y:  # Ring tip (16) above the ring base (14)
        raised_fingers += 1

    # Pinky (Landmarks 20, 18)
    if landmarks[20].y < landmarks[18].y:  # Pinky tip (20) above the pinky base (18)
        raised_fingers += 1

    return raised_fingers

# Function to determine which hand it is based on the wrist landmark (landmarks[0])
def get_hand_label(landmarks):
    wrist_x = landmarks[0].x  # Get the x-coordinate of the wrist
    if wrist_x < 0.5:  # If the wrist is on the left side of the frame, it's the left hand
        return "Left Hand"
    else:  # If the wrist is on the right side of the frame, it's the right hand
        return "Right Hand"

# Start the video loop
while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks, hand_info in zip(results.multi_hand_landmarks, results.multi_handedness):
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            landmarks = hand_landmarks.landmark

            # Get the correct hand label based on the wrist's x-coordinate
            hand_label = get_hand_label(landmarks)

            # Display hand label (Left/Right) on the screen
            cv2.putText(frame, hand_label, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2)

            # Count and display raised fingers (pass hand_info here)
            raised_fingers = count_raised_fingers(landmarks, hand_info)
            cv2.putText(frame, f"Fingers: {raised_fingers}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

            # Detect Victory sign and save the picture
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
