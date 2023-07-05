import os
import qrcode

def generate_qr_code(url):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    qr_code = qr.make_image(fill_color="black", back_color="white")
    return qr_code

def save_qr_code(qr_code, filename):
    output_dir = "out"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    file_path = os.path.join(output_dir, filename)
    qr_code.save(file_path)

    print(f"O código QR foi gerado e salvo como {file_path}.")

def main():
    url = input("Digite o URL que deseja codificar: ")
    filename = input("Digite o nome do arquivo de saída (com a extensão .png): ")

    qr_code = generate_qr_code(url)
    save_qr_code(qr_code, filename)

if __name__ == "__main__":
    main()