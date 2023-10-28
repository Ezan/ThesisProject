

def extract_image():
    # -*- coding: utf-8 -*-
    """
    Created on Mon Mar 16 16:55:53 2020

    @author: Jaya Sindhura Pailla

    This Script Extracts all the images from all the Research Papers(.pdf format) and stores them individually by creating seperate folder for each research paper

    Step 1: Place the research papers in pdf format in a path (eg: files_path = '/home/jpailla/Papers')
    Step 2: Create a directory "Images" where the folders for each paper gets created dynamically and extracted images gets stored here
    Step 3: pip install PyMupdf #to import the library "fitz" (to read pdf and etract images from pdf files)
    step 4: set the source path & destination path in different variables

    """
    import fitz
    import os
    import glob
    import shutil

    print(os.getcwd())

    files_path = '../../datasets/papers'
    Images_path = '../../datasets/images'
    # directory = 'C:\\Users\\sindh\\Desktop\\UNO\\pdf_images_extraction\\Files'

    """
    ##Work in progress: code to Delete the earlier extracted images,not working accurately,sometimes all folder images are not getting deleted##
    for filename in os.listdir(files_path): #read the files from the path
        filenm = os.path.splitext(filename)[0]
        os.chdir(Images_path)
        if os.path.exists(filenm):
           #os.remove(filenm) #using os.remove if file exists is throwing "PermissionError: [WinError 5] Access is denied"
           shutil.rmtree(filenm, ignore_errors=True)
           print(filenm+ "succesfully deleted")
    """

    owd = os.getcwd()
    paper_index = 1

    for filename in os.listdir(files_path):
        os.chdir(owd)  # read the files from the path
        print(os.getcwd())

        try:
            filename_withpath = os.path.join(files_path, filename)
            filenm = os.path.splitext(filename)[0]  # extracting only the filename without extension .pdf
            print(filenm)

            # os.chdir(Images_path)
            os.mkdir(Images_path + '/' + filenm)  # create seperate directory by pdf filename to save images
            file = fitz.open(filename_withpath)
            page = len(file)  # return the number of pages in each image file
            os.chdir(
                Images_path + '/' + filenm)  # change directory to the dir created on the pdf filename to save all the images in this location

            for i in range(page):  # from 1 to end of pages in each file
                j = 1
                for image in file.get_page_images(i):  # reads each image one by one
                    customxref = image[0]  # every image will have a xref number,store that in a variable
                    pic = fitz.Pixmap(file,
                                      customxref)  # pixmap (pixelmap) helps to extract the pixel map of the image provided from the file
                    finalpic = fitz.Pixmap(fitz.csRGB,
                                           pic)  # convert to RGB,becoz we are not sure in which format the pic os going to be
                    finalpic.save(str(paper_index) + "_" + str(j) + ".png")  # saving the image
                    pic = None
                    finalpic = None
                    j = j + 1
            paper_index += 1
        except Exception as e:
            print(e)
            continue


# if __name__ == "__main__":
#     extract_image()

