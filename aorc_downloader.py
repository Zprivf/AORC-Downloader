##############################
# Python code to mdownload AORC 4km Data. 
# Fitsume Wolkeba
# fwolkeba@crimson.ua.edu
# Last edited: 3/26/2024
#############################
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
def netcdf_merger(path_to_netcdf_files, output_folder_path_and_name_of_merged_file):
    # List all NetCDF files in the folder
    file_paths = glob.glob(path_to_netcdf_files)

    # Open all files and merge along the time dimension
    ds_merged = xr.open_mfdataset(file_paths, combine='by_coords')

    # Optionally, save the merged dataset to a new NetCDF file
    ds_merged.to_netcdf(output_folder_path_and_name_of_merged_file)
    
def sum_to_daily(hourly_netcdf_file,vaiable_name,output_folder_path_and_name_of_daily_file):

    data=xr.open_dataset(hourly_netcdf_file)
    daily_dataset = data[vaiable_name].resample(time='D').sum()
    daily_dataset = data[vaiable_name].resample(time='D', skipna=False).sum()
    daily_dataset.to_netcdf(output_folder_path_and_name_of_daily_file)
    
def avg_to_daily(hourly_netcdf_file,vaiable_name,output_folder_path_and_name_of_daily_file):

    data=xr.open_dataset(hourly_netcdf_file)
    daily_dataset = data[vaiable_name].resample(time='D').mean()
    daily_dataset = data[vaiable_name].resample(time='D', skipna=False).sum()
    daily_dataset.to_netcdf(output_folder_path_and_name_of_daily_file)
        

        
