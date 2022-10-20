# pdf_watermarker.py

from pathlib import Path
from typing import Union, Literal, List
from PyPDF2 import PdfWriter, PdfReader



def create_watermark(input_pdf: Path, watermark: Path, output: Path) -> None:
    watermark_obj = PdfReader(watermark)
    watermark_page = watermark_obj.getPage(0)

    pdf_reader = PdfReader(input_pdf)
    pdf_writer = PdfWriter()

    # Watermark all the pages
    for page in range(pdf_reader.getNumPages()):
        page = pdf_reader.getPage(page)
        page.mergePage(watermark_page)
        pdf_writer.addPage(page)

    with open(output, 'wb') as out:
        pdf_writer.write(out)


def create_stamp(
    input_pdf: Path,
    stamp: Path,
    output: Path,
    page_indices: Union[Literal["ALL"], List[int]] = "ALL",
):
    reader = PdfReader(stamp)
    image_page = reader.pages[0]

    writer = PdfWriter()

    reader = PdfReader(input_pdf)
    if page_indices == "ALL":
        page_indices = list(range(0, len(reader.pages)))
    for index in page_indices:
        content_page = reader.pages[index]
        mediabox = content_page.mediabox
        content_page.merge_page(image_page)
        content_page.mediabox = mediabox
        writer.add_page(content_page)

    with open(output, "wb") as fp:
        writer.write(fp)


"""

Notes: 

I could not get my nor your function to work with your provided watermark. 
I believe you are right, it was the pdf not your code. 

I added two types of watermarks, one that will go over the text and one under. 
The under the text is a watermark made in LibreWriter and the over text version
is a text box also from LibreWriter. I included gifs on how I made these files. 

LibreWriter is freeSoftware that runs on windows, mac and linux

Watermarks: watermark2.pdf, libreoffice-watermark.pdf, libreoffice-textbox.pdf

"""

# TODO: create gifs that ilustrate the work being done
if __name__ == '__main__':

    create_watermark_output = 'watermarked-sample.pdf'
    create_watermark(
        input_pdf='ExamplePDF.pdf',
        watermark='libreoffice-textbox.pdf',
        output=create_watermark_output,
    )
    print(f"watermark process complete! output: {create_watermark_output}")

    create_stamp_output = 'stamped-sample.pdf'
    create_stamp(
        input_pdf='ExamplePDF.pdf',
        stamp='libreoffice-watermark.pdf',
        output=create_stamp_output,
        page_indices="ALL"
    )
    print(f"watermark process complete! output: {create_stamp_output}")
