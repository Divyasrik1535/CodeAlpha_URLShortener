from django.db import models
import string
import random
class URL(models.Model):
    original_url = models.URLField(max_length=500)
    short_code = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        if not self.short_code:
            self.short_code = self.generate_short_code()
        super().save(*args, **kwargs)
    
    def generate_short_code(self):
        characters = string.ascii_letters + string.digits
        while True:
            code = ''.join(random.choices(characters, k=6))
            if not URL.objects.filter(short_code=code).exists():
                return code
    
    def __str__(self):
        return f"{self.short_code} -> {self.original_url}"