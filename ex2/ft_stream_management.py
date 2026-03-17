#!/usr/bin/env python3
import sys


def stream_manager() -> None:
    """Handle user input and route messages through system streams."""
    input_id = input("Input Stream active. Enter archivist ID: ")
    input_status = input("Input Stream active. Enter status report: ")

    print(f"\n[STANDARD] Archive status from {input_id}: {input_status}",
          file=sys.stdout)
    print("[ALERT] System diagnostic: Communication channels verified",
          file=sys.stderr)
    print("[STANDARD] Data transmission complete")
    print("\nThree-channel communication test successful.", file=sys.stdout)


def main() -> None:
    """Run the archive communication system."""
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")
    stream_manager()


if __name__ == "__main__":
    main()
