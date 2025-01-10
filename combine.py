#To combine all findings and output a pdf

from Singapore_scraper import Singapore
from US_scraper import USA
from Japan_alert_scraper import Japan_Alert
from Japan_vuln_scraper import Japan_Vuln
from China_scraper import China
from Australia_scraper import Australia

import pdfkit

# Generate HTML content
html_content = "<html><head><title>New Alerts Report</title></head><body>"
html_content += "<h1>New Alerts Report</h1>"


#Singapore
sg_alerts = Singapore()
html_content += f"<h2>Singapore</h2><ul>"
for alert in sg_alerts:
    html_content += f"<li><strong>Title:</strong> {alert['title']}<br>"
    html_content += f"<strong>Date:</strong> {alert['date']}<br>"
    html_content += f"<strong>Link:</strong> <a href='{alert['link']}'>{alert['link']}</a></li><br>"
html_content += "</ul>"


#US
usa_alerts = USA()
html_content += f"<h2>US</h2><ul>"
for alert in usa_alerts:
    html_content += f"<li><strong>{alert['rating']}</strong><br>"
    html_content += f"<li><strong>Title:</strong> {alert['title']}<br>"
    html_content += f"<strong>Date:</strong> {alert['date']}<br>"
    html_content += f"<strong>Link:</strong> <a href='{alert['link']}'>{alert['link']}</a></li><br>"
html_content += "</ul>"


#Japan Alert
japan_alerts= Japan_Alert()
html_content += f"<h2>Japan Alerts</h2><ul>"
for alert in japan_alerts:
    html_content += f"<li><strong>Title:</strong> {alert['title']}<br>"
    html_content += f"<strong>Date:</strong> {alert['date']}<br>"
    html_content += f"<strong>Link:</strong> <a href='{alert['link']}'>{alert['link']}</a></li><br>"
html_content += "</ul>"


#Japan Vuln
japan_vulns = Japan_Vuln()
html_content += f"<h2>Japan Vulns</h2><ul>"
for alert in japan_vulns:
    html_content += f"<li><strong>ID: </strong>{alert['id']}<br>"
    html_content += f"<li><strong>Title:</strong> {alert['title']}<br>"
    html_content += f"<strong>Date:</strong> {alert['date']}<br>"
    html_content += f"<strong>Link:</strong> <a href='{alert['link']}'>{alert['link']}</a></li><br>"
html_content += "</ul>"


#China
china_alerts = China()
html_content += f"<h2>China</h2><ul>"
for alert in china_alerts:
    html_content += f"<li><strong>Title:</strong> {alert['title']}<br>"
    html_content += f"<strong>Date:</strong> {alert['date']}<br>"
    html_content += f"<strong>Link:</strong> <a href='{alert['link']}'>{alert['link']}</a></li><br>"
html_content += "</ul>"


#Australia
australia_alerts = Australia()
html_content += f"<h2>US</h2><ul>"
for alert in australia_alerts:
    html_content += f"<li><strong>{alert['rating']}</strong><br>"
    html_content += f"<li><strong>Title:</strong> {alert['title']}<br>"
    html_content += f"<strong>Date:</strong> {alert['date']}<br>"
    html_content += f"<strong>Link:</strong> <a href='{alert['link']}'>{alert['link']}</a></li><br>"
html_content += "</ul>"


html_content += "</body></html>"

# Save to PDF
path_wkhtmltopdf = "C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
pdfkit.from_string(html_content, "new_alerts_report.pdf", configuration=config)