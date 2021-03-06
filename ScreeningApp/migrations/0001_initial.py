from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('candidate_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=500)),
                ('email', models.EmailField(max_length=254)),
                ('level_of_expertise', models.CharField(choices=[('Entry Level', 'Entry Level'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced'), ('Expert', 'Expert')], max_length=100)),
                ('area_of_expertise', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name': 'Candidate',
                'verbose_name_plural': 'Candidates',
            },
        ),
        migrations.CreateModel(
            name='Expertise',
            fields=[
                ('expertise_id', models.AutoField(primary_key=True, serialize=False)),
                ('expertise', models.CharField(max_length=300, unique=True)),
            ],
            options={
                'verbose_name': 'Expertise',
                'verbose_name_plural': 'Expertises',
            },
        ),
        migrations.CreateModel(
            name='Expertise_Area',
            fields=[
                ('expertise_area_id', models.AutoField(primary_key=True, serialize=False)),
                ('area_of_expertise', models.CharField(max_length=300, unique=True)),
                ('category_of_expertise', models.CharField(max_length=300)),
            ],
            options={
                'verbose_name': 'Expertise_Area',
                'verbose_name_plural': 'Expertise_Areas',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('question_id', models.AutoField(primary_key=True, serialize=False)),
                ('question', models.TextField()),
                ('qtype', models.CharField(choices=[('multiple choice', 'Multiple Choice'), ('yes/no', 'Yes/No')], max_length=100)),
                ('option_1', models.TextField(blank=True)),
                ('option_2', models.TextField(blank=True)),
                ('option_3', models.TextField(blank=True)),
                ('option_4', models.TextField(blank=True)),
                ('answer', models.TextField(blank=True)),
                ('category_of_expertise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ScreeningApp.Expertise_Area')),
                ('expertise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ScreeningApp.Expertise')),
            ],
            options={
                'verbose_name': 'Question',
                'verbose_name_plural': 'Questions',
            },
        ),
        migrations.CreateModel(
            name='Screenings',
            fields=[
                ('screening_id', models.AutoField(primary_key=True, serialize=False)),
                ('screening_uuid', models.CharField(blank=True, max_length=50)),
                ('candidate_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ScreeningApp.Candidate')),
            ],
            options={
                'verbose_name': 'Screening',
                'verbose_name_plural': 'Screenings',
            },
        ),
        migrations.CreateModel(
            name='Screenings_Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidate_ans', models.CharField(blank=True, max_length=50)),
                ('correct_ans', models.CharField(blank=True, max_length=50)),
                ('answer_correctness', models.CharField(blank=True, max_length=10)),
                ('question', models.ManyToManyField(related_name='questions', to='ScreeningApp.Question')),
                ('screening_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ScreeningApp.Screenings', verbose_name='candidate_name')),
            ],
            options={
                'verbose_name': 'Screening_Question',
                'verbose_name_plural': 'Screenings_Questions',
            },
        ),
        migrations.AddField(
            model_name='expertise',
            name='category_of_expertise',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ScreeningApp.Expertise_Area'),
        ),
    ]