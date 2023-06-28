# Model

- `models.py` 작성
```python

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    # 입력값 형식/규격 정의    
```


- 번역본 생성
    - `python manage.py makemigrations`
    `0001_initial.py` 등

- DB에 반영
    - `python manage.py migrate`

- `admin.py` 수정
``` python
from django.contrib import admin
from .models import Post
# 나의 models.py 안의 Post class

admin.site.register(Post)
# admin 사이트에 Post class를 등록
```