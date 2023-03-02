# 1. parallel_downloads_selenium
This is a README file that explains how to use the provided scripts to calculate the mean light intensity per country using the tiff files downloaded from this [link](https://eogdata.mines.edu/nighttime_light/nightly/rade9d/?C=N;O=D).
With this written documentation, you will learn how to:
- **Install Python**
- **Download the scripts from GitHub**
- **Create a virtual environment**
- **Install the Python dependencies/libraries**
- **Install the Chrome driver to run Python Selenium**
- **Call the Python script from R**
- **Solve the cropping problem**

# 2. Files in the Project Tree
You have **six files** in this repo.
- `download_images.py` --> The Python script that **downloads images in parallel**
- `cropping_function_demo.R` --> The R file that contains the code to calculate the **mean light intensity per country**
- `python_bat.bat` --> The batch file that will be used to **call the Python file from R**
- `.gitignore` --> The file that contains the **directories** and **files** to be ignored **before publishing to GitHub**
- `.RData` --> The file that contains the **history of the R file** from the last time I ran it so you can see **how the final dataset looks like**
- `requirements.txt` --> The **requirements file** that contains all the **Python dependencies** you need to install **after creating the virtual environment**

In addition to these files, which you can download from GitHub directly, you will need to create a new file called `.env`. You need to create the .env file in the root of the project/working directory, as shown in the screenshot below. 

![image](https://user-images.githubusercontent.com/98691360/222263773-5807f004-4382-4653-ad70-1878164eb62e.png)

This file will contain the following **global input variables** for the Python script and will look like this...
```python
url="https://eogdata.mines.edu/nighttime_light/nightly/rade9d/?C=N;O=D" # Set the URL to download the tiff files from
start_date="2018-01-01" # Set the start date of the tiff files
end_date="2018-12-31" # Set the end date of the tiff files
user_name="INSERT_USER_NAME" # Input your own username to the website
password="INSERT_PASSWORD" # Input your own password to the website
downloads_dir="INSERT_DIRECTORY" # Change this to where your Downloads folder is located on your computer (e.g., C:\Users\o.elmaria\Downloads)
pages_to_download_at_once="3" # Set the number of files to download in parallel. If you have a fast internet connection and large RAM, consider increasing this number to 10
```

# 3. How to Run the Code?
There are several steps you need to follow to run the code successfully on your computer. You might be able to skip some them depending on whether or not you have used Python and Selenium before on your computer

## 3.1 How to Install Python?
Please install the latest version of Python for your operating system using this [link](https://www.python.org/downloads/). Simply download the executable file and follow the setup instructions. The setup is very similar to installing a normal program on your computer.

## 3.2 How to Download the Scripts from GitHub?
If you have GitBash or, even better, the VSCode IDE, you can clone the repository using the command “git clone https://github.com/omar-elmaria/parallel_downloads_selenium.git”

If you don’t have GitBash or VSCode, you can also download the repo directly as a **zip file** by clicking the button shown in the screenshot below. However, I recommend you install VSCode because you will anyway need it in the following step.

![image](https://user-images.githubusercontent.com/98691360/222263227-9e66520d-892c-412f-857f-a7d1177d7724.png)

## Step 3.3: How to Create a Virtual Environment and Install the Dependencies?
First, you need to download an IDE such as **PyCharm** or **VSCode**. I recommend VSCode because it is free and has many plugins to work with all programming languages. You can use this [link](https://code.visualstudio.com/download) to download VSCode for your operating system. After VSCode is downloaded, please install the **plug-ins** you see in the screenshot below.

![image](https://user-images.githubusercontent.com/98691360/222264985-4ad1ed43-15d6-4ec6-a9b7-325efe3219f6.png)

After you download these extensions, you are ready to use Python. Python has a default version that gets installed on your computer automatically after you download it from the python.org website. You can use this one and install libraries and what not. However, it is highly recommended to create **virtual envrionments** to isolate **project dependencies** and keep them **independent of each other**. Follow the steps below to create a virtual environment:

- In VSCode, click on `File` > `Open Folder` > `Navigate to Your Working Directory Where You Downloaded the Scripts From GitHub`
- Type the following commands one by one in your terminal to **create** and **activate** your virtual environment 
```python
python -m venv venv_light_intensity
source venv_light_intensity/Scripts/activate
```
The first command **creates the virtual environment** and the **second one activates it**. After you type the second command, you should see (venv_light_intensity) appear next to or on top of your **current working directory** in VSCode's terminal. It should look similar to what is shown in the screenshot below.

![image](https://user-images.githubusercontent.com/98691360/222266327-7c95305b-39b9-49c2-9f34-7f0ee4513ccc.png)

- After activating your virtual environment, type the following command in your terminal --> `pip install -r requirements.txt`. This installs **all the required dependencies**
- To make sure the IDE uses the **right Python version**, click **“Ctrl-Shift-P”** > **Search for “Python: Select Interpreter”** and click on it > **Browse for the right Python executable**. You will find it in this path --> **“/venv_light_intensity/Scripts/python.exe”**
- If you create a `test.py` file, you should see the **Python version** and **name of the virtual environment**

![image](https://user-images.githubusercontent.com/98691360/222266917-2f9ebfc4-f4bc-42df-8599-b17735a381d5.png)

## Step 3.4: How to Install the Chrome driver to run Python Selenium?
You can follow the instructions in this 3-minute [video](https://www.youtube.com/watch?v=2WVxzRD6Ds4) to install the Chrome webdriver on your computer so you can run Selenium. The video mentions the version of Chrome. You can find that by pasting this URL into your normal Chrome search bar `chrome://settings/help`. The version should appear right away in the **About Chrome** section.

![image](https://user-images.githubusercontent.com/98691360/222534117-5c5d4a8b-28a1-4832-8d65-4b63c92f16f9.png)

## Step 3.4: Call the Python script from R
To call the Python script from R, you need to run the following two commands from your R script
```r
setwd("INSERT_PATH_TO_YOUR_WORKING_DIRECTORY") # Don't remove the double-quotes
shell.exec(file.path(getwd(), "python_bat.bat"))
```

The batch file itself need to have this command. The command takes the **Python executable** from the virtual environment and uses it to run the `download_images.py` file
```
"{INSERT_PATH_TO_VIRTUAL_ENVIRONMENT_FOLDER}\venv_light_intensity\Scripts\python.exe" "{INSERT_PATH_TO_WORKING_DIRECTORY}\download_images.py"
```
**P.S.** Don't forget the double-quotes. Also, you might need to replace the backslashes with forward slashes if you are on Windows

## Step 3.5: **How to Solve the Cropping Problem?**
In the repo, you will find a fully working version of the R code in the `cropping_function_demo.R` file. I believe the problem has to do with the .shp file you use in your script. What I did is that I extracted the country polygons from an R dataset called `wrld_simpl` and it worked like a charm.

The R script only uses **one date** and **one tiff file** to extract the mean light intensities because it is meant to show an illustrative example. What you will need to do is parametrize the date as you do in your original R script via a loop.

# Complete Workflow
Phew. This was a lot. I hope you're hanging in there with all of these instructions. In this section, I want to summarize how the workflow should look like after all the installations are done so you can can leave to run overnight.

1. Set the inputs in the `.env` file
2. Run the Python script from VSCode or from R using the instructions stated above
  - It is better to **first download the .tiff files** and then **run the R script** to extract the **mean_light_intensities**. This is because the Python script runs in parallel whereas the R script's for loop runs sequentially. To reconcile the two, the Python script has to be amended to download files sequentially. However, if we do that, it will take between 5-7 days to download all the .tiff files, assuming you only want to download one year worth of data
  -  Since this is a very long time, it is better to run the Python script in parallel to **download ALL the .tiff files first**, then use the R script to do the cropping. To do this, there are three options:
    -  Use an **external hard drive**
    -  Use a **Google Drive folder synced to your desktop** (assuming you have a G-mail premium account, which gives you access to **2 TB of storage**)
    -  Run the **Python + R scripts in batches**, manually deleting the downloaded files after you extract all the light intensities
