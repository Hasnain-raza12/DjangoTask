# Generated by Django 4.2.1 on 2023-05-03 14:19

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
            name='Companion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currently_in_contract', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('MC', 'Motorcycle'), ('SD', 'Sedan'), ('HB', 'Hatchback'), ('SUV', 'SUV'), ('VN', 'Van')], max_length=3)),
                ('sitting_capacity', models.PositiveIntegerField()),
                ('color', models.CharField(max_length=50)),
                ('registration_number', models.CharField(max_length=20, unique=True)),
                ('status', models.CharField(choices=[('EM', 'Empty'), ('FL', 'Full'), ('IA', 'Inactive')], max_length=2)),
                ('front_picture', models.ImageField(upload_to='vehicle_images')),
                ('side_picture', models.ImageField(upload_to='vehicle_images')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_vehicles', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='updated_vehicles', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('dob', models.DateField()),
                ('contact_numbers', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('landmark', models.CharField(max_length=100)),
                ('town', models.CharField(max_length=50)),
                ('gps_coordinates', models.CharField(max_length=50)),
                ('bio', models.TextField(blank=True)),
                ('affiliated_as', models.CharField(choices=[('ST', 'Student'), ('FC', 'Faculty'), ('SF', 'Staff')], max_length=2)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_profiles', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='updated_profiles', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('num_contracts', models.PositiveIntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('effective_start_date', models.DateField()),
                ('expiry_date', models.DateField()),
                ('fuel_share', models.DecimalField(decimal_places=2, max_digits=3)),
                ('maintenance_share', models.DecimalField(decimal_places=2, max_digits=3)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('schedule', models.DateTimeField()),
                ('companion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baham.companion')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contracts_created', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contracts_updated', to=settings.AUTH_USER_MODEL)),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baham.vehicle')),
            ],
        ),
    ]
