# Work in Progress: Yolov8 UAV Object Identifier and Tracker

> A computer vision system for real-time detection and tracking of moving targets, stress-tested against degraded sensor conditions relevant to defence and autonomous systems applications (jamming, atmospheric distortion, thermal/FLIR simulation).

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C.svg?logo=pytorch&logoColor=white)](https://pytorch.org/)
[![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-purple.svg)](https://github.com/ultralytics/ultralytics)
[![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8.svg?logo=opencv&logoColor=white)](https://opencv.org/)
---

## Overview

This project implements an end-to-end target detection and tracking pipeline, built to explore the core computer vision and estimation techniques underpinning modern **Guidance, Navigation, and Control (GNC)** and autonomous tracking systems. It combines a YOLOv8-based detector with a hand-rolled Kalman filter for track continuity, and is explicitly stress-tested against realistic sensor degradation scenarios (electronic warfare-style jamming, atmospheric distortion, low-contrast/thermal imaging).

The project is structured to reflect problems relevant to current UK defence investment priorities — particularly counter-UAS detection, sensor resilience under jamming, and GPS/sensor-denied tracking robustness.

**Why this project:** I wanted to apply the machine learning principles I've learnt to a problem with real defence relevance. Instead of only asking whether the model works on clean data, I ask: what happens when that data is degraded, spoofed, or intermittently blacked out? This mirrors real-world operating conditions far more closely, and opens up genuine investigation into problems facing current tracking systems.

---

## Key Features

- **Object detection** — YOLOv8 (PyTorch) fine tuned via transfer learning for target classes relevant to aerial/UAV surveillance scenarios
- **Multi-object tracking** — persistent track IDs across frames, with a custom constant velocity Kalman filter (implemented from first principles, not a library wrapper)
- **Sensor dropout / jamming simulation** — burst pattern dropout modelled on realistic electronic warfare (EW) blackout behaviour, used to evaluate track continuity, position error during coast, and recovery time
- **Environmental stress testing** — atmospheric distortion (fog/smoke), Gaussian/sensor noise, and thermal (FLIR-style) imaging simulation, with benchmarked mAP degradation and mitigation filters
- **Performance profiling** — frame rate (FPS) and latency benchmarking with an eye toward embedded/real time deployment constraints

---

## Project Structure

```
.
├── data/                   # Dataset download/prep scripts (VisDrone / DOTA)
├── src/
│   ├── detection/          # YOLOv8 training, inference
│   ├── tracking/           # Kalman filter, track management, ID association
│   ├── degradation/        # Jamming, noise, atmospheric, thermal simulation
│   └── evaluation/         # mAP, track continuity, position error, recovery time
├── notebooks/              # Exploratory analysis and result visualisation
├── results/                # Benchmark outputs, plots, demo video(s)
├── DEVLOG.md               # Weekly development log
├── requirements.txt
└── README.md
```

---

## Roadmap

- **Phase 0 — ML Foundations:** PyTorch fundamentals through Datacamp tutorial, OpenCV basics through image classification practise, and working YOLOv8 inference demo
- **Phase 1 — Data & Baseline:** Acquire and prepare dataset (VisDrone / DOTA); establish baseline detection pipeline
- **Phase 2 — Training:** Transfer learning on YOLOv8 for target detection; baseline mAP established
- **Phase 3 — Stress Testing:** Degraded-condition evaluation
  - Atmospheric distortion (fog/smoke)
  - Sensor/Gaussian noise
  - Thermal/FLIR simulation
  - Sensor dropout under jamming (custom Kalman filter, burst-pattern blackout, track continuity/coast error/recovery time metrics)
  - Multi-object tracking with persistent IDs
  - Small-object / counter-UAS evaluation
  - Cross-domain evaluation (DOTA)
  - Lightweight/quantized model variant
- **Phase 4 — Production:** Code cleanup, FPS/latency profiling, live demo, final documentation

See [`DEVLOG.md`](DEVLOG.md) for detailed weekly progress notes.

---

## Datasets

- **[VisDrone](http://aiskyeye.com/)** — aerial drone imagery, ITAR-compliant, used for primary training/evaluation
- **[DOTA](https://captain-whu.github.io/DOTA/)** — aerial imagery with oriented bounding boxes, used for cross-domain generalisation testing

---

## Results

*(To be populated as Phase 2–3 complete.)*

| Metric | Baseline | Under Jamming/Dropout | Under Atmospheric Distortion |
|---|---|---|---|
| mAP@0.5 | — | — | — |
| Track continuity | — | — | — |
| Position error (coast) | — | — | — |
| Recovery time | — | — | — |

---

## Installation

```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

## Usage

```bash
# Run detection + tracking on a video file
python src/main.py --source path/to/video.mp4

# Run with a specific degradation profile
python src/main.py --source path/to/video.mp4 --degrade jamming
```

*(Update with actual CLI once implemented.)*

---

## Technical Notes

- **Kalman filter:** implemented from scratch (constant-velocity model) rather than using a library abstraction, to demonstrate understanding of the underlying estimation theory rather than just API usage.
- **Jamming simulation:** models burst-pattern sensor dropout rather than simple frame-drop, intended to reflect plausible EW blackout behaviour rather than an idealised worst case.

---

## Relevance to Defence & GNC Applications

This project was deliberately shaped around problems referenced in the June 2026 UK Defence Investment Plan — particularly sensor resilience under electronic attack, counter-UAS detection, and GPS/sensor-denied tracking. The stress-testing phase (Phase 3) is intended as the primary differentiator versus a standard object-detection portfolio project.

---

## Author

**[Aaron Liddell]** — Final-year Physics student at the University of Edinburgh.

 [LinkedIn](https://www.linkedin.com/in/aaron-liddell-4ba8a21ba) ·  aaronliddell05@gmail.com
