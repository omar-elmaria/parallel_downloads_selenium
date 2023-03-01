library(raster) # To convert the tif file to a raster object
library(maptools) # To get the polygons of each country
library(terra) # For cropping and masking

# Choose a date. In your script, you will parametrize the date based on the name of the tiff file
date = "20180101"

# Set the working directory
wd = "I:/My Drive/AUC Drive/Entrepreneurship/Freelancing/scraping_gigs/andre_image_downloads/"

# Change the tiff file to a raster object
temp <- raster(paste0(wd,"SVDNB_npp_d", date, ".rade9d.tif"))

# Define the list of countries
countries <- c(
  "Austria", "Belgium", "Bulgaria", "Croatia", "Cyprus", "Czech Republic", "Denmark",
  "Estonia", "Finland", "France", "Germany", "Greece", "Hungary", "Ireland", "Italy", "Latvia",
  "Lithuania", "Luxembourg", "Malta", "Netherlands", "Norway", "Poland", "Portugal", "Romania",
  "Slovakia", "Slovenia", "Spain", "Sweden", "Switzerland", "United Kingdom"
)

# Extract the polygons of each country from the "wrld_simpl" dataset
# In your script, you will use the .shp file to get the polygons. If it doesn't work, then use the wrld_simpl dataset
# The shp file might actually be what is causing the error
data(wrld_simpl)

# Define an empty data frame that will contain the mean light intensity values per country
df = data.frame(country=NA, mean_light_intensity=NA)

# Loop over all the countries
for (country in countries) {
  # Get the country polygon by filtering the "wrld_simpl" dataset
  country_polygon <- subset(wrld_simpl, NAME==country)

  # Crop the tiff file based on the country_polygon
  r2 <- crop(temp, extent(country_polygon))

  # Create a new Raster object that has the same values as r2, except for the cells that are NA (or other maskvalue) in a 'mask'
  r3 <- mask(r2, country_polygon)

  # Plot the country polygon with some visual enhancements
  plot(r3, main=paste0(country, "_", date))
  plot(country_polygon, add=TRUE, lwd=2)
  
  mean_light_intensity <- mean(as.numeric(as.vector(r2)), na.rm = TRUE)

  df_iter = data.frame(country = country, mean_light_intensity = mean_light_intensity)
  
  df <- rbind(df, df_iter)
}

# Remove the NAs
df <- na.omit(df)
