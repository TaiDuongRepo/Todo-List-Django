# Generated by Django 4.2.11 on 2024-03-14 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0002_todos_remove_tasklist_tasks_delete_task_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Todos',
            new_name='Todo',
        ),
    ]
