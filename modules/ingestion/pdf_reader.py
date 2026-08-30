import pymupdf


class PDFReader:
    
    def extract_text(self , pdf_path: str) -> str:
        """
        Extract all text from a PDF.
        """

        doc = pymupdf.open(pdf_path)

        text = ""

        for page in doc:
            
            text += page.get_text()

        doc.close()

        return text