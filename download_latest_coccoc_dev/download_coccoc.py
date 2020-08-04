from download_latest_coccoc_dev.configs.yaml_configs import CocCocConfigs
from download_latest_coccoc_dev.home_made_utilities.ftp_download import download_latest_coccoc_dev_installer


def main():
    import sys
    if len(sys.argv) <= 1:
        coccoc_version = download_latest_coccoc_dev_installer()
        if coccoc_version not in "Already latest":
            CocCocConfigs.update_coccoc_dev_version(coccoc_version)
        else:
            pass
    else:
        coccoc_version = download_latest_coccoc_dev_installer(needed_download_version=sys.argv[1])
        if coccoc_version not in "Already latest":
            CocCocConfigs.update_coccoc_dev_version(coccoc_version)
        else:
            pass


if __name__ == "__main__":
    main()
















