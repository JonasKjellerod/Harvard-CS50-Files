from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 16)
        self.cell(0, 10, "CS50 Shirtificate", 0, 1, "C")

    def add_shirtificate(self, name):
        self.add_page()
        self.image("shirtificate.png", x=35, y=60, w=140)
        self.set_y(150)
        self.set_font("Arial", "B", 24)
        self.set_text_color(255, 255, 255)
        self.cell(0, 10, name, 0, 1, "C")

def main():
    name = input("Enter your name: ")
    pdf = PDF(orientation="P", format="A4")
    pdf.add_shirtificate(name)
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
