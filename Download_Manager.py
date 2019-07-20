# os import to manipulate paths
import os
# shutil contains a simply .move function and that is this imports sole use
import shutil


class DownloadManager:
    """
       This Script simply organises your messy downloads folders
       by creating folders for common files and arranges them
       by extension into said folders
        """

    """ Reminder of indexs of various  lists for lists_of_exts varable below
        0 = executables,
        1 = videos
        2 = pics
        3 = docs
        4 = spreadsheets
        5 = presentations
        6 = compressed """

    # each list contains extensions
    lists_of_exts = [
        [".exe", ".EXE1", ".dmg", ".APP", ".JAR", ".PLX", ".PYC", ".X86"],  # 0

        [".mp4", ".mov", ".webm", ".yuv",
         ".wmv", ".svi", ".rmvb", ".rm",
         ".ogv", ".ogg", ".nsv", ".mpg",
         ".mpeg", ".flv", ".m2v" ".mp2",
         ".mpeg", ".mpe", ".mpv", ".m4p",
         ".m4v", ".gifv", ".avi", "amv",
         ".3gp", ".3g2"],  # 1

        [".tif", ".tiff", ".gif", ".jpeg",
         ".jpg", ".jif", ".jfif", ".jp2",
         ".jpx", ".j2k", ".j2c", ".fpx",
         ".pcd", ".png"],  # 2

        [".pdf", ".doc", ".docx", ".txt",
         ".ODT", ],  # 3

        [".XLS", ".XLSX", ".ODS"],  # 4

        [".PPT", ".PPTX"],  # 5

        [".rar", ".zip", ".gz", ".7z",
         ".TAR.GZ", ".TAZ"]  # 6
    ]
    """
    Reminder of indexs of various  lists
    0 = executables,
    1 = videos
    2 = pics
    3 = docs
    4 = spreadsheets
    5 = presentations
    6 = compressed 
     """

    downloads_folder = input("Enter the path to your Downloads folder (eg.C:\\Users\\Name\\Downloads) :  ")

    path = os.getcwd()

    # Get the current working directory
    current_dir = os.getcwd()
    print("The current working directory is: " + path)
    # catch windows and OS errors
    try:
        os.chdir(downloads_folder)
        path = os.getcwd()
        print("The new current working directory is: " + path)

        # checking  to see if path is correct and misc is created WILL RUN if other folders are deleted
        if path == downloads_folder and not os.path.exists(path + "\\Misc"):
            print("Making Directories.......")
            os.mkdir(path + "\\Apps and Install_Packages")
            print("Making Directories........")
            os.mkdir(path + "\\Videos")
            print("Making Directories......")
            os.mkdir(path + "\\Images")
            print("Making Directories.....")
            os.mkdir(path + "\\Documents")
            print("Making Directories....")
            os.mkdir(path + "\\Spreadsheets")
            print("Making Directories...")
            os.mkdir(path + "\\SlideShows")
            print("Making Directories..")
            os.mkdir(path + "\\Archives_and_Compressed_Files")
            print("Making Directories.")
            os.mkdir(path + "\\Misc")
        else:
            files = os.listdir(path)
            print("Directories are created already")
            for list in lists_of_exts:
                for item in list:
                    for file in files:
                        if file.endswith(item):
                            if lists_of_exts.index(list) == 0:
                                print("moving file too: " + path + "\\" + "Apps and Install_Packages")
                                shutil.move(path + "\\" + file, path + "\\Apps and Install_Packages\\" + file)
                            elif lists_of_exts.index(list) == 1:
                                print("moving file too: " + path + "\\" + "Videos")
                                shutil.move(path + "\\" + file, path + "\\Videos\\" + file)
                            elif lists_of_exts.index(list) == 2:
                                print("moving file too: " + path + "\\" + "Images")
                                shutil.move(path + "\\" + file, path + "\\Images\\" + file)
                            elif lists_of_exts.index(list) == 3:
                                print("moving file too: " + path + "\\" + "Documents")
                                shutil.move(path + "\\" + file, path + "\\Documents\\" + file)
                            elif lists_of_exts.index(list) == 4:
                                print("moving file too: " + path + "\\" + "Spreadsheets")
                                shutil.move(path + "\\" + file, path + "\\Spreadsheets\\" + file)
                            elif lists_of_exts.index(list) == 5:
                                print("moving file too: " + path + "\\" + "SlideShows")
                                shutil.move(path + "\\" + file, path + "\\SlideShows\\" + file)
                            elif lists_of_exts.index(list) == 6:
                                print("moving file too: " + path + "\\" + "Archives_and_Compressed_Files")
                                shutil.move(path + "\\" + file, path + "\\Archives_and_Compressed_Files\\" + file)
                        else:
                            print("No Files needed Moving")
    except WindowsError:
        print("WindowsError Throw")
    except OSError:
        print("WindowsError Throw")
    finally:
        os.chdir(current_dir)
