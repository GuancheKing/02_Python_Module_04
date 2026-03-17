def ancient_txt_recovery() -> None:
    try:
        print("\nAccessing Storage Vault: ancient_fragment.txt")
        file = open("ancient_fragment.txt", "r")
        print("Connection established...")
        content = file.read()

        print("\nRECOVERED DATA:")
        print(content)

        file.close()
        print("\nData recovery complete. Storage unit disconnected.")
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first")


def main() -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    ancient_txt_recovery()


if __name__ == "__main__":
    main()
