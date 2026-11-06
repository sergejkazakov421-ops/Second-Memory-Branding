from PIL import Image, ImageDraw, ImageFilter
import math
import random

def draw_thought_node(draw, x, y, size, color):
    """Рисует маленький пузырь мысли (разной формы) с символом внутри"""
    shape = random.choice(['circle', 'square', 'diamond', 'rect', 'oval'])
    
    # Рисуем форму
    if shape == 'circle':
        draw.ellipse([(x-size, y-size), (x+size, y+size)], fill=color, outline=(150,150,150))
    elif shape == 'square':
        draw.rectangle([(x-size, y-size), (x+size, y+size)], fill=color, outline=(150,150,150))
    elif shape == 'diamond':
        draw.polygon([(x, y-size), (x+size, y), (x, y+size), (x-size, y)], fill=color, outline=(150,150,150))
    elif shape == 'rect':
        draw.rectangle([(x-size, y-size*0.6), (x+size, y+size*0.6)], fill=color, outline=(150,150,150))
    elif shape == 'oval':
        draw.ellipse([(x-size*0.8, y-size*0.5), (x+size*0.8, y+size*0.5)], fill=color, outline=(150,150,150))

    # Рисуем символ внутри
    sym = random.choice(['smile', 'sad', 'question', 'excl', 'bell', 'clock', 'pin', 'mic'])
    icon_color = (50, 50, 50)
    s = size * 0.6 # Масштаб иконки
    
    if sym == 'smile':
        draw.arc([(x-s, y-s), (x+s, y+s)], start=0, end=180, fill=icon_color, width=2)
        draw.ellipse([(x-s/2, y-s/2), (x-s/3, y-s/3)], fill=icon_color)
        draw.ellipse([(x+s/3, y-s/2), (x+s/2, y-s/3)], fill=icon_color)
    elif sym == 'sad':
        draw.arc([(x-s, y-s), (x+s, y+s)], start=180, end=0, fill=icon_color, width=2)
        draw.ellipse([(x-s/2, y-s/2), (x-s/3, y-s/3)], fill=icon_color)
        draw.ellipse([(x+s/3, y-s/2), (x+s/2, y-s/3)], fill=icon_color)
    elif sym == 'question':
        draw.text((x-s/2, y-s), "?", fill=icon_color)
    elif sym == 'excl':
        draw.text((x-s/4, y-s), "!", fill=icon_color)
    elif sym == 'bell':
        draw.arc([(x-s, y-s), (x+s, y+s)], start=180, end=0, fill=icon_color, width=2)
        draw.line([(x-s, y), (x-s*1.2, y+s*0.5), (x+s*1.2, y+s*0.5), (x+s, y)], fill=icon_color, width=2)
        draw.ellipse([(x-s/4, y+s*0.5), (x+s/4, y+s*0.8)], fill=icon_color)
    elif sym == 'clock':
        draw.ellipse([(x-s, y-s), (x+s, y+s)], outline=icon_color, width=2)
        draw.line([(x, y), (x, y-s*0.6)], fill=icon_color, width=2)
        draw.line([(x, y), (x+s*0.5, y+s*0.3)], fill=icon_color, width=2)
    elif sym == 'pin':
        draw.ellipse([(x-s*0.6, y-s), (x+s*0.6, y)], outline=icon_color, width=2)
        draw.polygon([(x-s*0.3, y-s*0.2), (x+s*0.3, y-s*0.2), (x, y+s*0.8)], fill=icon_color)
    elif sym == 'mic':
        draw.rounded_rectangle([(x-s*0.4, y-s), (x+s*0.4, y)], radius=3, outline=icon_color, width=2)
        draw.arc([(x-s*0.8, y-s*0.5), (x+s*0.8, y+s*0.8)], start=0, end=180, fill=icon_color, width=2)


def draw_main_icon(draw, icon_type, x, y, color):
    """Главные иконки приложения"""
    # (Код функций иконок остается прежним, я его немного сократил для читаемости)
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


def create_thought_flow():
    print("Создаем холст...")
    width, height = 1200, 900
    img = Image.new('RGB', (width, height), '#F8FAFC')
    draw = ImageDraw.Draw(img)

    cx, cy = width // 2, height // 2 - 20

    # 1. ГЕНЕРАЦИЯ МОЗГА (С V-образным вырезом)
    print("Генерируем мозг с V-образным вырезом...")
    
    brain_layer = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    brain_draw = ImageDraw.Draw(brain_layer)

    brain_points = []
    cerebellum_points = []

    for _ in range(25000):
        x = cx + random.uniform(-250, 250)
        y = cy + random.uniform(-220, 250)
        
        # 1. Полушария (овалы)
        in_left = ((x - (cx - 65)) / 120)**2 + ((y - cy) / 175)**2 < 1
        in_right = ((x - (cx + 65)) / 120)**2 + ((y - cy) / 175)**2 < 1
        
        # V-образный вырез внизу по центру (освобождаем место для мозжечка)
        if (in_left or in_right) and y > cy + 80 and abs(x - cx) < 35 + (y - (cy+80))*0.2:
            in_left = False
            in_right = False

        # 2. Мозжечок (в вырезе)
        in_cerebellum = ((x - cx) / 70)**2 + ((y - (cy + 130)) / 45)**2 < 1

        if in_left or in_right or in_cerebellum:
            
            # Центральная борозда
            if not in_cerebellum and abs(x - cx) < 15:
                if random.random() > 0.2: 
                    continue
            
            # Рыхлость
            edge_factor = random.random()
            is_edge = False
            if in_left and ((x - (cx - 65)) / 120)**2 + ((y - cy) / 175)**2 > 0.75: is_edge = True
            if in_right and ((x - (cx + 65)) / 120)**2 + ((y - cy) / 175)**2 > 0.75: is_edge = True
            if in_cerebellum and ((x - cx) / 70)**2 + ((y - (cy + 130)) / 45)**2 > 0.75: is_edge = True
            
            if is_edge and edge_factor > 0.3: 
                r = random.randint(1, 3)
                alpha = random.randint(30, 100)
            else:
                r = random.randint(2, 5)
                alpha = random.randint(100, 255)

            if in_cerebellum:
                color = (57, 255, 20, alpha) # Салатовый
                cerebellum_points.append((x, y))
            else:
                if random.random() > 0.85: color = (255, 255, 255, alpha)
                else: color = (random.randint(30, 100), random.randint(150, 220), 255, alpha)
                brain_points.append((x, y))
            
            brain_draw.ellipse([(x-r, y-r), (x+r, y+r)], fill=color)

    brain_layer_blurred = brain_layer.filter(ImageFilter.GaussianBlur(radius=3))
    
    # 2. ЧИП
    print("Рисуем чип...")
    chip_size = 50
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

    # 3. ИКОНКИ И ПЛАВНЫЕ СВЯЗИ С МЫСЛЯМИ
    print("Создаем плавные связи с мыслями...")
    
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
    thought_colors = ["#BAE6FD", "#FDE68A", "#BBF7D0", "#FECDD3", "#DDD6FE"]

    def draw_smooth_dotted_line(x1, y1, x2, y2, color, width):
        """Рисует плавную изогнутую пунктирную линию"""
        dist = math.hypot(x2-x1, y2-y1)
        steps = int(dist / 10)
        if steps < 2: steps = 2
        
        # Контрольная точка для изгиба (случайное отклонение от центра)
        mid_x = (x1 + x2) / 2
        mid_y = (y1 + y2) / 2
        offset = random.uniform(-50, 50)
        
        # Перпендикуляр для изгиба
        dx = x2 - x1
        dy = y2 - y1
        length = math.hypot(dx, dy)
        if length == 0: length = 1
        perp_x = -dy / length
        perp_y = dx / length
        
        ctrl_x = mid_x + perp_x * offset
        ctrl_y = mid_y + perp_y * offset

        # Рисуем квадратичную кривую Безье
        for i in range(steps):
            t1 = i / steps
            t2 = (i + 0.5) / steps
            # Формула Безье
            b1_x = (1-t1)**2 * x1 + 2*(1-t1)*t1 * ctrl_x + t1**2 * x2
            b1_y = (1-t1)**2 * y1 + 2*(1-t1)*t1 * ctrl_y + t1**2 * y2
            b2_x = (1-t2)**2 * x1 + 2*(1-t2)*t2 * ctrl_x + t2**2 * x2
            b2_y = (1-t2)**2 * y1 + 2*(1-t2)*t2 * ctrl_y + t2**2 * y2
            
            draw.line([(b1_x, b1_y), (b2_x, b2_y)], fill=color, width=width)
            
            # Добавляем мысли вдоль линии
            if random.random() > 0.7:
                draw_thought_node(draw, b1_x + random.uniform(-15, 15), b1_y + random.uniform(-15, 15), random.randint(6, 12), random.choice(thought_colors))


    # Рисуем связи
    for i, (nx, ny, r, shape, icon) in enumerate(nodes):
        # Связь с мозгом
        target_x, target_y = random.choice(brain_points)
        draw_smooth_dotted_line(nx, ny, target_x, target_y, "#94A3B8", 2)
        
        # Связи между иконками
        for j, (mx, my, mr, mshape, micon) in enumerate(nodes):
            if i < j and math.hypot(nx - mx, ny - my) < 400:
                draw_smooth_dotted_line(nx, ny, mx, my, "#CBD5E1", 2)

    # 4. РИСУЕМ САМИ ФИГУРЫ ИКОНКИ
    for i, (nx, ny, r, shape, icon) in enumerate(nodes):
        color = colors[i]
        if shape == 'circle': draw.ellipse([(nx - r, ny - r), (nx + r, ny + r)], fill=color, outline="#94A3B8", width=2)
        elif shape == 'square': draw.rectangle([(nx - r, ny - r), (nx + r, ny + r)], fill=color, outline="#94A3B8", width=2)
        elif shape == 'diamond': draw.polygon([(nx, ny - r), (nx + r, ny), (nx, ny + r), (nx - r, ny)], fill=color, outline="#94A3B8")
        draw_main_icon(draw, icon, nx, ny, icon_color)

    output_file = "Smooth_Brain_SecondMemory.png"
    img.save(output_file, quality=100)
    print(f"ГОТОВО! Файл сохранен как {output_file}")

if __name__ == "__main__":
    create_thought_flow()
