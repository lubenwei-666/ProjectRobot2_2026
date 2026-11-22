"""
Task 3: Protect stored face data by hashing.

Instead of keeping raw face images in plain form, store a hash digest.
SHA-256 is used as a simple, standard one-way protection method for this coursework.
"""

from __future__ import annotations

import hashlib
from typing import Dict


def hash_face_data(face_bytes: bytes) -> str:
    """Return SHA-256 hex digest of face bytes."""
    return hashlib.sha256(face_bytes).hexdigest()


def enroll_face(store: Dict[str, str], person_name: str, face_bytes: bytes) -> str:
    """
    Enroll a face: store only the hash, not the raw image bytes.
    Returns the hash string.
    """
    digest = hash_face_data(face_bytes)
    store[person_name] = digest
    return digest


def verify_face(store: Dict[str, str], person_name: str, face_bytes: bytes) -> bool:
    """Check whether the given face matches the stored hash for person_name."""
    if person_name not in store:
        return False
    return store[person_name] == hash_face_data(face_bytes)


def main() -> None:
    # Simulated face image bytes (in a real system these come from the camera)
    face_a = b"raw_face_image_bytes_of_person_A"
    face_b = b"raw_face_image_bytes_of_person_B"

    protected_store: Dict[str, str] = {}

    hash_a = enroll_face(protected_store, "PersonA", face_a)
    hash_b = enroll_face(protected_store, "PersonB", face_b)

    print("Stored protected face records (hashes only):")
    for name, digest in protected_store.items():
        print(f"  {name}: {digest}")

    print("Verify PersonA with correct data:", verify_face(protected_store, "PersonA", face_a))
    print("Verify PersonA with wrong data:", verify_face(protected_store, "PersonA", face_b))
    print("Example hash for PersonA:", hash_a)
    print("Example hash for PersonB:", hash_b)


if __name__ == "__main__":
    main()
