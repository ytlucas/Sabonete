import re
import os

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Hero
content = content.replace('<img src="/fotoProfissional.png" alt="Profissional" class="hero-img">', '<img src="/fotoProfissional.png" alt="Profissional" class="hero-img" fetchpriority="high" decoding="async">')

# Bio
content = content.replace('<img src="/fotoProfissional.png" alt="Beatriz" class="bio-img">', '<img src="/fotoProfissional.png" alt="Beatriz" class="bio-img" loading="lazy" decoding="async">')

# Resultados
for i in range(1, 6):
    content = content.replace(f'<img src="/resultado{i}.jpg" alt="Resultado de Aluna" class="resultado-img">', f'<img src="/resultado{i}.jpg" alt="Resultado de Aluna" class="resultado-img" loading="lazy" decoding="async">')

# Testimonials
for i in range(1, 5):
    content = content.replace(f'<img src="/cliente{i}.png" alt="Cliente {i}" class="test-img">', f'<img src="/cliente{i}.png" alt="Cliente {i}" class="test-img" loading="lazy" decoding="async">')

# Provas Sociais (with styling)
content = re.sub(r'<img src="/prova(\d+)\.jpg" alt="([^"]+)" class="resultado-img"\s*\n?\s*style="([^"]+)">', r'<img src="/prova\1.jpg" alt="\2" class="resultado-img" style="\3" loading="lazy" decoding="async">', content)

# Notification avatar
content = content.replace('<img src="" id="sn-avatar" alt="Avatar">', '<img src="" id="sn-avatar" alt="Avatar" loading="lazy" decoding="async">')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
