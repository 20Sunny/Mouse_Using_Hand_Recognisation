import cv2
import mediapipe as mp
import pyautogui
cap = cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()
index_y = 0
while True:
    _, frame = cap.read()
    frame =cv2.flip(frame, 1)
    frame_height, frame_width, _ = frame.shape
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)
            landmarks = hand.landmark
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x*frame_width)
                y = int(landmark.y*frame_height)
                if id ==8:
                    cv2.circle(img=frame, center=(x,y), radius=25, color=(255,255,255))
                    cv2.circle(img=frame, center=(x,y), radius=24, color=(255,255,255))
                    cv2.circle(img=frame, center=(x,y), radius=20, color=(255,255,255))
                    cv2.circle(img=frame, center=(x,y), radius=19, color=(255,255,255))
                    cv2.circle(img=frame, center=(x,y), radius=18, color=(255,255,255))
                    cv2.circle(img=frame, center=(x,y), radius=17, color=(255,255,255))
                    cv2.circle(img=frame, center=(x,y), radius=16, color=(255,255,255))
                    cv2.circle(img=frame, center=(x,y), radius=15, color=(255,255,255))
                    index_x = int(screen_width/frame_width*x)
                    index_y =int(screen_height/frame_height*y)
                    pyautogui.moveTo(index_x,index_y)
                if id == 4:
                    cv2.circle(img=frame, center=(x,y), radius=10, color=(0,255,255))
                    thumb_x = int(screen_width/frame_width*x)
                    thumb_y = int(screen_height/frame_height*y)
                    print('max',abs(index_y - thumb_y))
                    if abs(index_y - thumb_y) < 80:
                        pyautogui.click()
                if id == 20:
                    cv2.circle(img=frame, center=(x,y), radius=10, color=(0,255,255))
                    right_x = screen_width/frame_width*x
                    right_y = screen_height/frame_height*y
                    print('min',abs(thumb_y - right_y))
                    if abs(index_y - right_y) < 80:
                        pyautogui.rightClick()
    cv2.imshow('Virtual Mouse', frame)
    cv2.waitKey(1)