from PIL import Image, ImageDraw, ImageFilter, ImageFont
import math
import random

def draw_symbol(draw, sym_type, x, y, size, color):
    """Рисует маленькие символы (мысли)"""
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
    elif sym_type == 'star':
        points = []
        for i in range(10):
            angle = math.radians(i * 36 - 90)
            r_curr = size if i % 2 == 0 else size/2
            points.append((x + r_curr * math.cos(angle), y + r_curr * math.sin(angle)))
        draw.polygon(points, fill=color)
    elif sym_type == 'eye':
        draw.ellipse([(x-size, y-size/2), (x+size, y+size/2)], outline=color, width=2)
        draw.ellipse([(x-size/3, y-size/3), (x+size/3, y+size/3)], fill=color)
    elif sym_type == 'dot':
        draw.ellipse([(x-size, y-size), (x+size, y+size)], fill=color)

def draw_icon(draw, icon_type, x, y, color):
    """Функция для рисования основных иконок"""
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


def create_ultimate_brain():
    print("Создаем холст...")
    width, height = 1200, 900
    img = Image.new('RGB', (width, height), '#F8FAFC')
    draw = ImageDraw.Draw(img)

    cx, cy = width // 2, height // 2 - 30

    # 1. ГЕНЕРАЦИЯ МОЗГА (Строго по вашему контуру)
    print("Генерируем мозг с мозжечком и белыми искрами...")
    
    brain_layer = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    brain_draw = ImageDraw.Draw(brain_layer)

    # Массивы для точек, чтобы потом рисовать связи
    brain_points = []
    cerebellum_points = []

    # Генерируем очень много точек для плотности
    for _ in range(20000):
        x = cx + random.uniform(-250, 250)
        y = cy + random.uniform(-220, 250)
        
        # 1. Левое полушарие (смещено влево, вытянуто)
        in_left = ((x - (cx - 65)) / 125)**2 + ((y - cy) / 180)**2 < 1
        
        # 2. Правое полушарие (смещено вправо, вытянуто)
        in_right = ((x - (cx + 65)) / 125)**2 + ((y - cy) / 180)**2 < 1
        
        # 3. Мозжечок (внизу по центру, поменьше)
        in_cerebellum = ((x - cx) / 90)**2 + ((y - (cy + 160)) / 60)**2 < 1

        # Формируем форму
        if in_left or in_right or in_cerebellum:
            
            # Делаем четкую борозду по центру (между полушариями), но не трогаем мозжечок
            if not in_cerebellum and abs(x - cx) < 12:
                if random.random() > 0.15: # Оставляем 15% точек для "ниточек" связи
                    continue
            
            # ОЧЕНЬ РЫХЛЫЕ КРАЯ: если точка близко к границе, часто пропускаем
            edge_factor = random.random()
            is_edge = False
            if in_left and ((x - (cx - 65)) / 125)**2 + ((y - cy) / 180)**2 > 0.8: is_edge = True
            if in_right and ((x - (cx + 65)) / 125)**2 + ((y - cy) / 180)**2 > 0.8: is_edge = True
            if in_cerebellum and ((x - cx) / 90)**2 + ((y - (cy + 160)) / 60)**2 > 0.8: is_edge = True
            
            if is_edge and edge_factor > 0.3: # 70% точек на краю разлетаются
                # Если разлетается, делаем точку меньше и прозрачнее
                r = random.randint(1, 3)
                alpha = random.randint(30, 100)
            else:
                # Плотная внутренняя часть
                r = random.randint(2, 6)
                alpha = random.randint(120, 255)

            # Цвета: для мозга (Синий, Голубой, БЕЛЫЙ)
            if in_cerebellum:
                # Мозжечок: Неоново-розовый/малиновый
                color = (255, random.randint(50, 120), random.randint(150, 200), alpha)
                cerebellum_points.append((x, y))
            else:
                # Полушария: Синий + Белый (для искр)
                if random.random() > 0.8: # 20% точек белые (искры)
                    color = (255, 255, 255, alpha)
                else:
                    color = (random.randint(30, 100), random.randint(150, 220), 255, alpha)
                brain_points.append((x, y))
            
            # Слегка сдвигаем для хаоса
            px = x + random.uniform(-6, 6)
            py = y + random.uniform(-6, 6)
            
            brain_draw.ellipse([(px-r, py-r), (px+r, py+r)], fill=color)

    # Размываем мозг
    brain_layer_blurred = brain_layer.filter(ImageFilter.GaussianBlur(radius=3))
    
    # 2. ЦЕНТРАЛЬНЫЙ ЧИП
    print("Рисуем чип...")
    chip_size = 45
    chip_layer = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    chip_draw = ImageDraw.Draw(chip_layer)
    
    chip_draw.rectangle([(cx - chip_size, cy - chip_size), (cx + chip_size, cy + chip_size)], fill=(15, 23, 42, 255), outline=(56, 189, 248, 255), width=4)
    for angle in range(0, 360, 45):
        rad = math.radians(angle)
        end_x = cx + (chip_size + 50) * math.cos(rad)
        end_y = cy + (chip_size + 50) * math.sin(rad)
        chip_draw.line([(cx, cy), (end_x, end_y)], fill=(56, 189, 248, 255), width=3)
        chip_draw.ellipse([(end_x-4, end_y-4), (end_x+4, end_y+4)], fill=(14, 165, 233, 255))
    chip_draw.rectangle([(cx - 20, cy - 20), (cx + 20, cy + 20)], fill=(56, 189, 248, 255))

    img.paste(brain_layer_blurred, (0, 0), brain_layer_blurred)
    img.paste(chip_layer, (0, 0), chip_layer)

    # 3. ИКОНКИ И СЕТЬ СВЯЗЕЙ
    print("Создаем паутину связей и символов...")
    
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

    # Рисуем СВЯЗИ (очень много)
    # 1. От чипа к мозгу
    for _ in range(100):
        target_x = random.choice(brain_points)[0] if random.random() > 0.2 else random.choice(cerebellum_points)[0]
        target_y = random.choice(brain_points)[1] if random.random() > 0.2 else random.choice(cerebellum_points)[1]
        
        # Рисуем тонкие линии от чипа
        if random.random() > 0.5:
             draw.line([(cx, cy), (target_x, target_y)], fill=(56, 189, 248, 80), width=1)

    # 2. Между иконками и мозгом
    for i, (nx, ny, r, shape, icon) in enumerate(nodes):
        angle_to_center = math.atan2(cy - ny, cx - nx)
        start_x = nx + r * math.cos(angle_to_center)
        start_y = ny + r * math.sin(angle_to_center)
        end_x = cx + 160 * math.cos(angle_to_center)
        end_y = cy + 180 * math.sin(angle_to_center)
        
        # Рисуем пунктир
        length = math.hypot(end_x - start_x, end_y - start_y)
        steps = int(length / 12)
        for step in range(steps):
            if step % 2 == 0:
                x1 = start_x + (end_x - start_x) * (step / steps)
                y1 = start_y + (end_y - start_y) * (step / steps)
                x2 = start_x + (end_x - start_x) * ((step + 0.8) / steps)
                y2 = start_y + (end_y - start_y) * ((step + 0.8) / steps)
                draw.line([(x1, y1), (x2, y2)], fill="#94A3B8", width=2)
                
                # РАЗБРАСЫВАЕМ СИМВОЛЫ ВДОЛЬ ЛИНИЙ (Мысли)
                if random.random() > 0.6:
                    syms = ['question', 'plus', 'dot', 'infinity']
                    draw_symbol(draw, random.choice(syms), x1, y1, random.randint(2,4), "#94A3B8")

        # 3. Между иконками (Паутина)
        for j, (mx, my, mr, mshape, micon) in enumerate(nodes):
            if i != j:
                dist_nodes = math.hypot(nx - mx, ny - my)
                if dist_nodes < 280:
                    angle_nodes = math.atan2(my - ny, mx - nx)
                    s_x = nx + r * math.cos(angle_nodes)
                    s_y = ny + r * math.sin(angle_nodes)
                    e_x = mx + mr * math.cos(angle_nodes + math.pi)
                    e_y = my + mr * math.sin(angle_nodes + math.pi)
                    
                    # Пунктир между иконками
                    l = math.hypot(e_x - s_x, e_y - s_y)
                    st = int(l / 12)
                    for step in range(st):
                        if step % 2 == 0:
                            x1 = s_x + (e_x - s_x) * (step / st)
                            y1 = s_y + (e_y - s_y) * (step / st)
                            x2 = s_x + (e_x - s_x) * ((step + 0.8) / st)
                            y2 = s_y + (e_y - s_y) * ((step + 0.8) / st)
                            draw.line([(x1, y1), (x2, y2)], fill="#CBD5E1", width=2)
                            
                            # Символы на связях
                            if random.random() > 0.7:
                                syms = ['exclamation', 'at', 'star', 'eye']
                                draw_symbol(draw, random.choice(syms), x1, y1, random.randint(2,4), "#CBD5E1")


    # 4. ДОБАВЛЯЕМ СИМВОЛЫ В САМ МОЗГ (Беспорядочно)
    for _ in range(60):
        if random.random() > 0.5:
            p = random.choice(brain_points)
        else:
            p = random.choice(cerebellum_points)
        
        sym_type = random.choice(['question', 'exclamation', 'plus', 'infinity', 'at', 'star', 'eye'])
        draw_symbol(draw, sym_type, p[0], p[1], random.randint(3, 6), (255, 255, 255, random.randint(100, 200)))


    # 5. РИСУЕМ САМИ ИКОНКИ (Фигуры)
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

    output_file = "Ultimate_Brain_SecondMemory.png"
    img.save(output_file, quality=100)
    print(f"ГОТОВО! Файл сохранен как {output_file}")

if __name__ == "__main__":
    create_ultimate_brain()
