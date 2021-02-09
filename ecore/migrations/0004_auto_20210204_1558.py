# Generated by Django 3.1.6 on 2021-02-04 10:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecore', '0003_marchent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lenin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leninName', models.CharField(max_length=50)),
                ('leninCode', models.CharField(max_length=4)),
            ],
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='OrderId',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='ProductId',
        ),
        migrations.AlterField(
            model_name='marchent',
            name='code',
            field=models.CharField(max_length=4),
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='OrderItem',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.AddField(
            model_name='lenin',
            name='marchent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecore.marchent'),
        ),
    ]
