import PyPDF4
from PyPDF4 import PdfFileReader, PdfFileWriter

PyPDF4.PdfFileReader("ExamplePDF.pdf")


def create_watermark(input_pdf, output_pdf, watermark_pdf):
    watermark = PdfFileReader(watermark_pdf)
    page_watermark = watermark.getPage(0)
    input_pdf_reader = PdfFileReader(input_pdf)
    output_pdf_writer = PdfFileWriter()
    for page in range(input_pdf_reader.getNumPages()):
        page = input_pdf_reader.getPage(page)
        page.mergePage(page_watermark)
        output_pdf_writer.addPage(page)
    with open(output_pdf, "wb") as output:
        output_pdf_writer.write(output)


if __name__ == '__main__':
    create_watermark(
        input_pdf='ExamplePDF.pdf',
        output_pdf='watermarked-sample.pdf',
        watermark_pdf='WatermarkOverlay.pdf'
    )
    print("watermark process complete!")
