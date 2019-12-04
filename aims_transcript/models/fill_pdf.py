#! /usr/bin/python

import os
import pdfrw


class FillPDF:

    def __init__(self, input_pdf_path, output_pdf_path, data):
        self.input = input_pdf_path
        self.output = output_pdf_path
        self.data = data

    def write_fillable_pdf(self):
        template_pdf = pdfrw.PdfReader(self.input)
        annotations = template_pdf.pages[0]['/Annots']
        for annotation in annotations:
            if annotation['/Subtype'] == '/Widget':
                if annotation['/T']:
                    key = annotation['/T'][1:-1]
                    if key in data.keys():
                        annotation.update(
                            pdfrw.PdfDict(V='{}'.format(self.data[key]))
                        )
        pdfrw.PdfWriter().write(self.output, template_pdf)


data = {
    'full_name': "Dung"
}
input = "transcript_form.pdf"
output = "transcript_fill_pdf.pdf"
if __name__ == '__main__':
    x = FillPDF(input, output, data)
    x.write_fillable_pdf()