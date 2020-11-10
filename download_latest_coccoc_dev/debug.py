from download_latest_coccoc_dev.home_made_utilities.ftp_download import get_latest_directory_by_set_up_exe_date
import logging

LOGGER = logging.getLogger(__name__)

def main():
    from ftplib import FTP
    with FTP('browser3v.dev.itim.vn') as ftp:
        ftp.login('anonymous', '')
        ftp.cwd('corom')
        folders_list = ftp.nlst()
    LOGGER.info(folders_list)


if __name__ == "__main__":
    from ftplib import FTP
    with FTP('browser3v.dev.itim.vn') as ftp:
        ftp.login('anonymous', '')
        ftp.cwd('corom')
        print(get_latest_directory_by_set_up_exe_date(ftp))



