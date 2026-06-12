# 🖼️ Image Stitching & Panorama Creation

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python" />
  <img src="https://img.shields.io/badge/OpenCV-Computer%20Vision-green?logo=opencv" />
  <img src="https://img.shields.io/badge/NumPy-Scientific%20Computing-orange?logo=numpy" />
  <img src="https://img.shields.io/badge/Status-Completed-success" />
</p>

## 🌟 Overview

A Computer Vision project that automatically combines multiple overlapping images into a single seamless panoramic image using **ORB feature detection**, **Brute Force matching**, **RANSAC-based homography estimation**, and **perspective warping**.

This project demonstrates key concepts in image processing, feature extraction, geometric transformations, and panorama generation.

---

## 🚀 Key Features

✅ ORB (Oriented FAST and Rotated BRIEF) Feature Detection

✅ Brute Force Feature Matching

✅ RANSAC Outlier Removal

✅ Homography Matrix Estimation

✅ Perspective Transformation

✅ Automatic Panorama Generation

✅ Visualization of Feature Correspondences

---

## 🛠️ Tech Stack

* 🐍 Python
* 👁️ OpenCV
* 🔢 NumPy
* 📊 Matplotlib

---

## 🔄 Pipeline Workflow

```text
Input Images
      │
      ▼
Feature Detection (ORB)
      │
      ▼
Feature Matching (BFMatcher)
      │
      ▼
Outlier Rejection (RANSAC)
      │
      ▼
Homography Estimation
      │
      ▼
Perspective Warping
      │
      ▼
Panorama Generation
```

---

## 📈 Performance

| Metric                  | Value      |
| ----------------------- | ---------- |
| ORB Keypoints (Image 1) | ~3000      |
| ORB Keypoints (Image 2) | ~3000      |
| Good Matches            | ~825       |
| Homography Estimation   | Successful |
| Panorama Generation     | Successful |

---

## 📂 Project Structure

```text
Image-Stitching-Panorama/
│
├── images/
│   ├── img1.jpg
│   └── img2.jpg
│
├── outputs/
│   ├── feature_matches.jpg
│   └── final_panorama.jpg
│
├── image_stitching.py
├── requirements.txt
├── README.md
└── Project_Report.pdf
```

---

## ⚡ Installation

```bash
git clone https://github.com/yourusername/Image-Stitching-Panorama.git

cd Image-Stitching-Panorama

pip install -r requirements.txt
```

---

## ▶️ Run the Project

```bash
python image_stitching.py
```

---

## 🖼️ Results

### Input Images

| Image 1        | Image 2        |
| -------------- | -------------- |
| Add Screenshot | Add Screenshot |

### Feature Matching

Add `feature_matches.jpg`

### Final Panorama

Add `final_panorama.jpg`

---

## 🎯 Concepts Demonstrated

* Feature Detection & Description
* Feature Matching
* Geometric Image Transformation
* Homography Estimation
* RANSAC Algorithm
* Perspective Warping
* Panorama Stitching

---

## 🌍 Applications

* Virtual Tours
* Panoramic Photography
* Satellite Image Mosaicing
* Drone Mapping
* Robotics & Computer Vision

---

## 👨‍💻 Author

### Sachin Tomar

🎓 B.Tech – Mathematics & Computing
🏫 National Institute of Technology Kurukshetra

---

⭐ If you found this project interesting, consider giving it a star!
