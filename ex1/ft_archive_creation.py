#!/usr/bin/env python3
def archive_creation() -> None:
    """Create 'new_discovery.txt' and write predefined entries."""
    file_name = "new_discovery.txt"
    print(f"\nInitializing new storage unit: {file_name}")
    file = open(file_name, "w")
    print("Storage unit created successfully...")
    print("\nInscribing preservation data...")
    entry_data = (
        "[ENTRY 001] New quantum algorithm discovered\n"
        "[ENTRY 002] Efficiency increased by 347%\n"
        "[ENTRY 003] Archived by Data Archivist trainee"
    )
    print(entry_data)
    file.write(entry_data)
    file.close()
    print("\nData inscription complete. Storage unit sealed.")
    print(f"Archive '{file_name}' ready for long-term preservation.")


def main() -> None:
    """Run the archive creation system."""
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
    archive_creation()


if __name__ == "__main__":
    main()
