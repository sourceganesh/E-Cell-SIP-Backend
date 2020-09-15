from django.core import exceptions

#Will raise an exception when the user tries to upload a file greater that max limit
class FileSizeExceedException(Exception):
    def __init__(self):
        self.return_message = "File Size Exceeded"