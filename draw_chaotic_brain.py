from PIL import Image, ImageDraw, ImageFilter
import math
import random

def draw_icon(draw, icon_type, x, y, r, color):
    """Функция для рисования разных иконок"""
    if icon_type == 'pin':
        draw.ellipse([(x - 8, y - 12), (x + 8, y + 4)], outline=color, width=3)
        draw.polygon([(x - 4, y), (x + 4, y), (x, y + 12)], fill=color)
    elif icon_type == 'clock':
        draw.ellipse([(x - 12, y - 12), (x + 12, y + 12)], outline=color, width=3)
        draw.line([(x, y), (x, y - 8)], fill=color, width=3)
        draw.line([(x, y), (x + 6, y + 4)], fill=color, width=3)
    elif icon_type == 'note':
        draw.rectangle([(x - 10, y - 12), (x + 10, y + 12)], outline=color, width=3)
        draw.line([(x - 5, y - 4), (x + 5, y - 4)], fill=color, width=2)
        draw.line([(x - 5, y + 2), (x + 5, y + 2)], fill=color, width=2)
    elif icon_type == 'mic':
        draw.rounded_rectangle([(x - 5, y - 10), (x + 5, y + 3)], radius=5, outline=color, width=3)
        draw.arc([(x - 10, y - 5), (x + 10, y + 10)], start=0, end=180, fill=color, width=3)
        draw.line([(x, y + 10), (x, y + 15)], fill=color, width=3)
    elif icon_type == 'folder':
        draw.rectangle([(x - 12, y - 8), (x + 12, y + 10)], outline=color, width=3)
        draw.line([(x - 12, y - 8), (x - 5, y - 13), (x + 2, y - 13), (x + 5, y - 8)], fill=color, width=3)
    elif icon_type == 'bell':
        draw.arc([(x - 10, y - 10), (x + 10, y + 10)], start=180, end=0, fill=color, width=3)
        draw.line([(x - 10, y), (x - 12, y + 7), (x + 12, y + 7), (x + 10, y)], fill=color, width=3)
        draw.ellipse([(x - 3, y + 8), (x + 3, y + 13)], fill=color)
    elif icon_type == 'gear':
        draw.ellipse([(x - 8, y - 8), (x + 8, y + 8)], outline=color, width=3)
        draw.ellipse([(x - 3, y - 3), (x + 3, y + 3)], fill=color)
        for angle in range(0, 360, 45):
            rad = math.radians(angle)
            x1 = x + 10 * math.cos(rad)
            y1 = y + 10 * math.sin(rad)
            draw.ellipse([(x1-2, y1-2), (x1+2, y1+2)], fill=color)
    elif icon_type == 'cloud':
        draw.ellipse([(x - 10, y - 6), (x + 4, y + 6)], outline=color, width=3)
        draw.ellipse([(x - 4, y - 10), (x + 10, y + 6)], outline=color, width=3)
    elif icon_type == 'lock':
        draw.rectangle([(x - 10, y - 2), (x + 10, y + 12)], outline=color, width=3)
        draw.arc([(x - 6, y - 10), (x + 6, y + 2)], start=0, end=180, fill=color, width=3)
    elif icon_type == 'heart':
        draw.pieslice([(x - 10, y - 8), (x, y + 2)], 180, 0, fill=color)
        draw.pieslice([(x, y - 8), (x + 10, y + 2)], 180, 0, fill=color)
        draw.polygon([(x - 10, y - 3), (x + 10, y - 3), (x, y + 12)], fill=color)
    elif icon_type == 'star':
        points = []
        for i in range(10):
            angle = math.radians(i * 36 - 90)
            r_inner = 5
            r_outer = 11
            r_curr = r_outer if i % 2 == 0 else r_inner
            points.append((x + r_curr * math.cos(angle), y + r_curr * math.sin(angle)))
        draw.polygon(points, fill=color)


def create_chaotic_brain():
    print("Создаем холст...")
    width, height = 1200, 900
    img = Image.new('RGB', (width, height), '#F8FAFC')
    draw = ImageDraw.Draw(img)

    cx, cy = width // 2, height // 2

    # 1. ГЕНЕРАЦИЯ РЫХЛОГО, МЯГКОГО МОЗГА (КАК В 1 ВЕРСИИ)
    print("Генерируем мягкий мозг...")
    points = []
    
    # Создаем форму из двух вытянутых полушарий с помощью плотного облака точек
    for _ in range(2500):
        angle = random.uniform(0, math.pi * 2)
        # Используем нормальное распределение для создания плотного центра и рыхлых краев
        radius_x = random.gauss(160, 40) 
        radius_y = random.gauss(120, 30)
        
        side = random.choice([-1, 1]) # Левое или правое полушарие
        offset = side * random.uniform(20, 60) # Раздвигаем полушария

        x = cx + offset + radius_x * math.cos(angle)
        y = cy + radius_y * math.sin(angle)
        
        # Немного сплющиваем для анатомичности
        points.append((x, y))

    # Слой для свечения мозга
    glow_layer = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    glow_draw = ImageDraw.Draw(glow_layer)

    # Рисуем точки (нейроны) без жестких линий между ними
    for p in points:
        # Чем ближе к центру, тем больше и ярче точки
        dist_to_center = math.hypot(p[0] - cx, p[1] - cy)
        alpha = int(255 - (dist_to_center * 0.5))
        if alpha < 0: alpha = 0
        
        r = random.randint(2, 6)
        glow_draw.ellipse([(p[0]-r, p[1]-r), (p[0]+r, p[1]+r)], fill=(56, 189, 248, alpha))
        
        # Добавляем соединительные линии ТОЛЬКО внутри мозга для эффекта сети
        if random.random() > 0.7: # Не все точки соединяем
            for p2 in random.sample(points, 3):
                d = math.hypot(p[0]-p2[0], p[1]-p2[1])
                if d < 30:
                    glow_draw.line([p, p2], fill=(14, 165, 233, int(alpha*0.5)), width=1)

    # 2. ЦЕНТРАЛЬНЫЙ ЧИП
    print("Рисуем чип...")
    chip_size = 50
    glow_draw.rectangle([(cx - chip_size, cy - chip_size), (cx + chip_size, cy + chip_size)], fill=(15, 23, 42, 255), outline=(56, 189, 248, 255), width=4)
    
    for angle in range(0, 360, 45):
        rad = math.radians(angle)
        end_x = cx + (chip_size + 50) * math.cos(rad)
        end_y = cy + (chip_size + 50) * math.sin(rad)
        glow_draw.line([(cx, cy), (end_x, end_y)], fill=(56, 189, 248, 200), width=3)
        glow_draw.ellipse([(end_x-4, end_y-4), (end_x+4, end_y+4)], fill=(14, 165, 233, 255))
    
    glow_draw.rectangle([(cx - 20, cy - 20), (cx + 20, cy + 20)], fill=(56, 189, 248, 255))

    # Размываем и накладываем свечение
    glow_layer_blurred = glow_layer.filter(ImageFilter.GaussianBlur(radius=8))
    img.paste(glow_layer_blurred, (0, 0), glow_layer_blurred)
    
    # Накладываем четкий слой
    clear_layer = glow_layer.filter(ImageFilter.GaussianBlur(radius=1))
    img.paste(clear_layer, (0, 0), clear_layer)


    # 3. ХАОТИЧНО РАСПОЛАГАЕМ ИКОНКИ И РИСУЕМ СВЯЗИ
    print("Расставляем иконки (хаотично)...")
    
    # Координаты заданы вручную, чтобы повторить хаос с картинки-референса
    nodes = [
        # (X, Y, Радиус, Иконка, Родитель (к чему привязана линия: 'brain' или индекс другой иконки))
        (cx - 250, cy - 150, 45, 'folder', 'brain'),
        (cx - 350, cy + 50, 35, 'note', 'brain'),
        (cx - 200, cy + 250, 50, 'bell', 1), # Привязана к заметке
        (cx + 100, cy - 280, 40, 'heart', 'brain'),
        (cx + 300, cy - 150, 55, 'star', 'brain'),
        (cx + 350, cy + 100, 45, 'pin', 4), # Привязана к звезде
        (cx + 200, cy + 250, 50, 'clock', 'brain'),
        (cx - 100, cy + 300, 35, 'mic', 6), # Привязана к часам
        (cx - 400, cy - 100, 30, 'cloud', 0), # Привязана к папке
        (cx + 450, cy - 50, 30, 'lock', 4), # Привязана к звезде
        (cx, cy + 350, 25, 'gear', 7) # Привязана к микрофону
    ]

    colors = ["#FCE7F3", "#FEF3C7", "#DCFCE7", "#E0F2FE", "#F3E8FF", "#FFE4E6", "#CCFBF1", "#FEE2E2", "#E0F2FE", "#FEF3C7", "#FCE7F3"]
    icon_color = "#1E293B"

    # Сначала рисуем линии
    for i, (nx, ny, r, icon, parent) in enumerate(nodes):
        if parent == 'brain':
            # Линия от мозга
            # Вычисляем точку на краю облачка
            angle_to_center = math.atan2(cy - ny, cx - nx)
            start_x = nx + r * math.cos(angle_to_center)
            start_y = ny + r * math.sin(angle_to_center)
            
            # Вычисляем точку на краю мозга (примерно)
            end_x = cx + 150 * math.cos(angle_to_center)
            end_y = cy + 110 * math.sin(angle_to_center)
            
        else:
            # Линия от другой иконки
            px, py, pr, _, _ = nodes[parent]
            angle_to_parent = math.atan2(py - ny, px - nx)
            start_x = nx + r * math.cos(angle_to_parent)
            start_y = ny + r * math.sin(angle_to_parent)
            end_x = px + pr * math.cos(angle_to_parent + math.pi)
            end_y = py + pr * math.sin(angle_to_parent + math.pi)

        # Рисуем пунктир
        length = math.hypot(end_x - start_x, end_y - start_y)
        steps = int(length / 12)
        for step in range(steps):
            if step % 2 == 0:
                x1 = start_x + (end_x - start_x) * (step / steps)
                y1 = start_y + (end_y - start_y) * (step / steps)
                x2 = start_x + (end_x - start_x) * ((step + 0.8) / steps)
                y2 = start_y + (end_y - start_y) * ((step + 0.8) / steps)
                draw.line([(x1, y1), (x2, y2)], fill="#64748B", width=2)


    # Затем рисуем сами облачка и иконки, чтобы перекрыть концы линий
    for i, (nx, ny, r, icon, parent) in enumerate(nodes):
        draw.ellipse([(nx - r, ny - r), (nx + r, ny + r)], fill=colors[i], outline="#CBD5E1", width=2)
        draw_icon(draw, icon, nx, ny, r, icon_color)


    output_file = "Chaotic_Brain_SecondMemory.png"
    img.save(output_file, quality=100)
    print(f"ГОТОВО! Файл сохранен как {output_file}")

if __name__ == "__main__":
    create_chaotic_brain()
