import os
import csv
import shutil

def task_1_demo():
    """
    Demonstrates file handling, automation, and exception handling for Python Task 1.
    """
    # Define a base directory to keep our demo files organized
    base_dir = './task1_demo_output'
    
    # --- 1. Setup: Create Directory and Sample Files ---
    try:
        # Create the directory if it doesn't exist
        if not os.path.exists(base_dir):
            os.makedirs(base_dir)
            print(f"Created directory: {base_dir}")
        else:
            print(f"Directory already exists: {base_dir}")
    except OSError as e:
        print(f"Error creating directory: {e}")
        return # Exit if we can't create the directory

    # Define file paths
    txt_file_path = os.path.join(base_dir, 'sample.txt')
    csv_file_path = os.path.join(base_dir, 'data.csv')
    
    # --- 2. File Writing: TXT and CSV ---
    try:
        # Write to a TXT file
        with open(txt_file_path, 'w') as f:
            f.write("Hello, this is a sample text file for automation demo.\n")
            f.write("This line is written using Python.\n")
        print(f"Successfully wrote to {txt_file_path}")
        
        # Write to a CSV file
        with open(csv_file_path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Task', 'Status'])
            writer.writerow(['Task_A', 'Completed'])
            writer.writerow(['Task_B', 'Pending'])
            writer.writerow(['Task_C', 'In Progress'])
        print(f"Successfully wrote to {csv_file_path}")
        
    except IOError as e:
        print(f"Error writing files: {e}")

    # --- 3. File Reading: TXT and CSV ---
    print("\n--- Reading File ---")
    try:
        with open(txt_file_path, 'r') as f:
            content = f.read()
            print(f"Content read from TXT: {content.strip()}")
    except FileNotFoundError:
        print(f"Error: The file {txt_file_path} was not found.")
    except Exception as e:
        print(f"An unexpected error occurred while reading TXT: {e}")

    print("\n--- Reading CSV Data ---")
    try:
        with open(csv_file_path, 'r') as f:
            reader = csv.reader(f)
            header = next(reader) # Skip header
            for row in reader:
                print(f"Processing: {row[0]} - {row[1]}")
    except FileNotFoundError:
        print(f"Error: The file {csv_file_path} was not found.")
    except Exception as e:
        print(f"An unexpected error occurred while reading CSV: {e}")

    # --- 4. Automation: Rename, Move, and Delete ---
    print("\n--- Automating File Operations ---")
    
    # Define new paths for automation
    renamed_txt_path = os.path.join(base_dir, 'archived_sample.txt')
    moved_csv_path = os.path.join(base_dir, 'moved_data.csv')
    
    try:
        # Rename a file
        os.rename(txt_file_path, renamed_txt_path)
        print(f"Renamed '{txt_file_path}' to '{renamed_txt_path}'")
        
        # Move a file (shutil.move can also rename)
        # Here we move the CSV to a new location within the same directory
        # For a true move, you would specify a different directory.
        shutil.move(csv_file_path, moved_csv_path)
        print(f"Moved '{csv_file_path}' to '{moved_csv_path}'")

        # Demonstrate deletion
        # Let's create a temporary file to delete
        temp_file_path = os.path.join(base_dir, 'temp_to_delete.txt')
        with open(temp_file_path, 'w') as f:
            f.write("This file will be deleted.")
        
        os.remove(temp_file_path)
        print(f"Successfully deleted '{temp_file_path}'")
        
    except FileNotFoundError as e:
        print(f"Error during automation: A file was not found. {e}")
    except OSError as e:
        print(f"Error during automation: {e}")

    # --- 5. Verification ---
    print("\n--- Verification: Listing files in the demo directory ---")
    if os.path.exists(base_dir):
        print(f"Current files in {base_dir}:")
        print(os.listdir(base_dir))
    else:
        print(f"Directory {base_dir} does not exist.")

# Run the demo
if __name__ == "__main__":
    task_1_demo()
    print("\nFile operation sequence completed.")