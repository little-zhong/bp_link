import sys
import qrcode


def link2qr(link):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(link)
    qr.print_ascii(invert=True)


if __name__ == "__main__":
    args = sys.argv
    link2qr(args[1])
    # python3 link2qr.py link
