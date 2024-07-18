# Simple-Password-Cracker

## Overview
This scrip demonstrates how to hash a password and compare it with hashed entires in a password file. It uses the MD5 hashing algorithm to ensure the password is not stored in plain text.

## Files
- 'Ashley-Madison.txt': A text file containing a list of the passwords found by the Ashley Madison hack.

## Dependencies
- 'hashlib': A Python module used for hashing

## How It Works
1. **Import the 'hashlib module'**: This module provides hashing functions such as MD5, SHA-1, etc.

2. **Define the password and the filename**

3. **Encode the password**: The password is converted into bytes using UTF-8 encoding.

4. **Hash the password**: The encoded password is hashed using the MD5 algorithm. The strip() method removes any leading or trailing whitespace.

5. **Print the hashed password**: This prints the MD5 hash of the password

6. **OPen the password file**: The file is opened in read mode

7. **Compare each word in the file**: Each word (potential password) in the file is encoded and hashed, then compared to the hashed password.

## Summary
This script reads a password from a file, hashes it using MD5, and compares it to a pre-defined hashed password. If a match is found, it prints a message indicating a security breach; otherwise, it confirms the password is strong. This demonstrates a basic approach to password hashing and checking, highlighting the importance of not storing plain text passwords.

## Credits
- **YoutTube Link**: https://www.youtube.com/watch?v=G1FgPh9D0jU&ab_channel=BrandonJacobson