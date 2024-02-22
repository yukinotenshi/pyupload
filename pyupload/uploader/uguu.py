from pyupload.uploader.base import Uploader


class UguuUploader(Uploader):
    def __init__(self, filename):
        self.filename = filename
        self.file_host_url = 'https://uguu.se/upload'

    def execute(self):
        file = open(self.filename, 'rb')
        try:
            data = {'files[]': (file.name, file, self._mimetype())}
            response = self._multipart_post(data)
        finally:
            file.close()

        return response.json()['files'][0]['url']
