import tarfile, os, shutil

def extract_all_tars(input_folder, output_folder):
    for file in os.listdir(input_folder):
        if file.endswith("tar.gz"):
            tar = tarfile.open(input_folder + "/" + file, "r:gz")
            tar.extractall(path = input_folder)
            tar.close()
            for innerfile in os.listdir(input_folder + "/" + file[0:len(file) - 7]):
                if innerfile.endswith("pdf"):
                    shutil.move(input_folder + "/" +file[0:len(file) - 7] + "/" + innerfile, output_folder + "/" + innerfile)
#First parameter is the input folder (so the folder that has all the tar.gz files)
#Second parameter is the output folder (the folder where you want all the PDFs to appear)
extract_all_tars("text", "Try")
