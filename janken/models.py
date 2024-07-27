from django.db import models

class GameResult(models.Model):
    CHOICES = (
        ('G', 'グー'),
        ('C', 'チョキ'),
        ('P', 'パー'),
    )
    user_choice = models.CharField(max_length=1, choices=CHOICES)
    computer_choice = models.CharField(max_length=1, choices=CHOICES)
    result = models.CharField(max_length=10)  # 勝ち、負け、引き分け