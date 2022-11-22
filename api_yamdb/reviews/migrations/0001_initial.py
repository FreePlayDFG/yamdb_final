# Generated by Django 2.2.16 on 2021-11-13 10:40

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('titles', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(help_text='Тест отзыва', max_length=256, verbose_name='Текст')),
                ('score', models.PositiveSmallIntegerField(default=None, help_text='Оставьте оценку', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)], verbose_name='Оценка')),
                ('pub_date', models.DateTimeField(auto_now_add=True, db_index=True, help_text='Дата публикации', verbose_name='Дата')),
                ('author', models.ForeignKey(help_text='Автор отзыва', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='review', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('title', models.ForeignKey(help_text='Название произведения', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='titles.Title', verbose_name='Произведение')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
                'ordering': ['id'],
                'unique_together': {('author', 'title')},
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(help_text='Напишите ваш комментарий', max_length=256, verbose_name='Комментарий')),
                ('pub_date', models.DateTimeField(auto_now_add=True, db_index=True, help_text='Дата публикации', verbose_name='Дата')),
                ('author', models.ForeignKey(help_text='Автор комментария', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('review', models.ForeignKey(help_text='Отзыв о произведении', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='reviews.Review', verbose_name='Отзыв')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
                'ordering': ['-pub_date'],
            },
        ),
    ]
