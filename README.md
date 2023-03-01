# parallel_downloads_selenium
This is a README file that explains how to use the provided scripts to calculate the mean light intensity per country using the tiff files downloaded from this [link](https://eogdata.mines.edu/nighttime_light/nightly/rade9d/?C=N;O=D).
With this written documentation, you will learn how to:
- **Install Python**
- **Create a virtual environment**
- **Install the Python dependencies/libraries**
- **Download the code from GitHub**
- **Call the Python script from R**
- **Solve the cropping problem**

# Files in the Project Tree
You have **six files** in this repo.
- `download_images.py` --> The Python script that **downloads images in parallel**
- `cropping_function_demo.R` --> The R file that contains the code to calculate the **mean light intensity per country**
- `python_bat.bat` --> The batch file that will be used to **call the Python file from R**
- `.gitignore` --> The file that contains the **directories** and **files** to be ignored **before publishing to GitHub**
- `.RData` --> The file that contains the **history of the R file** from the last time I ran it so you can see **how the final dataset looks like**
- `requirements.txt` --> The **requirements file** that contains all the **Python dependencies** you need to install **after creating the virtual environment**

In addition to these files, which you can download from GitHub directly, you will need to create a new file called `.env`. This file will contain the following global input variables
```python
url="https://eogdata.mines.edu/nighttime_light/nightly/rade9d/?C=N;O=D" # Set the URL to download the tiff files from
start_date="2018-01-01" # Set the start date of the tiff files
end_date="2018-12-31" # Set the end date of the tiff files
user_name="INSERT_USER_NAME" # Input your own username to the website
password="INSERT_PASSWORD" # Input your own password to the website
downloads_dir="INSERT_DIRECTORY" # Change this to where your Downloads folder is located on your computer (e.g., C:\Users\o.elmaria\Downloads)
pages_to_download_at_once="3" # Set the number of files to download in parallel. If you have a fast internet connection and large RAM, consider increasing this number to 10
```
