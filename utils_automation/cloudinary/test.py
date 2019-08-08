import cloudinary
from cloudinary.api import delete_resources_by_tag, resources_by_tag
from cloudinary.uploader import upload
from cloudinary.utils import cloudinary_url
# Initiate cloudinary sdk
cloudinary.config(
    cloud_name='cuongld',
    api_key='563773355814327',
    api_secret='VHwdNYRZVdCML2QtvJLP5cp2wPo'
)

# Upload an image
cloudinary.uploader.upload("lake.jpg")
