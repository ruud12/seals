from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib import colors
from isah.models import ServiceReport
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm, inch
from datetime import datetime
import time





class MyPrint:
    def __init__(self, buffer, pagesize, report):
        self.buffer = buffer
        self.report = report
        if pagesize == 'A4':
            self.pagesize = A4
        elif pagesize == 'Letter':
            self.pagesize = letter
            self.width, self.height = self.pagesize

    


    def export_report(self):
        buffer = self.buffer
        report = self.report
        doc = SimpleDocTemplate(buffer, 
            rightMargin = 72,
            leftMargin = 72,
            topMargin = 72,
            bottomMargin = 72,
            pagesize = self.pagesize)

        elements = []

        styles = getSampleStyleSheet()
        styles.add(ParagraphStyle(name='centered', alignment=TA_CENTER))

        elements.append(Paragraph('Service report '+report.ls.company.name, styles['Heading1']))
        elements.append(Paragraph('Superintendant: '+report.superintendant.first_name+" "+report.superintendant.last_name, styles['Normal']))
        elements.append(Paragraph('Email superintendant: '+report.superintendant.email, styles['Normal']))
        elements.append(Paragraph('LS order no.: '+report.ls.LS_number, styles['Normal']))
        elements.append(Paragraph('Company: '+report.ls.company.name, styles['Normal']))
        elements.append(Paragraph('Location: '+report.location, styles['Normal']))



        elements.append(Paragraph('Date from: '+report.date_from.strftime("%d-%m-%Y"), styles['Normal']))
        elements.append(Paragraph('Date to: '+report.date_to.strftime("%d-%m-%Y"), styles['Normal']))

        for seal in report.ls.seals.all():
            elements.append(Paragraph(seal.serial_number, styles['Heading2']))
            data= [
                ['Serial number seal', seal.serial_number],
                ['Type', seal.seal_type.name],
                ['Size', str(seal.size)],
                ['Side', seal.side],
                ['Vessel', str(seal.vessel.name)],
                ['IMO', seal.vessel.imo_number]
            ]

            t=Table(data, hAlign='LEFT') #,2*[3*inch], 3*[0.4*inch])
            t.setStyle(TableStyle([('ALIGN',(0,0),(-1,-1),'LEFT'),
                       ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
                       ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                       ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                       ]))

            elements.append(t)


        doc.build(elements)

        pdf = buffer.getvalue()
        buffer.close()

        return pdf