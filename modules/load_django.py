import os
import sys
import django

sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "braincomua_project")
    ),
)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "braincomua_project.settings")

django.setup()
