from django.core.files.storage import FileSystemStorage

class ProfileImageStorage(FileSystemStorage):

    def get_available_name(self, name: str, max_length: int | None = None) -> str:
        self.delete(name) # Delete previous picture profile
        return super().get_available_name(name, max_length)
    
    