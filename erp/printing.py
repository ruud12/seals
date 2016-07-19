from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib import colors
from erp.models import serviceReport
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm, inch






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


        elements.append(Paragraph('Service report '+report.seal.vessel.name, styles['Heading1']))

        
        elements.append(Paragraph('General information', styles['Heading2']))
        elements.append(Paragraph('Serial number seal: '+report.seal.x_number, styles['Normal']))
        elements.append(Paragraph('Type: '+report.seal.seal_type, styles['Normal']))
        elements.append(Paragraph('Size: '+str(report.seal.size), styles['Normal']))
        elements.append(Paragraph('Superintendant: '+report.superintendant.first_name+" "+report.superintendant.last_name, styles['Normal']))


        elements.append(Paragraph('Vessel information', styles['Heading2']))

        data= [['Vessel', report.seal.vessel.name],
           ['Company', report.seal.company.name],
           ['IMO', report.seal.vessel.imo]]


        t=Table(data, hAlign='LEFT') #,2*[3*inch], 3*[0.4*inch])
        t.setStyle(TableStyle([('ALIGN',(0,0),(-1,-1),'LEFT'),
                       ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
                       ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                       ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                       ]))

        elements.append(t)


        elements.append(Paragraph('Contact information', styles['Heading2']))
        for i, contact in enumerate(report.seal.vessel.contacts.all()):
            elements.append(Paragraph(contact.first_name + " " + contact.last_name +": "+contact.position, styles['Normal']))






        doc.build(elements)

        pdf = buffer.getvalue()
        buffer.close()

        return pdf