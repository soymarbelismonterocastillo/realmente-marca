import base64

with open(r'c:\Users\soyma\OneDrive\Documents\ANTIGRAVITY\MARCA\mesa_metafora_culpa.png', 'rb') as f:
    b64 = base64.b64encode(f.read()).decode('utf-8')
data_uri = f'data:image/png;base64,{b64}'

html_path1 = r'c:\Users\soyma\OneDrive\Documents\ANTIGRAVITY\MARCA\presentacion_episodio_62.html'
html_path2 = r'c:\Users\soyma\OneDrive\Documents\ANTIGRAVITY\MARCA\Episodios\EP62_La_Trampa_de_la_Culpa\04_Club_Ejercicio_y_Diapositivas\presentacion_episodio_62.html'

for path in [html_path1, html_path2]:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    content_new = content.replace('src="mesa_metafora_culpa.png"', f'src="{data_uri}"')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content_new)

print('Successfully embedded Base64 image into both HTML files!')
