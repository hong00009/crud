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