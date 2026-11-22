# Agile User Stories and Sprints

## Epic

Build a micro:bit robot that can display numbers, recognize faces, and protect face data.

## Sprint 1 (2 Days) – Robot setup and LED numbers

### User Stories
- As a developer, I want to assemble the micro:bit robot so that hardware is ready for demos.
- As a developer, I want to show numbers on the micro:bit LED matrix so that recognition results can be visualized.

### Tasks
- [x] Set up project structure and GitHub repository
- [x] Prepare micro:bit robot hardware
- [x] Implement LED number display program (`task1_led_numbers.py`)

## Sprint 2 (3 Days) – Face recognition and mapping

### User Stories
- As a developer, I want to recognize different faces using the micro:bit robot camera workflow.
- As a developer, I want to link each face to a different number image on the LED matrix.

### Tasks
- [x] Implement face recognition flow (`task2_face_recognition.py`)
- [x] Bind face IDs to LED numbers 1/2/3
- [x] Test mapping with sample faces / demo mode

## Sprint 3 (2 Days) – Protect face data and finalize

### User Stories
- As a developer, I want to protect stored face images using hashing so that raw biometric data is not stored in plain form.

### Tasks
- [x] Implement hashing protection (`task3_face_hash.py`)
- [x] Merge feature branches into `main`
- [x] Prepare demo video and reports
