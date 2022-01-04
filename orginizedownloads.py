import os
from pathlib import Path

# code : .js, .py, .html, .java, .css
# documents : .ppt, .pptx, .xls, .xlsx, .doc, .docx, .txt, .tex
# pdf files : .pdf
# images : .bmp , .gif .ico , .jpeg, .jpg , .png ,.svg , .tif, .tiff
# applications: .apk, .bat , .bin , exe , .jar , .msi , .py
# others : all other extentions

folders = {
    "Code" : {'html', 'css', 'py', 'java'},
    "Pdf Files" : {'pdf'},
    "Documents" : {'ppt','pptx','pdf','xls', 'xlsx','doc','docx','txt', 'tex', 'epub'}, 
    "Applications" : {'exe'}, 
    "Images" : {'bmp','gif','jpeg','jpg','png','jfif','svg','tif','tiff'}, 
    "Others" : {"NONE"}
}

download_path = r"C:\Users\ammar_m4r3wcb\Downloads"

onlyfiles = [os.path.join(downloads_path, file) 
        for file in os.listdir(downloads_path) 
            if os.path.isfile(os.path.join(downloads_path, file))]

onlyfolders = [os.path.join(downloads_path, file) 
        for file in os.listdir(downloads_path) 
            if not os.path.isfile(os.path.join(downloads_path, file))]

extension_filetype_map = {extension: fileType 
        for fileType, extensions in folder_names.items() 
                for extension in extensions }

# make folders

folder_paths = [os.path.join(downloads_path, folder_name) 
        for folder_name in folder_names.keys()]

[os.mkdir(folderPath) 
        for folderPath in folder_paths if not os.path.exists(folderPath)]

# move files
def new_path(old_path):
    extension = str(old_path).split('.')[-1]
    amplified_folder = extension_filetype_map[extension] if extension in extension_filetype_map.keys() else 'Others'
    final_path = os.path.join(downloads_path,amplified_folder, str(old_path).split('\\')[-1])
    return final_path
    

[Path(eachfile).rename(new_path(eachfile)) for eachfile in onlyfiles]

# Move other folders
[Path(onlyfolder).rename(os.path.join(downloads_path,'Others', str(onlyfolder).split('\\')[-1])) 
        for onlyfolder in onlyfolders 
                if str(onlyfolder).split('\\')[-1] not in folder_names.keys()]


sys.exit()