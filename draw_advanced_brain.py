from PIL import Image, ImageDraw, ImageFilter
import math
import random

def draw_icon(draw, icon_type, x, y, r, color):
    """Функция для рисования разных иконок"""
    if icon_type == 'pin':
        draw.ellipse([(x - 10, y - 15), (x + 10, y + 5)], outline=color, width=3)
        draw.polygon([(x - 5, y), (x + 5, y), (x, y + 15)], fill=color)
    elif icon_type == 'clock':
        draw.ellipse([(x - 15, y - 15), (x + 15, y + 15)], outline=color, width=3)
        draw.line([(x, y), (x, y - 10)], fill=color, width=3)
        draw.line([(x, y), (x + 8, y + 5)], fill=color, width=3)
    elif icon_type == 'note':
        draw.rectangle([(x - 12, y - 15), (x + 12, y + 15)], outline=color, width=3)
        draw.line([(x - 6, y - 5), (x + 6, y - 5)], fill=color, width=2)
        draw.line([(x - 6, y + 2), (x + 6, y + 2)], fill=color, width=2)
    elif icon_type == 'mic':
        draw.rounded_rectangle([(x - 6, y - 12), (x + 6, y + 4)], radius=6, outline=color, width=3)
        draw.arc([(x - 12, y - 6), (x + 12, y + 12)], start=0, end=180, fill=color, width=3)
        draw.line([(x, y + 12), (x, y + 18)], fill=color, width=3)
    elif icon_type == 'folder':
        draw.rectangle([(x - 14, y - 10), (x + 14, y + 12)], outline=color, width=3)
        draw.line([(x - 14, y - 10), (x - 6, y - 16), (x + 2, y - 16), (x + 6, y - 10)], fill=color, width=3)
    elif icon_type == 'bell':
        draw.arc([(x - 12, y - 12), (x + 12, y + 12)], start=180, end=0, fill=color, width=3)
        draw.line([(x - 12, y), (x - 15, y + 8), (x + 15, y + 8), (x + 12, y)], fill=color, width=3)
        draw.ellipse([(x - 4, y + 10), (x + 4, y + 16)], fill=color)
    elif icon_type == 'gear':
        draw.ellipse([(x - 10, y - 10), (x + 10, y + 10)], outline=color, width=3)
        draw.ellipse([(x - 4, y - 4), (x + 4, y + 4)], fill=color)
        for angle in range(0, 360, 45):
            rad = math.radians(angle)
            x1 = x + 12 * math.cos(rad)
            y1 = y + 12 * math.sin(rad)
            draw.ellipse([(x1-3, y1-3), (x1+3, y1+3)], fill=color)
    elif icon_type == 'cloud':
        draw.ellipse([(x - 12, y - 8), (x + 4, y + 8)], outline=color, width=3)
        draw.ellipse([(x - 4, y - 12), (x + 12, y + 8)], outline=color, width=3)
    elif icon_type == 'lock':
        draw.rectangle([(x - 12, y - 4), (x + 12, y + 14)], outline=color, width=3)
        draw.arc([(x - 8, y - 14), (x + 8, y + 4)], start=0, end=180, fill=color, width=3)
    elif icon_type == 'heart':
        draw.pieslice([(x - 12, y - 10), (x, y + 2)], 180, 0, fill=color)
        draw.pieslice([(x, y - 10), (x + 12, y + 2)], 180, 0, fill=color)
        draw.polygon([(x - 12, y - 4), (x + 12, y - 4), (x, y + 15)], fill=color)
    elif icon_type == 'star':
        points = []
        for i in range(10):
            angle = math.radians(i * 36 - 90)
            r_inner = 6
            r_outer = 14
            r_curr = r_outer if i % 2 == 0 else r_inner
            points.append((x + r_curr * math.cos(angle), y + r_curr * math.sin(angle)))
        draw.polygon(points, fill=color)


def create_advanced_brain():
    print("Создаем холст...")
    width, height = 1200, 900
    img = Image.new('RGB', (width, height), '#F8FAFC')
    draw = ImageDraw.Draw(img)

    cx, cy = width // 2, height // 2

    # 1. ГЕНЕРАЦИЯ ТОЧЕК МОЗГА (Два полушария)
    print("Генерируем нейроны...")
    points = []
    
    # Левое полушарие
    for _ in range(800):
        angle = random.uniform(0, math.pi * 2)
        radius = random.uniform(30, 160)
        x = cx - 40 + radius * math.cos(angle) * 0.9
        y = cy + radius * math.sin(angle) * 1.1
        if (x - (cx - 40))**2 / 150**2 + (y - cy)**2 / 190**2 < 1:
            points.append((x, y))
            
    # Правое полушарие
    for _ in range(800):
        angle = random.uniform(0, math.pi * 2)
        radius = random.uniform(30, 160)
        x = cx + 40 + radius * math.cos(angle) * 0.9
        y = cy + radius * math.sin(angle) * 1.1
        if (x - (cx + 40))**2 / 150**2 + (y - cy)**2 / 190**2 < 1:
            points.append((x, y))

    # 2. СЛОЙ ДЛЯ СВЕЧЕНИЯ
    glow_layer = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    glow_draw = ImageDraw.Draw(glow_layer)

    # 3. РИСУЕМ НЕЙРОННЫЕ СВЯЗИ (Ближайшие соседи)
    print("Создаем связи...")
    for i, p1 in enumerate(points):
        # Находим ближайших соседей для текущей точки
        distances = []
        for j, p2 in enumerate(points):
            if i != j:
                dist = math.hypot(p1[0] - p2[0], p1[1] - p2[1])
                if dist < 40: # Максимальная длина связи
                    distances.append((dist, j))
        
        # Сортируем по расстоянию и берем 2-3 ближайших
        distances.sort()
        for dist, j in distances[:2]:
            p2 = points[j]
            # Чем короче линия, тем она ярче
            alpha = int(255 - (dist * 4))
            if alpha > 0:
                glow_draw.line([p1, p2], fill=(56, 189, 248, alpha), width=2)

    # Рисуем сами нейроны (точки)
    for p in points:
        r = random.randint(2, 4)
        glow_draw.ellipse([(p[0]-r, p[1]-r), (p[0]+r, p[1]+r)], fill=(14, 165, 233, 255))

    # 4. ЦЕНТРАЛЬНЫЙ ЧИП
    chip_size = 50
    glow_draw.rectangle([(cx - chip_size, cy - chip_size), (cx + chip_size, cy + chip_size)], fill=(15, 23, 42, 255), outline=(56, 189, 248, 255), width=4)
    
    # Дорожки от чипа
    for angle in range(0, 360, 45):
        rad = math.radians(angle)
        end_x = cx + (chip_size + 60) * math.cos(rad)
        end_y = cy + (chip_size + 60) * math.sin(rad)
        glow_draw.line([(cx, cy), (end_x, end_y)], fill=(56, 189, 248, 180), width=3)
        glow_draw.ellipse([(end_x-5, end_y-5), (end_x+5, end_y+5)], fill=(14, 165, 233, 255))
    
    # Внутренний чип
    glow_draw.rectangle([(cx - 20, cy - 20), (cx + 20, cy + 20)], fill=(56, 189, 248, 255))

    # Накладываем свечение
    glow_layer_blurred = glow_layer.filter(ImageFilter.GaussianBlur(radius=5))
    img.paste(glow_layer_blurred, (0, 0), glow_layer_blurred)
    img.paste(glow_layer, (0, 0), glow_layer)


    # 5. РИСУЕМ ОБЛАЧКА И ИКОНКИ (11 штук)
    print("Рисуем иконки...")
    nodes = []
    num_nodes = 11
    for i in range(num_nodes):
        # Распределяем по кругу с небольшим случайным отклонением
        angle = (i / num_nodes) * math.pi * 2
        dist = random.uniform(280, 350)
        nx = cx + dist * math.cos(angle)
        ny = cy + dist * math.sin(angle)
        r = random.randint(35, 50)
        nodes.append((nx, ny, r))

    colors = ["#E0F2FE", "#FCE7F3", "#FEF3C7", "#DCFCE7", "#F3E8FF", "#E0E7FF", "#FFE4E6", "#CCFBF1", "#FEE2E2", "#E0F2FE", "#FEF3C7"]
    icon_types = ['pin', 'clock', 'note', 'mic', 'folder', 'bell', 'gear', 'cloud', 'lock', 'heart', 'star']
    icon_color = "#1E293B" # Темно-серый

    for i, (nx, ny, r) in enumerate(nodes):
        # Облачко
        draw.ellipse([(nx - r, ny - r), (nx + r, ny + r)], fill=colors[i], outline="#94A3B8", width=2)
        
        # Иконка
        draw_icon(draw, icon_types[i], nx, ny, r, icon_color)

        # Линия от мозга к облачку (пунктир)
        # Вычисляем точку на краю мозга и на краю облачка
        angle_to_center = math.atan2(cy - ny, cx - nx)
        start_x = nx + (r + 10) * math.cos(angle_to_center)
        start_y = ny + (r + 10) * math.sin(angle_to_center)
        
        end_x = cx - 160 * math.cos(angle_to_center)
        end_y = cy - 190 * math.sin(angle_to_center)
        
        length = math.hypot(end_x - start_x, end_y - start_y)
        steps = int(length / 15)
        for step in range(steps):
            if step % 2 == 0:
                x1 = start_x + (end_x - start_x) * (step / steps)
                y1 = start_y + (end_y - start_y) * (step / steps)
                x2 = start_x + (end_x - start_x) * ((step + 0.5) / steps)
                y2 = start_y + (end_y - start_y) * ((step + 0.5) / steps)
                draw.line([(x1, y1), (x2, y2)], fill="#94A3B8", width=3)


    output_file = "Advanced_Brain_SecondMemory.png"
    img.save(output_file, quality=100)
    print(f"ГОТОВО! Файл сохранен как {output_file}")

if __name__ == "__main__":
    create_advanced_brain()
