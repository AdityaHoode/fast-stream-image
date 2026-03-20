import os
from dotenv import load_dotenv
from imagekitio import ImageKit

load_dotenv()

imageKit = ImageKit(private_key=os.getenv("IMAGEKIT_PRIVATE_KEY"))

