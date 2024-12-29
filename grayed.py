def read_bmp(file_path):
    with open(file_path, 'rb') as f:
        data = f.read()
    return bytearray(data)

def write_bmp(file_path, data):
    with open(file_path, 'wb') as f:
        f.write(data)

def convert_to_grayscale(input_path, output_path_gray):
    data = read_bmp(input_path)
    
    # Extrair cabeçalho (primeiros 54 bytes para BMPs padrão)
    header = data[:54]
    
    # P(offset nos bytes 10-13)
    pixel_array_offset = int.from_bytes(header[10:14], 'little')
    width = int.from_bytes(header[18:22], 'little')
    height = int.from_bytes(header[22:26], 'little')
    pixels = data[pixel_array_offset:]
    
    # Array para a nova imagem em tons de cinza
    grayscale_pixels = bytearray(pixels)
    
    # Conversão para níveis de cinza
    for i in range(0, len(pixels), 3):  # BMP usa formato BGR
        b, g, r = pixels[i], pixels[i+1], pixels[i+2]
        # Converter para cinza
        gray = int(0.3 * r + 0.59 * g + 0.11 * b)
        grayscale_pixels[i:i+3] = [gray, gray, gray]  # Substituir RGB pelo nível de cinza
    
    # Salvar 
    write_bmp(output_path_gray, header + grayscale_pixels)

# Exemplo de uso
convert_to_grayscale(
   r"C:\Users\WIN11\Downloads\dog-imagem.bmp", 
    r"C:\\Users\\WIN11\\Downloads\\dog_image_gray.bmp"
)
