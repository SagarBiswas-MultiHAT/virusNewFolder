import os
folderName = "Malicious"
count = 0
# print("Script Name: ", mainFileName) # Script Name:  /home/sagar-biswas/MEDIA/Programming --Learning/NEW_PY/CyberSecurity/Public/virusNewForder.py

# while count < 10:
while True:
    count += 1
    try:
        temp = folderName + str(count) # + means write or append? Amswer: append
        os.mkdir(temp)
        # print("Folder Created: ", temp)
    except Exception as Error:
        print("Error: ", Error)
        break


# To remove the created folders type on terminal: 

        # 1st command:  ls | grep "Malicious"
        # 2nd command:  rm -d Malicious*
# 
'''
Explanation:

The command ls | grep "Malicious" searches for and displays only the entries from the ls output that contain the word "Malicious".

The -d option in the rm command stands for "directory". When used, it allows you to remove empty directories specifically.

    -- The -d option tells rm to remove the specified directory only if it is empty.
'''


# To remove the created 1 to ... folders type on terminal:

    # sudo find . -maxdepth 1 -name "Malicious*" -exec rm -rf {} +

'''
Explanation:

 1. sudo

    - Purpose: Runs the command with superuser privileges.

    - Why: Required if the files or directories are owned by another user or are protected against modification or deletion.

---

 2. find

    - Purpose: A utility to search for files and directories in a directory hierarchy.

---

 3. .

    - Purpose: Specifies the current directory as the starting point for the search.

    - Why: Limits the search to the current location instead of the whole filesystem.

---

 4. -maxdepth 1

    - Purpose: Limits the search depth to the current directory.

    - Why: Ensures that only files and directories in the current directory are matched (ignores subdirectories).

---

 5. -name "Malicious*"

    - Purpose: Matches files and directories whose names start with `Malicious`.

    - Why: Ensures the command only targets files or directories matching this pattern.

---

 6. -exec

    - Purpose: Allows you to execute a specified command (`rm -rf` in this case) on each file or directory found by `find`.

---

 7. rm -rf

    - Purpose:
        -r: Recursively deletes directories and their contents.
        -f: Forces deletion, suppressing confirmation prompts (even for write-protected files).

    - Why: Ensures that all matching directories and files, even those write-protected, are deleted.

---

8. {}

    - Purpose: A placeholder for each file or directory found by `find`.

    - Why: Each matched item is substituted into `{}` before executing the `rm` command.

---

9. +

    - Purpose: Optimizes execution by passing multiple matched items to `rm` in batches instead of running `rm` for each file or directory individually.
    
    - Why: Increases efficiency, especially when dealing with a large number of matches.

---

How It Works:

1. The `find` command searches the current directory (`.`) for items matching the name pattern `Malicious*`, restricting the search to the current directory (`-maxdepth 1`).
2. For each match, it substitutes the file or directory name into `{}` and passes them in batches to the `rm -rf` command.
3. `sudo` ensures the command runs with the required privileges to delete protected or owned files.
4. The `rm -rf` command forcibly and recursively deletes the matched files or directories.

---

This command is powerful and should be used cautiously as it permanently deletes files and directories without confirmation.

'''