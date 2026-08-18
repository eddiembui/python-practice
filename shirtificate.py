from fpdf import FPDF


class PDF(FPDF):
  def header(self):
    self.set_font("Helvetica", style="B", size=25)
    self.text(74, 40,"CS50 Shirtificate")

pdf = PDF()

def main():
  user_name = input("Name: ")
  pdf.add_page()
  pdf.set_font("Helvetica", style="B",size=15)
  pdf.set_text_color(255)
  pdf.image("shirtificate.png", 50, 70, 120)
  pdf.text(79, 120, f"{user_name} took CS50")

  pdf.output("shirtificate.pdf")

if __name__ == "__main__":
  main()