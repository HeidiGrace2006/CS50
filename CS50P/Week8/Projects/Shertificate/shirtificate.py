from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("helvetica", "B", 40)
        #ln for moving y, cell for moving x
        self.ln(15)
        self.cell(35)
        self.cell(125, 30, "CS50 Shertificate", border=1, align="C")

    def footer(self):
        #                                                                                        x    y   w    h
        self.image("https://cs50.harvard.edu/python/2022/psets/8/shirtificate/shirtificate.png", 17, 80, 175, 170)
        self.set_font("Courier", "", 37)
        self.set_text_color(255,255,255)
        self.cell(-130, 235, f"{name} took CS50", border=0, align="C")

pdf = PDF()
pdf.add_page()
name = input("Name: ")
pdf.output("shirtificate.pdf")

#Below is just the tutorial code for reference
'''
pdf = FPDF()
pdf.add_page()
pdf.set_font('helvetica', size=12)
pdf.cell(text="hello world")
pdf.output("hello_world.pdf")

#######################################

class PDF(FPDF):
    def header(self):
        # Rendering logo:
        self.image("../docs/fpdf2-logo.png", 10, 8, 33)
        # Setting font: helvetica bold 15
        self.set_font("helvetica", "B", 15)
        # Moving cursor to the right:
        self.cell(80)
        # Printing title:
        self.cell(30, 10, "Title", border=1, align="C")
        # Performing a line break:
        self.ln(20)

    def footer(self):
        # Position cursor at 1.5 cm from bottom:
        self.set_y(-15)
        # Setting font: helvetica italic 8
        self.set_font("helvetica", "I", 8)
        # Printing page number:
        self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="C")


# Instantiation of inherited class
pdf = PDF()
pdf.add_page()
pdf.set_font("Times", size=12)
for i in range(1, 41):
    pdf.cell(0, 10, f"Printing line number {i}", new_x="LMARGIN", new_y="NEXT")
pdf.output("new-tuto2.pdf")
'''