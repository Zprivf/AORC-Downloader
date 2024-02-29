import os
def AORC_downloader (url,output_directory):
# Create the output directory if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    try:
        os.system(f"wget -c --mirror --no-parent --no-check-certificate  {url} -P {output_directory}")
        print(f"Contents of {url} folder downloaded and saved in {output_directory}")
    except Exception as e:
        print("url failed:", e)
    else:
        exit() 
    try:
        os.system(f"wget -c --no-check-certificate  {url} -P {output_directory}")
        print(f"File {url} downloaded and saved in {output_directory}")
    except Exception as e:
        print("url failed:", e)
    else:
        print("url succeeded")
        exit()  

    os.system(f"wget -ci --no-check-certificate  {url} -P {output_directory}")
    print(f"Contents of list {url} downloaded and saved in {output_directory}")