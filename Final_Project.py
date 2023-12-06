import cv2
import mediapipe as mp
import numpy as np
import time
import math

mp_pose = mp.solutions.pose
mp_draw = mp.solutions.drawing_utils

pose = mp_pose.Pose()
cap = cv2.VideoCapture("gait_abnormal_01.mp4")
# cap = cv2.VideoCapture("gait_normal_01.mp4")

# Set the video be low frame rate
fourcc = cv2.VideoWriter_fourcc(*'XVID')
fps = 45
video_writer = cv2.VideoWriter('low_frame_rate_video.mp4', fourcc, fps, (1600, 900))

# mediapipe connect point
rl1, rl2, rl3 = 24, 26, 28
ll1, ll2, ll3 = 23, 25, 27
left_ear, left_shoulder, left_hip = 8, 12, 24
ra1, ra2, ra3 = 11, 13, 15
la1, la2, la3 = 12, 14, 16


right_toe_y = []
right_toe_x = []
left_toe_y = []
left_toe_x = []
left_heel_x = []
left_heel_y = []
right_heel_x = []
right_heel_y = []
right_arm_x = []
right_arm_y = []
left_arm_x = []
left_arm_y = []


check_lead_foot = 0 #boolean
no_total_frame = 0
no_neck_frame = 0
no_rightleg_frame = 0
no_leftleg_frame = 0
no_limping_right = 0
no_limping_left = 0
no_swing_right = 0
no_swing_left = 0
lead_foot_right = 0
lead_foot_left = 0

initial_right_swing_frame = []
initial_left_swing_frame = []

no_total_cycle = 0
phase_of_right = ""
phase_of_left = ""

while True:

    # read videos
    ret, img = cap.read()
    cv2.imshow('Frame', img)
    cv2.waitKey(1)
    results = pose.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    mp_draw.draw_landmarks(img, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
    
    h, w, c = img.shape
    opImg = np.zeros([h, w, c])
    opImg.fill(128)
    mp_draw.draw_landmarks(opImg, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                           mp_draw.DrawingSpec((255, 0, 0), 2, 2),
                           mp_draw.DrawingSpec((255, 0, 255), 2, 2))

    ########################################################################### Start analyze ################################################################################
    # Read data by mediapipe
    new_lmList = []
    if results.pose_landmarks:
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h, w, c = img.shape
            cx, cy = int(lm.x * w), int(lm.y * h)
            new_lmList.append([id, cx, cy])
            cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)

    if len(new_lmList) != 0:
        no_total_frame += 1
        cv2.putText(img, str(no_total_frame), (50, 50),
                        cv2.FONT_HERSHEY_PLAIN, 1, (0, 256, 0), 2)

        # Right leg
        rx1, ry1 = new_lmList[rl1][1:]
        rx2, ry2 = new_lmList[rl2][1:]
        rx3, ry3 = new_lmList[rl3][1:]
        # Calculate the angle right leg
        right_angle = math.degrees(math.atan2(ry3 - ry2, rx3 - rx2) - math.atan2(ry1 - ry2, rx1 - rx2))
        if right_angle < 0:
            right_angle += 360
        
        # Left leg
        lx1, ly1 = new_lmList[ll1][1:]
        lx2, ly2 = new_lmList[ll2][1:]
        lx3, ly3 = new_lmList[ll3][1:]
        # Calculate the angle left leg
        left_angle = math.degrees(math.atan2(ly3 - ly2, lx3 - lx2) - math.atan2(ly1 - ly2, lx1 - lx2))
        if left_angle < 0:
            left_angle += 360

        # Right arm
        rax1, ray1 = new_lmList[ra1][1:]
        rax2, ray2 = new_lmList[ra2][1:]
        rax3, ray3 = new_lmList[ra3][1:]
        # Calculate the angle right arm
        right_arm_angle = math.degrees(math.atan2(ray3 - ray2, rax3 - rax2) - math.atan2(ray1 - ray2, rax1 - rax2))
        if right_arm_angle < 0:
            right_arm_angle += 360
        
        # Left arm
        lax1, lay1 = new_lmList[la1][1:]
        lax2, lay2 = new_lmList[la2][1:]
        lax3, lay3 = new_lmList[la3][1:]
        # Calculate the angle left arm
        left_arm_angle = math.degrees(math.atan2(lay3 - lay2, lax3 - lax2) - math.atan2(lay1 - lay2, lax1 - lax2))
        if left_arm_angle < 0:
            left_arm_angle += 360

        # Showing line and angle two legs
        cv2.line(img, (rx1, ry1), (rx2, ry2), (255, 255, 255), 3)
        cv2.line(img, (rx3, ry3), (rx2, ry2), (255, 255, 255), 3)
        cv2.circle(img, (rx1, ry1), 10, (0, 0, 255), cv2.FILLED)
        cv2.circle(img, (rx1, ry1), 15, (0, 0, 255), 2)
        cv2.circle(img, (rx2, ry2), 10, (0, 0, 255), cv2.FILLED)
        cv2.circle(img, (rx2, ry2), 15, (0, 0, 255), 2)
        cv2.circle(img, (rx3, ry3), 10, (0, 0, 255), cv2.FILLED)
        cv2.circle(img, (rx3, ry3), 15, (0, 0, 255), 2)
        cv2.putText(img, str(int(right_angle)), (rx2 - 50, ry2 + 50),
                    cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
        cv2.line(img, (lx1, ly1), (lx2, ly2), (255, 255, 255), 3)
        cv2.line(img, (lx3, ly3), (lx2, ly2), (255, 255, 255), 3)
        cv2.circle(img, (lx1, ly1), 10, (0, 255, 0), cv2.FILLED)
        cv2.circle(img, (lx1, ly1), 15, (0, 255, 0), 2)
        cv2.circle(img, (lx2, ly2), 10, (0, 255, 0), cv2.FILLED)
        cv2.circle(img, (lx2, ly2), 15, (0, 255, 0), 2)                 
        cv2.circle(img, (lx3, ly3), 10, (0, 255, 0), cv2.FILLED)
        cv2.circle(img, (lx3, ly3), 15, (0, 255, 0), 2)
        cv2.putText(img, str(int(left_angle)), (lx2 - 50, ly2 + 50),
                    cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
        
        # Showing line and angle two arms
        cv2.line(img, (rax1, ray1), (rax2, ray2), (255, 255, 255), 3)
        cv2.line(img, (rax3, ray3), (rax2, ray2), (255, 255, 255), 3)
        cv2.circle(img, (rax1, ray1), 10, (0, 0, 255), cv2.FILLED)
        cv2.circle(img, (rax1, ray1), 15, (0, 0, 255), 2)
        cv2.circle(img, (rax2, ray2), 10, (0, 0, 255), cv2.FILLED)
        cv2.circle(img, (rax2, ray2), 15, (0, 0, 255), 2)
        cv2.circle(img, (rax3, ray3), 10, (0, 0, 255), cv2.FILLED)
        cv2.circle(img, (rax3, ray3), 15, (0, 0, 255), 2)
        cv2.putText(img, str(int(right_angle)), (rax2 - 50, ray2 + 50),
                    cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
        cv2.line(img, (lax1, lay1), (lax2, lay2), (255, 255, 255), 3)
        cv2.line(img, (lax3, lay3), (lax2, lay2), (255, 255, 255), 3)
        cv2.circle(img, (lax1, lay1), 10, (0, 255, 0), cv2.FILLED)
        cv2.circle(img, (lax1, lay1), 15, (0, 255, 0), 2)
        cv2.circle(img, (lax2, lay2), 10, (0, 255, 0), cv2.FILLED)
        cv2.circle(img, (lax2, lay2), 15, (0, 255, 0), 2)                 
        cv2.circle(img, (lax3, lay3), 10, (0, 255, 0), cv2.FILLED)
        cv2.circle(img, (lax3, lay3), 15, (0, 255, 0), 2)
        cv2.putText(img, str(int(left_angle)), (lax2 - 50, lay2 + 50),
                    cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
        
        ############################################################################### Hip hike ################################################################################## 
        #data for check Hip hike (some leg always swing phase)
        if 200 > right_angle > 160 :
            no_rightleg_frame += 1
        if 200 > left_angle > 160 :
            no_leftleg_frame += 1
        # Hip hike 99% of one leg always swing phase
        if no_rightleg_frame / no_total_frame > 0.99 or no_leftleg_frame / no_total_frame > 0.99:
            cv2.putText(img, "Gait abnormal - risk : Hip hike", (50, 450),
                        cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 256), 2)
        
        ############################################################################# Neck pain ###################################################################################
        # display angle of neck / bent
        left_ear_x, left_ear_y = new_lmList[left_ear][1:]
        left_shoulder_x, left_shoulder_y = new_lmList[left_shoulder][1:]
        left_hip_x, left_hip_y = new_lmList[left_hip][1:]
        left_ear_angle = math.degrees(math.atan2(left_hip_y - left_shoulder_y, left_hip_x - left_shoulder_x) - math.atan2(left_ear_y - left_shoulder_y, left_ear_x - left_shoulder_x))

        if left_ear_angle < 0:
            left_ear_angle += 360

        cv2.line(img, (left_ear_x, left_ear_y), (left_shoulder_x, left_shoulder_y), (255, 255, 255), 3)
        cv2.line(img, (left_hip_x, left_hip_y), (left_shoulder_x, left_shoulder_y), (255, 255, 255), 3)
        cv2.circle(img, (left_ear_x, left_ear_y), 10, (0, 0, 255), cv2.FILLED)
        cv2.circle(img, (left_ear_x, left_ear_y), 15, (0, 0, 255), 2)
        cv2.circle(img, (left_shoulder_x, left_shoulder_y), 10, (0, 0, 255), cv2.FILLED)
        cv2.circle(img, (left_shoulder_x, left_shoulder_y), 15, (0, 0, 255), 2)
        cv2.circle(img, (left_hip_x, left_hip_y), 10, (0, 0, 255), cv2.FILLED)
        cv2.circle(img, (left_hip_x, left_hip_y), 15, (0, 0, 255), 2)
        cv2.putText(img, str(int(left_ear_angle)-180), (left_shoulder_x - 50, left_shoulder_y + 50),
                    cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)

        if left_ear_angle - 180 > 30 or left_ear_angle - 180 < -30 :
            no_neck_frame += 1

        if no_neck_frame / no_total_frame > 0.7 :
            cv2.putText(img, "Gait abnormal - risk : Neck pain", (50, 400),
                        cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 256), 2)
          
        ############################################################################# Gait limping ################################################################################
        # Gait limping read toe and heel point
        right_toe_index_x, right_toe_index_y = new_lmList[32][1:]
        right_heel_index_x, right_heel_index_y = new_lmList[30][1:]
        left_toe_index_x, left_toe_index_y = new_lmList[31][1:]
        left_heel_index_x, left_heel_index_y = new_lmList[29][1:]
        right_toe_y.append(right_toe_index_y)
        right_toe_x.append(right_toe_index_x)
        right_heel_x.append(right_heel_index_x)
        right_heel_y.append(right_heel_index_y)
        left_toe_y.append(left_toe_index_y)
        left_toe_x.append(left_toe_index_x)
        left_heel_x.append(left_heel_index_x)
        left_heel_y.append(left_heel_index_y)
        # print("X : ", right_toe_index_x, "     Y : ", right_toe_index_y)

        if left_toe_index_x > left_heel_index_x: #Check gait side (right side)
            if left_toe_index_x > right_heel_index_x:
                check_lead_foot = 1 #Left foot is lead
                no_limping_left += 1
            else:
                check_lead_foot = 0 #Right foot is lead
                no_limping_right += 1
        elif left_toe_index_x < left_heel_index_x:
            if left_toe_index_x < right_heel_index_x:
                check_lead_foot = 1 #Left foot is lead
                no_limping_left += 1
            else:
                check_lead_foot = 0 #Right foot is lead
                no_limping_right += 1

        if no_limping_right / no_total_frame > 0.80 or no_limping_left / no_total_frame > 0.80:
            cv2.putText(img, "Gait abnormal - risk : Limping", (50, 425),
                        cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 256), 2)
        if check_lead_foot:
            cv2.putText(img, "Lead foot : left", (50, 350),
                        cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 256), 2)
        else:
            cv2.putText(img, "Lead foot : right", (50, 350),
                        cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 256), 2)
        
        ############################################################################# No arm swing ################################################################################
        # Gait limping read hand points and using feet points
        right_hand_index_x, right_hand_index_y = new_lmList[16][1:]
        left_hand_index_x, left_hand_index_y = new_lmList[15][1:]
        right_arm_x.append(right_hand_index_x)
        right_arm_y.append(right_hand_index_y)
        left_arm_x.append(left_hand_index_x)
        left_arm_y.append(left_hand_index_y)

        if left_toe_index_x > left_heel_index_x:
            if check_lead_foot :
                lead_foot_left += 1
                if left_toe_index_x > right_hand_index_x and right_heel_index_x < right_hand_index_x:
                    no_swing_right +=1
                if left_toe_index_x > left_hand_index_x and right_heel_index_x < left_hand_index_x:
                    no_swing_left +=1
            else:
                lead_foot_right += 1
                if right_toe_index_x > right_hand_index_x and left_heel_index_x < right_hand_index_x:
                    no_swing_right +=1
                if left_toe_index_x > left_hand_index_x and right_heel_index_x < left_hand_index_x:
                    no_swing_left +=1
        else:
            if check_lead_foot :
                lead_foot_left += 1
                if left_toe_index_x < right_hand_index_x and right_heel_index_x > right_hand_index_x:
                    no_swing_right +=1
                if left_toe_index_x < left_hand_index_x and right_heel_index_x > left_hand_index_x:
                    no_swing_left +=1
            else:
                lead_foot_right += 1
                if right_toe_index_x < right_hand_index_x and left_heel_index_x > right_hand_index_x:
                    no_swing_right +=1
                if left_toe_index_x < left_hand_index_x and right_heel_index_x > left_hand_index_x:
                    no_swing_left +=1
        
        if (no_swing_right / no_total_frame > 0.95 and (lead_foot_right / no_total_frame > 0.8 or lead_foot_left / no_total_frame > 0.8)) or (no_swing_left / no_total_frame > 0.95 and (lead_foot_right / no_total_frame > 0.8 or lead_foot_left / no_total_frame > 0.8)):
            cv2.putText(img, "Gait abnormal - risk : Parkinson", (50, 475),
                        cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 256), 2)



        # if len(right_toe_y) > 1:
        #     # start swing phase of right side
        #     if right_toe_y[no_total_frame-2] - right_toe_y[no_total_frame-1] > 10:
        #         initial_right_swing_frame.append(no_total_frame)
        #         no_total_cycle += 1
        #         phase_of_right = "swing phase"

        #     # start swing phase of left side
        #     elif left_toe_y[no_total_frame-2] - left_toe_y[no_total_frame-1] > 10:
        #         initial_left_swing_frame.append(no_total_frame)
        #         phase_of_right = "stance phase"

        #         # กะเผลก
        #         # if right_foot_x[no_total_frame-2] > left_foot_x[no_total_frame-2] :
        #         #     cv2.putText(img, "stumblingly", (50, 500),
        #         #         cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 256), 2)
        #     # else:
        #     #     phase_of_right = "swing phase" if (phase_of_right != 'swing phase') else "stance phase"
        
        cv2.putText(img, "phase of right side : " + phase_of_right, (50, 75),
                        cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 2)
        cv2.putText(img, "phase of left side : " + phase_of_left, (50, 100),
                        cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 2)
            
        print("TOTAL CYCLE : ", no_total_cycle)
        print(initial_right_swing_frame)
        print(initial_left_swing_frame)
        # Check Neck, Hip hike(R L legs), Limping(R L feet), Arms (R L), Lead foot (R L)
        print("%.3f "%float(no_neck_frame / no_total_frame), "%.3f "%float(no_rightleg_frame / no_total_frame), "%.3f "%float(no_leftleg_frame / no_total_frame), "%.3f "%float(no_limping_right / no_total_frame), "%.3f "%float(no_limping_left / no_total_frame), "%.3f "%float(no_swing_right / no_total_frame), "%.3f "%float(no_swing_left / no_total_frame), "%.3f"%float(lead_foot_right / no_total_frame), "%.3f"%float(lead_foot_left / no_total_frame))


    cv2.imshow("Extracted Pose", opImg)
    cv2.imshow("Pose Estimation", img)

    # Break the loop if the user presses 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



cap.release()
video_writer.release()
cv2.destroyAllWindows()
