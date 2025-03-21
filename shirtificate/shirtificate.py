from fpdf import FPDF


class Shirtify():

    def __init__(self):
        self.name = input('What\'s your name?: ') + ' took CS50'
        self._pdf = FPDF()
        self._pdf.add_page()
        self._pdf.set_font('Times', 'B', 60)
        self._pdf.cell(0, 60, 'CS50 Shirtificate', align='C', ln=1)
        self._pdf.image('shirtificate.png', w=self._pdf.w - 20)
        self._pdf.set_font_size(30)
        self._pdf.set_text_color(255, 255, 255)
        self._pdf.text(x=47.5, y=140, txt=f'{self.name}')

    def save(self, filename):
        self._pdf.output(filename)


def main():
    pdf = Shirtify()
    pdf.save('shirtificate.pdf')


if __name__ == "__main__":
    main()
