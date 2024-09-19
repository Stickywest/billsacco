# Generated by Django 5.0.6 on 2024-08-16 15:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "accounts",
            "0003_remove_blog_author_remove_blog_updated_at_blog_video_and_more",
        ),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Account",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "balance",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("last_savings_date", models.DateTimeField(blank=True, null=True)),
                (
                    "account_type",
                    models.CharField(
                        choices=[
                            ("FD", "Fixed Deposit"),
                            ("J", "Junior"),
                            ("SC", "Shared Capital"),
                            ("C", "Chama"),
                        ],
                        default="FD",
                        max_length=2,
                    ),
                ),
                (
                    "account_number",
                    models.CharField(blank=True, max_length=12, unique=True),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Loan",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("amount", models.DecimalField(decimal_places=2, max_digits=10)),
                ("borrowed_at", models.DateTimeField(auto_now_add=True)),
                (
                    "account",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="accounts.account",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Transaction",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("amount", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "transaction_type",
                    models.CharField(
                        choices=[("Deposit", "Deposit"), ("Withdrawal", "Withdrawal")],
                        max_length=10,
                    ),
                ),
                ("date", models.DateTimeField(auto_now_add=True)),
                (
                    "account",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="accounts.account",
                    ),
                ),
            ],
        ),
    ]
