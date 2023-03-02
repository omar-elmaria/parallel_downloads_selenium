### Full script template ###

# Import libraries
library(raster) # To convert the tif file to a raster object
library(maptools) # To get the polygons of each country
library(terra) # For cropping and masking

# Set the working directory
wd = "INSERT_PATH_TO_THE_WORKING_DIRECTORY"

# Define the list of countries
countries <- c(
  "Austria", "Belgium", "Bulgaria", "Croatia", "Cyprus", "Czech Republic", "Denmark",
  "Estonia", "Finland", "France", "Germany", "Greece", "Hungary", "Ireland", "Italy", "Latvia",
  "Lithuania", "Luxembourg", "Malta", "Netherlands", "Norway", "Poland", "Portugal", "Romania",
  "Slovakia", "Slovenia", "Spain", "Sweden", "Switzerland", "United Kingdom"
)

# Start and end date (provide in format "YYYY-MM-DD")
start_date <- "2018-01-01"
end_date <- "2018-12-31"

# Generate a sequence of dates to process
dates <- seq(
  from = as.Date(start_date, format = "%Y-%m-%d"),
  to = as.Date(end_date, format = "%Y-%m-%d"),
  by = "1 day"
)

# Loop through the dates and convert each one to the desired numeric format
date_numeric <- format(dates, format = "%Y%m%d")

# Here, the list where all maps are stored is created
nightlydata <- matrix(nrow = length(dates), ncol = length(countries)+1)
colnames(nightlydata) <- c("date", as.character(countries))
nightlydata[, 1] <- date_numeric

for (date in date_numeric) {
  # The whole raster is loaded into R. This step assumes that you have already downloaded the tiff files using the Python script
  temp <- raster(paste0(wd,"SVDNB_npp_d", date, ".rade9d.tif"))
  
  # Continue the rest of the code to extract the mean light intensities as explained in cropping_function_demo.R (line 22 to 53)
}