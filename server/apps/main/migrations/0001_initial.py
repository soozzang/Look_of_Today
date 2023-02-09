# Generated by Django 3.2 on 2023-02-09 05:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Clothes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='main/images/clothes/%Y/%m/%d')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('buying', models.TextField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('like', models.ManyToManyField(blank=True, related_name='clothesLike', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Acc',
            fields=[
                ('clothes_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.clothes')),
            ],
            bases=('main.clothes',),
        ),
        migrations.CreateModel(
            name='Bottom',
            fields=[
                ('clothes_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.clothes')),
            ],
            bases=('main.clothes',),
        ),
        migrations.CreateModel(
            name='Outer',
            fields=[
                ('clothes_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.clothes')),
            ],
            bases=('main.clothes',),
        ),
        migrations.CreateModel(
            name='Shoes',
            fields=[
                ('clothes_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.clothes')),
            ],
            bases=('main.clothes',),
        ),
        migrations.CreateModel(
            name='Top',
            fields=[
                ('clothes_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.clothes')),
            ],
            bases=('main.clothes',),
        ),
        migrations.CreateModel(
            name='Talk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('공동 구매', '공동 구매'), ('오픈런', '오픈런'), ('고민방', '고민방')], max_length=5)),
                ('img', models.ImageField(blank=True, null=True, upload_to='main/images/commu/%Y/%m/%d')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('likes', models.ManyToManyField(blank=True, related_name='Talk_Likes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_img', models.ImageField(upload_to='main/images/post/%Y/%m/%d')),
                ('title', models.CharField(max_length=100)),
                ('open', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('likes', models.ManyToManyField(blank=True, related_name='Likes', to=settings.AUTH_USER_MODEL)),
                ('acc', models.ManyToManyField(blank=True, related_name='Acc', to='main.Acc')),
                ('bottom', models.ManyToManyField(blank=True, related_name='Bottom', to='main.Bottom')),
                ('outer', models.ManyToManyField(blank=True, related_name='Outer', to='main.Outer')),
                ('shoes', models.ManyToManyField(blank=True, related_name='Shoes', to='main.Shoes')),
                ('top', models.ManyToManyField(blank=True, related_name='Top', to='main.Top')),
            ],
        ),
        migrations.CreateModel(
            name='TalkComment',
            fields=[
                ('comment_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.comment')),
                ('talk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.talk')),
            ],
            bases=('main.comment',),
        ),
        migrations.CreateModel(
            name='PostComment',
            fields=[
                ('comment_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.comment')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.post')),
            ],
            bases=('main.comment',),
        ),
    ]
