import os
from jinja2 import Environment, FileSystemLoader

def fetch_report(df, output_path="outputs", template_path="templates"):
    env = Environment(loader=FileSystemLoader(template_path))
    template = env.get_template("report.html")

    summary_html = df.describe(include="all").to_html()
    missing_html= df.isnull().sum().to_frame("Missing Count").to_html()

    plots_dir = os.path.join(output_path, "plots")
    images = [
        os.path.join("plots", img)
        for img in os.listdir(plots_dir)
        if img.endswith(".png")

    ]

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