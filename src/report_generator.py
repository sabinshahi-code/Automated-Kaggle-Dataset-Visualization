import time
import os
from jinja2 import Environment, FileSystemLoader

def fetch_report(df, output_path="outputs", template_path="templates"):
    env = Environment(loader=FileSystemLoader(template_path))
    template = env.get_template("report.html")

    summary_html = df.describe(include="all").to_html()
    missing_html= df.isnull().sum().to_frame("Missing Count").to_html()

    plots_dir = os.path.join(output_path, "plots")

    if not os.path.isdir(plots_dir):
        raise FileNotFoundError(f"Plots directory not found: {plots_dir}")
    
    now = time.time()
    max_age_seconds = 90 #seconds count
    images = [
        os.path.join("plots", img)
        for img in os.listdir(plots_dir)
        if img.endswith(".png")
        and (now - os.path.getmtime(os.path.join(plots_dir, img))) <= max_age_seconds

    ]

    images.sort(
        key=lambda img: os.path.getmtime(
            os.path.join(plots_dir, os.path.basename(img))
        ),
        reverse=True
    )

    html_content = template.render(
        rows=df.shape[0],
        columns=df.shape[1],
        summary_tbl=summary_html,
        missing_tbl=missing_html,
        images=images
    )

    report_path = os.path.join(output_path, "report.html")
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    return report_path