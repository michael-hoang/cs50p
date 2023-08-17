from fpdf import Align, FPDF


class ShirtificatePrinter(FPDF):
    """Class representation of Shirtificate (Shirt Certificate) printer."""

    def __init__(self, orientation="P", unit="mm", format="A4"):
        super().__init__(orientation=orientation, unit=unit, format=format)

    def load_shirt_img(self, shirt_img_path: str):
        """Render shirt image to ShirtificatePrinter."""
        self.add_page()
        self.image(shirt_img_path, h=self.eph / 1.4, x=Align.C, y=self.eph * 0.25)

    def export_shirtificate(self, output_path: str = "./shirtificate.pdf"):
        """Export Shirtificate to PDF file."""
        self.output(output_path)

    def add_text(
        self,
        text: str,
        font: tuple = ("helvetica", "", 14),
        color: tuple = (0, 0, 0),
        align: str = "C",
        text_box_h: float = None,
    ):
        """
        Add text to shirtificate.

        text: string,
        font: (font_family, font_style, font_size),
        color: tuple, default: (0, 0, 0)
        align: L, C (default), X, R
        text_box_h: float, default: self.eph (100% page height)

        """
        self.set_font(font[0], font[1], font[2])
        if not text_box_h:
            text_box_h = self.eph
        self.set_text_color(color[0], color[1], color[2])
        self.cell(txt=text, align=align, new_x="LEFT", new_y="NEXT", h=text_box_h, w=0)


if __name__ == "__main__":
    name = input("Name: ")
    sp = ShirtificatePrinter()
    sp.load_shirt_img("./shirtificate.png")
    sp.add_text(
        text="CS50 Shirtificate", font=("helvetica", "", 50), text_box_h=sp.eph * 0.2
    )
    sp.add_text(
        text=f"{name.title()} took CS50",
        font=("helvetica", "", 40),
        color=(255, 255, 255),
        text_box_h=sp.eph * 0.55,
    )
    sp.export_shirtificate()
