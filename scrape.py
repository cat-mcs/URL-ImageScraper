
# Importing Libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib.request
import time
import os

# Function to download image
def download_image(filename, src, num, dir):
    
    try:
        # creating the png file name
        filename = filename + str(num) + '.png'  
        # creating the image path
        image_path = os.path.abspath(os.path.join(os.getcwd(), dir, filename))
        # downloading the image
        urllib.request.urlretrieve(src, image_path)  
        # printing the success message
        print(f'{filename}')
    except:
        pass

# Function to collect image links
def image_links(filename, dir):
    
    # counter for file name
    n = 0 
    
    # getting the <img> tags for url in question
    try:
        time.sleep(5)
        images = driver.find_elements(By.XPATH, "//img")
        print('Number of images: ', len(images))
    except:
        pass

    # iterating through the list of images
    for image in images:
            try:
                # getting the src attribute
                src = image.get_attribute('src')
                # calling the download_image function
                download_image(filename, src, n, dir)
            except:
                pass

            # counter increase
            n += 1
        
# main function
if __name__ == '__main__':
    name = input('Please Provide The Person Name: \n')
    url = input('Please Provide The Page URL: \n')
    dir = 'scrapedpng'
    
    # setting up the chrome driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)
    
    # if directory does not exist
    if not os.path.isdir(dir):
        os.makedirs(dir)
    
    # calling the image_links function 
    image_links(name, dir)
