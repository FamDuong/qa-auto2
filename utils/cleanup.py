

class Files:
    def delete_files_in_folder(self, mydir, endwith):
        import os
        filelist = [f for f in os.listdir(mydir) if f.endswith(endwith)]
        for f in filelist:
            os.remove(os.path.join(mydir, f))
