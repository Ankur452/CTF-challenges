import random
import gzip
import bz2
import tarfile
import os
import tempfile
import string

# Function to generate a random string
def generate_random_string(length=64):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

# Function to compress a file using Gzip
def compress_with_gzip(file_name):
    try:
        with open(file_name, 'rb') as f_in:
            with gzip.open(f'{file_name}.gz', 'wb') as f_out:
                f_out.writelines(f_in)
        print(f"File '{file_name}' compressed with Gzip successfully.")
    except Exception as e:
        print(f"Error compressing with Gzip: {str(e)}")

# Function to compress a file using Bzip2
def compress_with_bzip2(file_name):
    try:
        with open(file_name, 'rb') as f_in:
            with bz2.BZ2File(f'{file_name}.bz2', 'wb') as f_out:
                f_out.writelines(f_in)
        print(f"File '{file_name}' compressed with Bzip2 successfully.")
    except Exception as e:
        print(f"Error compressing with Bzip2: {str(e)}")

# Function to compress a file using Tar
def compress_with_tar(file_name):
    try:
        with tarfile.open(f'{file_name}.tar', 'w') as tar:
            tar.add(file_name)
        print(f"File '{file_name}' compressed with Tar successfully.")
    except Exception as e:
        print(f"Error compressing with Tar: {str(e)}")

# Function to strip file extension
def strip_extension(file_name):
    base_name = os.path.splitext(file_name)[0]
    return base_name

# Main function
def main():
    file_name = 'flag.txt'

    # Generate a random string and write it to the flag.txt file
    random_string = generate_random_string()
    with open(file_name, 'w') as flag_file:
        flag_file.write(random_string)

    # Randomly shuffle the compression methods
    compression_methods = [compress_with_gzip, compress_with_bzip2, compress_with_tar]
    random.shuffle(compression_methods)

    # Create a temporary directory for storing intermediate files
    temp_dir = tempfile.mkdtemp()

    # Move the original file to the temporary directory
    os.rename(file_name, os.path.join(temp_dir, file_name))

    for compression_method in compression_methods:
        # Randomly select the number of times to compress (between 1 and 5)
        num_compressions = random.randint(1, 5)

        for _ in range(num_compressions):
            try:
                # Compress the file using the selected method
                compression_method(os.path.join(temp_dir, file_name))
                
            except Exception as e:
                print(f"Error: {str(e)}")

    # Rename the final compressed file to remove the extension
    final_compressed_file = os.path.join(temp_dir, file_name)
    os.rename(final_compressed_file, strip_extension(final_compressed_file))

    # Move the final file back to the original directory
    os.rename(os.path.join(temp_dir, final_compressed_file), final_compressed_file)

    # Remove the temporary directory and its contents
    os.rmdir(temp_dir)

if __name__ == "__main__":
    main()
