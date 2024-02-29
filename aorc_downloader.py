import os
def AORC_downloader (url,output_directory):
# Create the output directory if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    try:
        os.system(f"wget -c --mirror --no-parent --no-check-certificate  {url} -P {output_directory}")  
        print(f"Contents of folder {url} downloaded and saved in {output_directory}")
    except:    
        print(" Web folder not working, check and run again")
        try:
            os.system(f"wget -c --no-check-certificate  {url} -P {output_directory}")
            print(f"Contents of file {url} downloaded and saved in {output_directory}")
        except:
            print(" file not availible, check file and run again")
            try:
                os.system(f"wget -ci --no-check-certificate  {url} -P {output_directory}")
                print(f"Contents of text {url} downloaded and saved in {output_directory}")
            except Exception as e:
                print("text file failed, check file and run again:", e)
            else:
                print("Something failed please recheck url and downloadfolder again:")

        

        
