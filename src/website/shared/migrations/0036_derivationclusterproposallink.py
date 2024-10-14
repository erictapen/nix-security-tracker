# Generated by Django 4.2.16 on 2024-10-14 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shared', '0035_metric_attack_complexity_metric_attack_vector_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DerivationClusterProposalLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provenance_flags', models.IntegerField()),
                ('derivation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shared.nixderivation')),
                ('proposal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shared.cvederivationclusterproposal')),
            ],
        ),
    ]
