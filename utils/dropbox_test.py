import dropbox, sys, os

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

    def get_file(self, path_local, path_dropbox):
        dbx = dropbox.Dropbox(self.access_token)
        dbx.files_download_to_file(path_local, path_dropbox)


def main():
    access_token = 'u-IiRmPV-VYAAAAAAAABtV50rZLN-NzV51Q1SOOGXrnNfAV4HJov6xClYbbqfkYK'
    transferData = TransferData(access_token)

    file_from = '../screenshots/11-14-36.624.png'
    file_to = '/Automation ScreenShot/11-14-36.624.png'  # The full path to upload the file to, including the file name

    # API v2
    # transferData.get_file(file_from, file_to)
    transferData.upload_file(file_from,file_to)


if __name__ == '__main__':
    main()
