from django.db import models
from django.utils import timezone
import uuid
from django.contrib.auth.models import User  # ユーザーモデルをインポート
#ログインユーザごとにデータの切り替え



class Diary(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateField(verbose_name='日付', default=timezone.now)
    title = models.CharField(verbose_name='タイトル', max_length=40)
    text = models.CharField(verbose_name='本文', max_length=400)
    created_at = models.DateTimeField(verbose_name='作成日時', default=timezone.now)
    updated_at = models.DateTimeField(verbose_name='編集日時', blank=True, null=True)
    contributor = models.ForeignKey(User, on_delete=models.CASCADE)  # 投稿者を表す外部キー