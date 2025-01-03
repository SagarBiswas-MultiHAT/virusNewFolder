# Virus Folder Creation Script

![virusNewFolder](https://scontent.fdac138-2.fna.fbcdn.net/v/t39.30808-6/471780123_122132262602552158_5933686155363882713_n.jpg?stp=dst-jpg_p526x296_tt6&_nc_cat=103&ccb=1-7&_nc_sid=127cfc&_nc_ohc=iBKZPhz3pEMQ7kNvgEktkq-&_nc_zt=23&_nc_ht=scontent.fdac138-2.fna&_nc_gid=AYmT18M1kisGdB1FStuI4Lz&oh=00_AYA8Aww-e4CAQIB0z4z8LoSTrd_Ge1UuAsJtagAsJgarbw&oe=6778A2E1)

This Python script automates the creation of multiple folders named "Malicious", followed by a number (e.g., Malicious1, Malicious2), until an error occurs. It's useful for testing purposes, but should be used with caution as it continuously creates directories. Additionally, the script provides terminal commands for safely removing the created folders.

## Features

- Automatically creates multiple folders with the name "Malicious" followed by a number.
- Continuously creates folders until an error is encountered.
- Provides commands for safely deleting the created folders.

## Requirements

- Python 3.x

## How to Use

1. Clone or download the script.
2. Run the script in your terminal:
    ```bash
    python3 virusNewFolder.py
    ```
3. The script will begin creating folders named "Malicious1", "Malicious2", etc.

## Deleting Created Folders

If you want to remove the folders created by the script, use the following terminal commands:

### 1. To list and find the created folders:
```bash
ls | grep "Malicious"
```

### 2. To remove the folders individually (if they are empty):
```bash
rm -d Malicious*
```

### 3. To remove all "Malicious" folders (even non-empty ones), use this command:
```bash
sudo find . -maxdepth 1 -name "Malicious*" -exec rm -rf {} +
```

### Explanation:

- `ls | grep "Malicious"`: Lists all folders containing "Malicious" in the current directory.
- `rm -d Malicious*`: Deletes empty folders named "Malicious*".
- `sudo find . -maxdepth 1 -name "Malicious*" -exec rm -rf {} +`: Uses the `find` command to search for and delete all folders starting with "Malicious", even if they are not empty.

## License

This project is licensed under the MIT License. Use responsibly.
