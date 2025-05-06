def main():
    
   

    import zipfile
    import os

    zip_path = "students-performance-in-exams.zip"
    extract_path = "."#set extract_path = ".", it tells the program to extract the contents of the zip file into the current directory

    # Ensure the file exists before attempting extraction
    if os.path.exists(zip_path):
        print(f"Extracting {zip_path}...")
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_path)
        print(f"Extraction complete to {extract_path}")
    else:
        print(f"Error: {zip_path} does not exist.")


if __name__ == "__main__":
    main()