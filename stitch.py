import cv2
import numpy as np
import matplotlib.pyplot as plt

# =====================================================
# LOAD IMAGES
# =====================================================

img1 = cv2.imread('images/img1.jpg')
img2 = cv2.imread('images/img2.jpg')

# =====================================================
# CHECK IMAGES
# =====================================================

if img1 is None or img2 is None:
    print("Error loading images!")
    print("Check image path and filenames.")
    exit()

# =====================================================
# RESIZE IMAGES
# =====================================================

img1 = cv2.resize(img1, (800, 600))
img2 = cv2.resize(img2, (800, 600))

# =====================================================
# CONVERT TO GRAYSCALE
# =====================================================

gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# =====================================================
# ORB FEATURE DETECTOR
# =====================================================

orb = cv2.ORB_create(3000)

kp1, des1 = orb.detectAndCompute(gray1, None)
kp2, des2 = orb.detectAndCompute(gray2, None)

print("Keypoints in Image 1:", len(kp1))
print("Keypoints in Image 2:", len(kp2))

# =====================================================
# BF MATCHER
# =====================================================

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

matches = bf.match(des1, des2)

# Sort matches based on distance
matches = sorted(matches, key=lambda x: x.distance)

# =====================================================
# FILTER GOOD MATCHES
# =====================================================

good_matches = []

for m in matches:
    if m.distance < 40:
        good_matches.append(m)

print("Good Matches Found:", len(good_matches))

# =====================================================
# CHECK SUFFICIENT MATCHES
# =====================================================

if len(good_matches) < 10:
    print("Not enough matches found!")
    exit()

# =====================================================
# DRAW MATCHES
# =====================================================

matched_image = cv2.drawMatches(
    img1, kp1,
    img2, kp2,
    good_matches[:50],
    None,
    flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS
)

plt.figure(figsize=(18,8))
plt.imshow(cv2.cvtColor(matched_image, cv2.COLOR_BGR2RGB))
plt.title("Feature Matching")
plt.axis('off')
plt.show()

# =====================================================
# EXTRACT MATCHED POINTS
# =====================================================

src_pts = np.float32(
    [kp1[m.queryIdx].pt for m in good_matches]
).reshape(-1,1,2)

dst_pts = np.float32(
    [kp2[m.trainIdx].pt for m in good_matches]
).reshape(-1,1,2)

# =====================================================
# FIND HOMOGRAPHY MATRIX
# =====================================================

H, mask = cv2.findHomography(
    dst_pts,
    src_pts,
    cv2.RANSAC,
    5.0
)

print("\nHomography Matrix:\n")
print(H)

# =====================================================
# WARP PERSPECTIVE
# =====================================================

width = img1.shape[1] + img2.shape[1]
height = max(img1.shape[0], img2.shape[0])

result = cv2.warpPerspective(img2, H, (width, height))

# Place first image
result[0:img1.shape[0], 0:img1.shape[1]] = img1

# =====================================================
# REMOVE BLACK AREA
# =====================================================

gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)

_, thresh = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY)

contours, _ = cv2.findContours(
    thresh,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

x, y, w, h = cv2.boundingRect(contours[0])

result = result[y:y+h, x:x+w]

# =====================================================
# SAVE OUTPUT
# =====================================================

cv2.imwrite("final_panorama.jpg", result)

print("\nPanorama Saved Successfully!")

# =====================================================
# DISPLAY FINAL PANORAMA
# =====================================================

plt.figure(figsize=(20,10))
plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
plt.title("Final Panorama")
plt.axis('off')
plt.show()