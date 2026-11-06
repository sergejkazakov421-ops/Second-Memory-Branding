from PIL import Image, ImageDraw, ImageFilter, ImageFont
import math
import random

def draw_symbol(draw, sym_type, x, y, size, color):
    if sym_type == 'question':
        draw.text((x, y), "?", fill=color, font=ImageFont.load_default())
    elif sym_type == 'exclamation':
        draw.text((x, y), "!", fill=color, font=ImageFont.load_default())
    elif sym_type == 'plus':
        draw.line([(x-size, y), (x+size, y)], fill=color, width=2)
        draw.line([(x, y-size), (x, y+size)], fill=color, width=2)
    elif sym_type == 'infinity':
        draw.text((x, y), "∞", fill=color, font=ImageFont.load_default())
    elif sym_type == 'at':
        draw.text((x, y), "@", fill=color, font=ImageFont.load_default())
    elif sym_type == 'eye':
        draw.ellipse([(x-size, y-size/2), (x+size, y+size/2)], outline=color, width=2)
        draw.ellipse([(x-size/3, y-size/3), (x+size/3, y+size/3)], fill=color)
    elif sym_type == 'dot':
        draw.ellipse([(x-size, y-size), (x+size, y+size)], fill=color)

def draw_chaotic_line(draw, x1, y1, x2, y2, color, width):
    """Рисует ломаную, хаотичную линию (как нейронную связь)"""
    dist = math.hypot(x2-x1, y2-y1)
    steps = int(dist / 15)
    if steps < 2: steps = 2
    
    points = [(x1, y1)]
    for i in range(1, steps):
        t = i / steps
        # Базовая точка на прямой
        bx = x1 + (x2 - x1) * t
        by = y1 + (y2 - y1) * t
        # Добавляем случайное отклонение (хаос)
        jitter_x = random.uniform(-20, 20)
        jitter_y = random.uniform(-20, 20)
        points.append((bx + jitter_x, by + jitter_y))
    points.append((x2, y2))
    
    # Рисуем сегменты
    for i in range(len(points) - 1):
        # Пунктирность
        if random.random() > 0.3:
            draw.line([points[i], points[i+1]], fill=color, width=width)
            # Иногда добавляем символы на линию
            if random.random() > 0.7:
                draw_symbol(draw, random.choice(['question', 'plus', 'dot']), points[i][0], points[i][1], random.randint(2,4), color)

def draw_icon(draw, icon_type, x, y, color):
    if icon_type == 'pin':
        draw.ellipse([(x - 6, y - 10), (x + 6, y + 2)], outline=color, width=2)
        draw.polygon([(x - 3, y - 2), (x + 3, y - 2), (x, y + 8)], fill=color)
    elif icon_type == 'clock':
        draw.ellipse([(x - 9, y - 9), (x + 9, y + 9)], outline=color, width=2)
        draw.line([(x, y), (x, y - 5)], fill=color, width=2)
        draw.line([(x, y), (x + 4, y + 2)], fill=color, width=2)
    elif icon_type == 'note':
        draw.rectangle([(x - 7, y - 9), (x + 7, y + 9)], outline=color, width=2)
        draw.line([(x - 3, y - 3), (x + 3, y - 3)], fill=color, width=2)
        draw.line([(x - 3, y + 2), (x + 3, y + 2)], fill=color, width=2)
    elif icon_type == 'mic':
        draw.rounded_rectangle([(x - 4, y - 8), (x + 4, y + 2)], radius=4, outline=color, width=2)
        draw.arc([(x - 8, y - 4), (x + 8, y + 8)], start=0, end=180, fill=color, width=2)
        draw.line([(x, y + 8), (x, y + 12)], fill=color, width=2)
    elif icon_type == 'folder':
        draw.rectangle([(x - 9, y - 6), (x + 9, y + 8)], outline=color, width=2)
        draw.line([(x - 9, y - 6), (x - 4, y - 10), (x + 2, y - 10), (x + 4, y - 6)], fill=color, width=2)
    elif icon_type == 'bell':
        draw.arc([(x - 8, y - 8), (x + 8, y + 8)], start=180, end=0, fill=color, width=2)
        draw.line([(x - 8, y), (x - 10, y + 5), (x + 10, y + 5), (x + 8, y)], fill=color, width=2)
        draw.ellipse([(x - 2, y + 6), (x + 2, y + 10)], fill=color)
    elif icon_type == 'gear':
        draw.ellipse([(x - 6, y - 6), (x + 6, y + 6)], outline=color, width=2)
        draw.ellipse([(x - 2, y - 2), (x + 2, y + 2)], fill=color)
        for angle in range(0, 360, 45):
            rad = math.radians(angle)
            draw.line([(x + 6*math.cos(rad), y + 6*math.sin(rad)), (x + 9*math.cos(rad), y + 9*math.sin(rad))], fill=color, width=2)
    elif icon_type == 'cloud':
        draw.ellipse([(x - 8, y - 4), (x + 2, y + 6)], outline=color, width=2)
        draw.ellipse([(x - 2, y - 8), (x + 8, y + 6)], outline=color, width=2)
    elif icon_type == 'lock':
        draw.rectangle([(x - 8, y - 2), (x + 8, y + 9)], outline=color, width=2)
        draw.arc([(x - 5, y - 8), (x + 5, y + 2)], start=0, end=180, fill=color, width=2)
    elif icon_type == 'heart':
        draw.pieslice([(x - 8, y - 6), (x, y + 2)], 180, 0, fill=color)
        draw.pieslice([(x, y - 6), (x + 8, y + 2)], 180, 0, fill=color)
        draw.polygon([(x - 8, y - 2), (x + 8, y - 2), (x, y + 9)], fill=color)
    elif icon_type == 'star':
        points = []
        for i in range(10):
            angle = math.radians(i * 36 - 90)
            r_curr = 9 if i % 2 == 0 else 4
            points.append((x + r_curr * math.cos(angle), y + r_curr * math.sin(angle)))
        draw.polygon(points, fill=color)


def create_chaos_brain():
    print("Создаем холст...")
    width, height = 1200, 900
    img = Image.new('RGB', (width, height), '#F8FAFC')
    draw = ImageDraw.Draw(img)

    cx, cy = width // 2, height // 2 - 30

    # 1. ГЕНЕРАЦИЯ МОЗГА (Форма по вашему контуру + Мозжечок)
    print("Генерируем мозг, мозжечок и рыхлость...")
    
    brain_layer = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    brain_draw = ImageDraw.Draw(brain_layer)

    brain_points = []
    cerebellum_points = []

    # Генерируем частицы
    for _ in range(25000):
        x = cx + random.uniform(-250, 250)
        y = cy + random.uniform(-220, 250)
        
        # 1. Полушария (вытянутые овалы)
        in_left = ((x - (cx - 65)) / 120)**2 + ((y - cy) / 175)**2 < 1
        in_right = ((x - (cx + 65)) / 120)**2 + ((y - cy) / 175)**2 < 1
        
        # Вырезаем низ полушарий, чтобы освободить место для мозжечка
        if (in_left or in_right) and y > cy + 110 and abs(x - cx) < 70:
            in_left = False
            in_right = False

        # 2. Мозжечок (внизу по центру, между полушариями)
        in_cerebellum = ((x - cx) / 75)**2 + ((y - (cy + 150)) / 50)**2 < 1

        if in_left or in_right or in_cerebellum:
            
            # Борозда по центру (делаем шире и глубже)
            if not in_cerebellum and abs(x - cx) < 20:
                if random.random() > 0.1: # Оставляем только 10% точек для связей
                    continue
            
            # РЫХЛОСТЬ: Отбрасываем много точек на краях
            edge_factor = random.random()
            is_edge = False
            if in_left and ((x - (cx - 65)) / 120)**2 + ((y - cy) / 175)**2 > 0.7: is_edge = True
            if in_right and ((x - (cx + 65)) / 120)**2 + ((y - cy) / 175)**2 > 0.7: is_edge = True
            if in_cerebellum and ((x - cx) / 75)**2 + ((y - (cy + 150)) / 50)**2 > 0.7: is_edge = True
            
            # Увеличиваем разброс (60% точек на краю разлетаются)
            if is_edge and edge_factor > 0.4: 
                r = random.randint(1, 3)
                alpha = random.randint(20, 80)
            else:
                r = random.randint(2, 5)
                alpha = random.randint(100, 255)

            # ЦВЕТА
            if in_cerebellum:
                # Ядерно-салатовый (кислотный зеленый)
                color = (57, 255, 20, alpha) 
                cerebellum_points.append((x, y))
            else:
                # Синий + Белый (искры)
                if random.random() > 0.85:
                    color = (255, 255, 255, alpha)
                else:
                    color = (random.randint(20, 80), random.randint(150, 220), 255, alpha)
                brain_points.append((x, y))
            
            # Сдвиг для хаоса
            px = x + random.uniform(-8, 8)
            py = y + random.uniform(-8, 8)
            
            brain_draw.ellipse([(px-r, py-r), (px+r, py+r)], fill=color)

    # Четкая разделительная линия (пустота по центру)
    # Можно добавить тонкую пунктирную линию, чтобы подчеркнуть разрез
    
    brain_layer_blurred = brain_layer.filter(ImageFilter.GaussianBlur(radius=2))
    
    # 2. ЦЕНТРАЛЬНЫЙ ЧИП (Увеличенный)
    print("Рисуем увеличенный чип...")
    chip_size = 60 # Увеличили с 45
    chip_layer = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    chip_draw = ImageDraw.Draw(chip_layer)
    
    chip_draw.rectangle([(cx - chip_size, cy - chip_size), (cx + chip_size, cy + chip_size)], fill=(15, 23, 42, 255), outline=(56, 189, 248, 255), width=5)
    for angle in range(0, 360, 45):
        rad = math.radians(angle)
        end_x = cx + (chip_size + 60) * math.cos(rad)
        end_y = cy + (chip_size + 60) * math.sin(rad)
        chip_draw.line([(cx, cy), (end_x, end_y)], fill=(56, 189, 248, 255), width=4)
        chip_draw.ellipse([(end_x-5, end_y-5), (end_x+5, end_y+5)], fill=(14, 165, 233, 255))
    chip_draw.rectangle([(cx - 25, cy - 25), (cx + 25, cy + 25)], fill=(56, 189, 248, 255))

    img.paste(brain_layer_blurred, (0, 0), brain_layer_blurred)
    img.paste(chip_layer, (0, 0), chip_layer)

    # 3. ИКОНКИ И ХАОТИЧНЫЕ СВЯЗИ
    print("Создаем хаотичную паутину связей...")
    
    nodes = [
        (cx - 350, cy - 200, 45, 'circle', 'folder'),
        (cx - 480, cy + 50, 35, 'diamond', 'note'),
        (cx - 300, cy + 280, 50, 'square', 'bell'),
        (cx + 180, cy - 320, 40, 'circle', 'heart'),
        (cx + 400, cy - 180, 55, 'diamond', 'star'),
        (cx + 450, cy + 150, 45, 'square', 'pin'),
        (cx + 300, cy + 350, 50, 'circle', 'clock'),
        (cx - 80, cy + 400, 35, 'diamond', 'mic'),
        (cx - 500, cy - 100, 30, 'square', 'cloud'),
        (cx + 550, cy - 50, 30, 'circle', 'lock'),
        (cx + 150, cy + 450, 25, 'diamond', 'gear')
    ]

    colors = ["#FCE7F3", "#FEF3C7", "#DCFCE7", "#E0F2FE", "#F3E8FF", "#FFE4E6", "#CCFBF1", "#FEE2E2", "#E0F2FE", "#FEF3C7", "#FCE7F3"]
    icon_color = "#1E293B"

    # Рисуем хаотичные связи
    # 1. От чипа к мозгу (много хаоса)
    for _ in range(150):
        target_list = cerebellum_points if random.random() > 0.7 else brain_points
        target_x, target_y = random.choice(target_list)
        draw_chaotic_line(draw, cx, cy, target_x, target_y, (56, 189, 248, 120), 1)

    # 2. Между иконками и мозгом/друг другом
    for i, (nx, ny, r, shape, icon) in enumerate(nodes):
        
        # Связь с мозгом
        target_list = cerebellum_points if random.random() > 0.8 else brain_points
        target_x, target_y = random.choice(target_list)
        draw_chaotic_line(draw, nx, ny, target_x, target_y, "#94A3B8", 2)

        # Связи с другими иконками (паутина)
        for j, (mx, my, mr, mshape, micon) in enumerate(nodes):
            if i != j:
                dist_nodes = math.hypot(nx - mx, ny - my)
                if dist_nodes < 350: # Увеличили радиус связей
                    draw_chaotic_line(draw, nx, ny, mx, my, "#CBD5E1", 2)


    # 4. СИМВОЛЫ В САМОМ МОЗГЕ (Беспорядочно)
    for _ in range(100):
        p = random.choice(brain_points + cerebellum_points)
        sym_type = random.choice(['question', 'exclamation', 'plus', 'infinity', 'at', 'eye'])
        color = (57, 255, 20, 200) if p in cerebellum_points else (255, 255, 255, 200)
        draw_symbol(draw, sym_type, p[0], p[1], random.randint(3, 7), color)


    # 5. РИСУЕМ САМИ ФИГУРЫ ИКОНОК
    for i, (nx, ny, r, shape, icon) in enumerate(nodes):
        color = colors[i]
        
        if shape == 'circle':
            draw.ellipse([(nx - r, ny - r), (nx + r, ny + r)], fill=color, outline="#94A3B8", width=2)
        elif shape == 'square':
            draw.rectangle([(nx - r, ny - r), (nx + r, ny + r)], fill=color, outline="#94A3B8", width=2)
        elif shape == 'diamond':
            points = [(nx, ny - r), (nx + r, ny), (nx, ny + r), (nx - r, ny)]
            draw.polygon(points, fill=color, outline="#94A3B8")
        
        draw_icon(draw, icon, nx, ny, icon_color)

    output_file = "Chaos_Brain_SecondMemory.png"
    img.save(output_file, quality=100)
    print(f"ГОТОВО! Файл сохранен как {output_file}")

if __name__ == "__main__":
    create_chaos_brain()
