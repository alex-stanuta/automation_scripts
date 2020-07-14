#Script to create a function for generating reports with the reportlab library

#reports.py
#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(attachment, title, paragraph):
	styles = getSampleStyleSheet()
	report = SimpleDocTemplate(attachment)
	report_title = Paragraph(title, styles["h1"])
	#table_style = [('NOGRID', (0,0), (-1, -1), 0)]
	#report_table = Table(data = paragraph, style = table_style, hAlign = 'LEFT')
	empty_line = Spacer (1,20)
	report_data = Paragraph(paragraph,styles["Normal"])
	report.build([report_title, empty_line, report_data])

