import random
import subprocess

# Function to decompress a file using Gzip
def decompress_with_gzip(file_name):
    try:
        subprocess.run(['gunzip', file_name])
        print(f"File '{file_name}' decompressed with Gzip successfully.")
        return f'{file_name[:-3]}'  # Return the decompressed file name
    except Exception as e:
        print(f"Error decompressing with Gzip: {str(e)}")
        return None

# Function to decompress a file using Bzip2
def decompress_with_bzip2(file_name):
    try:
        subprocess.run(['bunzip2', file_name])
        print(f"File '{file_name}' decompressed with Bzip2 successfully.")
        return f'{file_name[:-4]}'  # Return the decompressed file name
    except Exception as e:
        print(f"Error decompressing with Bzip2: {str(e)}")
        return None

# Function to decompress a file using Tar
def decompress_with_tar(file_name):
    try:
        subprocess.run(['tar', '-xf', file_name])
        print(f"File '{file_name}' decompressed with Tar successfully.")
        return 'flag.txt'  # Assuming the original file name is 'flag.txt'
    except Exception as e:
        print(f"Error decompressing with Tar: {str(e)}")
        return None

# Main function
def main():
    compressed_file = 'flag'  # Replace with the actual compressed file name
    decompression_methods = [decompress_with_tar, decompress_with_bzip2, decompress_with_gzip]

    # Reverse the order of decompression methods
    decompression_methods.reverse()

    # Randomly select the number of times to decompress (between 1 and 5)
    num_decompressions = random.randint(1, 5)

    for _ in range(num_decompressions):
        # Determine the compression type using the 'file' command
        try:
            compression_type = subprocess.check_output(['file', compressed_file]).decode()
            if 'gzip' in compression_type:
                decompression_method = decompress_with_gzip
            elif 'bzip2' in compression_type:
                decompression_method = decompress_with_bzip2
            elif 'tar' in compression_type:
                decompression_method = decompress_with_tar
            else:
                print(f"Error: Unsupported compression format in '{compressed_file}'")
                break

            # Attempt to decompress the file using the selected method
            decompressed_file = decompression_method(compressed_file)

            if decompressed_file:
                # Update the compressed_file to the decompressed file for the next iteration
                compressed_file = decompressed_file
        except Exception as e:
            print(f"Error determining compression type: {str(e)}")
            break

    # Rename the final decompressed file to 'result.txt'
    final_result_file = 'result.txt'
    try:
        import os
        os.rename(compressed_file, final_result_file)
        print(f"Final result saved as '{final_result_file}'.")
    except Exception as e:
        print(f"Error renaming the final result file: {str(e)}")

if __name__ == "__main__":
    main()
