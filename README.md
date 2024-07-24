# Fun-and-Utility-Hub

Overview
This project is a comprehensive suite featuring a collection of classic games and essential utilities. It combines entertainment with productivity tools, offering a versatile experience for users. The suite includes:

BlackJack Game
PingPong Game
Turtle Crossing Game
HungrySnake Game
Hangman Game
Quizzler Quest
FluentFlock (Language Learning Game)
Focus Hours (Productivity Timer)
PassWordManager (Password Management Tool)
DocuMaster (Document Management Utility)
DocuMaster (Document Management Utility)
DocuMaster is a powerful tool within this suite designed to handle various document-related tasks with ease. It supports command-line and interactive modes, providing functionalities such as:

Document Creation: Create and save documents in .docx format with customized headings and content.
Text Manipulation:
Search and Replace: Modify specific words or phrases in the document.
Text Extraction: Extract information or count occurrences of a word.
Text Sorting: Sort lines or words alphabetically.
Remove Duplicates: Eliminate duplicate lines.
File Compression: Compress document content into a .gz file.
File Decompression: Decompress .gz files back to their original format.
PDF Creation: Convert .docx documents to PDF format.
Command-Line Usage
To run various document management commands, use the following options:

Count words: -w
Count characters: -c
Count lines: -l
Sort lines alphabetically: -s
Remove duplicate lines: -d
Replace words: -r <target> <replacement>
Compress file: -z
Decompress file: -x
Create PDF from Word: -p

Copy code
python docu_master.py <file_path> -<command>

Interactive Mode
You can also run the utility in an interactive mode directly in the terminal, allowing for visual and guided command execution:


Copy code
python docu_master.py

In this mode, you will be prompted to:

Create a new file or upload an existing one.
Choose from text manipulation, file compression, or PDF creation tasks.
Perform the desired operations with visual feedback and guidance.
