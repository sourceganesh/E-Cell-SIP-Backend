from django.core import exceptions

class FileSizeExceedException(Exception):
    def __init__(self):
        self.return_message = "File Size Exceeded"