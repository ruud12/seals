from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from erp.models import serviceReport
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm, inch



class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        canvas.Canvas.__init__(self, *args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)

        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_number(num_pages)
        canvas.Canvas.save(self)

    def draw_page_number(self, page_count):
        self.drawRightString( 211 * mm, 15 * mm + (0.2 * inch),
            "Page %d of %d" % (self._pageNumber, page_count))



class MyPrint:
    def __init__(self, buffer, pagesize, report):
        self.buffer = buffer
        self.report = report
        if pagesize == 'A4':
            self.pagesize = A4
        elif pagesize == 'Letter':
            self.pagesize = letter
            self.width, self.height = self.pagesize

    @staticmethod
    def _header_footer(canvas, doc):
        canvas.saveState()
        styles = getSampleStyleSheet()

        # header

        header = Paragraph('this is a multiline header.' * 5, styles['Normal'])
        w, h = header.wrap(doc.width, doc.topMargin)
        header.drawOn(canvas, doc.leftMargin, doc.height + doc.topMargin + doc.bottomMargin - 2*h)

        # footer 
        footer = Paragraph('this is a multiline footer.' * 5, styles['Normal'])
        w, h = footer.wrap(doc.width, doc.bottomMargin)
        footer.drawOn(canvas, doc.leftMargin, h)

        canvas.restoreState()


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
        elements.append(Paragraph('Vessel name: '+report.seal.vessel.name, styles['Normal']))
        elements.append(Paragraph('IMO: '+report.seal.vessel.imo, styles['Normal']))
        elements.append(Paragraph('Company: '+report.seal.company.name, styles['Normal']))


        elements.append(Paragraph('Contact information', styles['Heading2']))
        for i, contact in enumerate(report.seal.vessel.contacts.all()):
            elements.append(Paragraph(contact.first_name + " " + contact.last_name +": "+contact.position, styles['Normal']))






        doc.build(elements, onFirstPage = self._header_footer, onLaterPages = self._header_footer, canvasmaker=NumberedCanvas)

        pdf = buffer.getvalue()
        buffer.close()

        return pdf