import os
import cv2
from cvzone.PoseModule import PoseDetector

# Initialize webcam
cap = cv2.VideoCapture(0)
detector = PoseDetector()

# Path to shirt images
shirtFolderPath = r"C:\Users\Lenovo\OneDrive\Documents\shirts"
listShirts = os.listdir(shirtFolderPath)

# Calculate the fixed aspect ratio
fixedRatio = 262 / 190  # widthOfShirt / widthOfPoint11to12
shirtRatioHeightWidth = 581 / 440

# Initialize image number for shirt selection
imageNumber = 0

# Load overlay images and buttons
imgButtonRight = cv2.imread("C:/Users/hanis/Downloads/Resources-1/Resources/button.png", cv2.IMREAD_UNCHANGED)

# Check if imgButtonRight is loaded properly
if imgButtonRight is None:
    print("Error: Failed to load imgButtonRight")
else:
    # Resize the overlay image
    if len(imgButtonRight.shape) > 2 and imgButtonRight.shape[2] == 4:  # Check if the image has an alpha channel
        imgButtonRight = cv2.resize(imgButtonRight, (128, 128), interpolation=cv2.INTER_AREA)[:, :, :3]
    else:
        imgButtonRight = cv2.resize(imgButtonRight, (128, 128), interpolation=cv2.INTER_AREA)

    # Load the mirrored image for the left button
    imgButtonLeft = cv2.flip(imgButtonRight, 1)

    # Initialize counters and speed for button interaction
    counterRight = 0
    counterLeft = 0
    selectionSpeed = 6

while True:
    success, img = cap.read()
    img = detector.findPose(img)
    
    lmList, bboxInfo = detector.findPosition(img, bboxWithHands=False, draw=False)
    if lmList:
        # Calculate necessary parameters for shirt placement
        lm11 = lmList[11][1:3]
        lm12 = lmList[12][1:3]
        imgShirtPath = os.path.join(shirtFolderPath, listShirts[imageNumber])

        # Check if imgShirtPath exists
        if not os.path.exists(imgShirtPath):
            print(f"Error: {imgShirtPath} does not exist")
            continue

        # Load imgShirt
        imgShirt = cv2.imread(imgShirtPath, cv2.IMREAD_UNCHANGED)

        # Check if imgShirt is loaded properly
        if imgShirt is None:
            print(f"Error: Failed to load {imgShirtPath}")
            continue

        # Calculate the width of the shirt based on pose landmarks
        widthOfShirt = int((lm11[0] - lm12[0]) * fixedRatio)

        # Check if widthOfShirt is valid
        if widthOfShirt <= 0:
            print("Error: Invalid widthOfShirt")
            continue

        # Resize imgShirt
        imgShirt = cv2.resize(imgShirt, (widthOfShirt, int(widthOfShirt * shirtRatioHeightWidth)))

        # Calculate offset based on current scale
        currentScale = (lm11[0] - lm12[0]) / 190
        offset = int(44 * currentScale), int(48 * currentScale)

        # Overlay the shirt on the person's body
        try:
            for c in range(3):
                img[lm12[1] - offset[1]:lm12[1] - offset[1] + imgShirt.shape[0], 
                    lm12[0] - offset[0]:lm12[0] - offset[0] + imgShirt.shape[1], c] = \
                    img[lm12[1] - offset[1]:lm12[1] - offset[1] + imgShirt.shape[0], 
                    lm12[0] - offset[0]:lm12[0] - offset[0] + imgShirt.shape[1], c] * \
                    (1 - imgShirt[:, :, 3] / 255.0)
        except:
            pass

        # Overlay interactive buttons for shirt selection
        if imgButtonRight is not None:
            overlay_right_x = img.shape[1] - imgButtonRight.shape[1] - 10
            overlay_left_x = 10

            img[293:293 + imgButtonRight.shape[0], overlay_right_x:overlay_right_x + imgButtonRight.shape[1]] = imgButtonRight
            img[293:293 + imgButtonLeft.shape[0], overlay_left_x:overlay_left_x + imgButtonLeft.shape[1]] = imgButtonLeft

            # Implement button interaction for shirt selection
            if lmList[16][1] < 300:
                counterRight += 1
                cv2.ellipse(img, (139, 360), (66, 66), 0, 0,
                            counterRight * selectionSpeed, (0, 255, 0), 20)
                if counterRight * selectionSpeed > 360:
                    counterRight = 0
                    if imageNumber < len(listShirts) - 1:
                        imageNumber += 1
            elif lmList[15][1] > 900:
                counterLeft += 1
                cv2.ellipse(img, (1138, 360), (66, 66), 0, 0,
                            counterLeft * selectionSpeed, (0, 255, 0), 20)
                if counterLeft * selectionSpeed > 360:
                    counterLeft = 0
                    if imageNumber > 0:
                        imageNumber -= 1
            else:
                counterRight = 0
                counterLeft = 0

    cv2.imshow("Image", img)
    cv2.waitKey(1)