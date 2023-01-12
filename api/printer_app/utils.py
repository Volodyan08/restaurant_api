import subprocess
from celery import shared_task


@shared_task()
def generate_pdf(html, output_path):
    subprocess.run(["docker", "exec", "restaurant_api_wkhtmltopdf_1", "wkhtmltopdf", html, output_path])
