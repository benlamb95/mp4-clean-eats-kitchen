# Generated by Django 3.2.13 on 2022-06-21 09:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_auto_20220614_1346'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='step',
            name='recipe',
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.CharField(default='Enter Ingredients', max_length=150),
        ),
        migrations.AddField(
            model_name='recipe',
            name='steps',
            field=models.CharField(default='Enter Steps', max_length=150),
        ),
        migrations.AlterField(
            model_name='comment',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='recipes.recipe'),
        ),
        migrations.DeleteModel(
            name='RecipeIngredient',
        ),
        migrations.DeleteModel(
            name='Step',
        ),
    ]
