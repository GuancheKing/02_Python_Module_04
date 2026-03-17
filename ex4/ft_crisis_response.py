#!/usr/bin/env python3
def crisis_response() -> None:
    """Handle archive access failures and recovery scenarios."""
    print("\nCRISIS ALERT: Attempting access to 'lost_archive.txt'...")
    try:
        with open("lost_archive.txt", "r") as lost_file:
            content = lost_file.read()
            print(content)
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")

    print("\nCRISIS ALERT: Attempting access to 'classified_data.txt'...")
    try:
        with open("classified_data.txt", "r") as deny_file:
            content = deny_file.read()
            print(content)
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")

    print("\nROUTINE ACCESS: Attempting access to 'standard_archive.txt'...")
    try:
        with open("standard_archive.txt", "r") as file:
            content = file.read()
            print(f"SUCCESS: Archive recovered - ``{content}''")
            print("STATUS: Normal operations resumed")
    except Exception:
        print("ERROR: Unexpected error")


def main() -> None:
    """Run the crisis response system."""
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")
    crisis_response()


if __name__ == "__main__":
    main()
