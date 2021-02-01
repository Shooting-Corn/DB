from google_images_download import google_images_download
num = 0
while(num < 35):
    response = google_images_download.googleimagesdownload()

    arguments={"keywords":"clown","limit":100,"print_urls":True}
    paths = response.download(arguments)
    num+=1