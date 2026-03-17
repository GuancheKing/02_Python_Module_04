def vault_security() -> None:
    """Perform secure file reading and writing with context managers."""
    try:
        print("\nInitiating secure vault access...")
        print("Vault connection established with failsafe protocols")

        print("\nSECURE EXTRACTION:")
        with open("classified_data.txt", "r") as extraction:
            content = extraction.read()
            print(content)

        print("\nSECURE PRESERVATION:")
        with open("security_protocols.txt", "w") as preservation:
            entry_data = "[CLASSIFIED] New security protocols archived"
            preservation.write(entry_data)
            print(entry_data)

        print("Vault automatically sealed upon completion")
        print("\nAll vault operations completed with maximum security.")

    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")


def main() -> None:
    """Run the vault security system."""
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
    vault_security()


if __name__ == "__main__":
    main()
