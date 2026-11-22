"""
Task 2: Recognize faces and map each face to a number on the LED matrix.

In the lab tutorial you usually:
- capture / detect a face with the camera module
- identify which enrolled face it is
- show the linked number on the micro:bit LED matrix

This file provides a clear structure you can connect to the tutorial API.
For a PC-side demo without hardware, it uses a simulated detector.
"""

from __future__ import annotations

# Face ID -> LED number
FACE_TO_NUMBER = {
    "face_A": "1",
    "face_B": "2",
    "face_C": "3",
}


def detect_face_id(camera_frame=None) -> str:
    """
    Replace this function body with the face-recognition call from your lab tutorial.

    Example idea:
        result = tutorial_recognize(camera_frame)
        return result.name
    """
    # Demo fallback (simulation): pretend we recognized face_A
    return "face_A"


def map_face_to_led_number(face_id: str) -> str:
    return FACE_TO_NUMBER.get(face_id, "?")


def show_on_microbit(number: str) -> None:
    """
    Send / display the number on micro:bit LED matrix.
    Replace with your tutorial serial/radio/micro:bit display code if needed.
    """
    try:
        from microbit import display  # type: ignore

        display.show(number)
    except Exception:
        # PC demo: print instead of driving hardware
        print("[LED MATRIX]", number)


def main() -> None:
    print("Face recognition demo started...")
    face_id = detect_face_id()
    number = map_face_to_led_number(face_id)
    print(f"Recognized: {face_id} -> number {number}")
    show_on_microbit(number)


if __name__ == "__main__":
    main()
