import os
import shutil
import logging

# Configure logging
logging.basicConfig(
    filename='file_operations.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Function to rename files
def rename_files(folder_path):
    try:
        files = os.listdir(folder_path)
        count = 1

        for file in files:
            old_path = os.path.join(folder_path, file)

            if os.path.isfile(old_path):
                file_ext = os.path.splitext(file)[1]
                new_name = f"file_{count}{file_ext}"
                new_path = os.path.join(folder_path, new_name)

                os.rename(old_path, new_path)
                print(f"Renamed: {file} → {new_name}")
                logging.info(f"Renamed: {file} → {new_name}")
                count += 1

    except Exception as e:
        print("Error while renaming files:", e)
        logging.error(f"Rename Error: {e}")


# Function to sort files by extension
def sort_files(folder_path):
    try:
        files = os.listdir(folder_path)

        for file in files:
            file_path = os.path.join(folder_path, file)

            if os.path.isfile(file_path):
                extension = os.path.splitext(file)[1][1:]

                if extension == "":
                    extension = "others"

                target_folder = os.path.join(folder_path, extension)

                if not os.path.exists(target_folder):
                    os.makedirs(target_folder)

                shutil.move(file_path, os.path.join(target_folder, file))
                print(f"Moved: {file} → {extension}/")
                logging.info(f"Moved: {file} → {extension}/")

    except Exception as e:
        print("Error while sorting files:", e)
        logging.error(f"Sorting Error: {e}")


# Function to delete empty files
def delete_empty_files(folder_path):
    try:
        files = os.listdir(folder_path)

        for file in files:
            file_path = os.path.join(folder_path, file)

            if os.path.isfile(file_path) and os.path.getsize(file_path) == 0:
                os.remove(file_path)
                print(f"Deleted empty file: {file}")
                logging.info(f"Deleted empty file: {file}")

    except Exception as e:
        print("Error while deleting files:", e)
        logging.error(f"Delete Error: {e}")


# Main Program
print("===== File Automation Script =====")
folder = input("Enter folder path: ")

print("\nChoose an operation:")
print("1. Rename Files")
print("2. Sort Files")
print("3. Delete Empty Files")

choice = input("Enter your choice (1/2/3): ")

if choice == '1':
    rename_files(folder)
elif choice == '2':
    sort_files(folder)
elif choice == '3':
    delete_empty_files(folder)
else:
    print("Invalid choice. Please select 1, 2, or 3.")