from PIL import Image, ImageDraw, ImageFilter
import math
import random

def draw_thought_node(draw, x, y, size, color):
    shape = random.choice(['circle', 'square', 'diamond', 'rect', 'oval'])
    if shape == 'circle': draw.ellipse([(x-size, y-size), (x+size, y+size)], fill=color, outline=(100,100,100))
    elif shape == 'square': draw.rectangle([(x-size, y-size), (x+size, y+size)], fill=color, outline=(100,100,100))
    elif shape == 'diamond': draw.polygon([(x, y-size), (x+size, y), (x, y+size), (x-size, y)], fill=color, outline=(100,100,100))
    elif shape == 'rect': draw.rectangle([(x-size, y-size*0.6), (x+size, y+size*0.6)], fill=color, outline=(100,100,100))
    elif shape == 'oval': draw.ellipse([(x-size*0.8, y-size*0.5), (x+size*0.8, y+size*0.5)], fill=color, outline=(100,100,100))

    sym = random.choice(['smile', 'sad', 'question', 'excl', 'bell', 'clock', 'pin', 'mic'])
    icon_color = (20, 20, 20)
    s = size * 0.6
    
    if sym == 'smile':
        draw.arc([(x-s, y-s), (x+s, y+s)], start=0, end=180, fill=icon_color, width=2)
        draw.ellipse([(x-s/2, y-s/2), (x-s/3, y-s/3)], fill=icon_color)
        draw.ellipse([(x+s/3, y-s/2), (x+s/2, y-s/3)], fill=icon_color)
    elif sym == 'sad':
        draw.arc([(x-s, y-s), (x+s, y+s)], start=180, end=0, fill=icon_color, width=2)
        draw.ellipse([(x-s/2, y-s/2), (x-s/3, y-s/3)], fill=icon_color)
        draw.ellipse([(x+s/3, y-s/2), (x+s/2, y-s/3)], fill=icon_color)
    elif sym == 'question': draw.text((x-s/2, y-s), "?", fill=icon_color)
    elif sym == 'excl': draw.text((x-s/4, y-s), "!", fill=icon_color)
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


def create_focused_chaos():
    print("Создаем холст...")
    width, height = 1200, 900
    # Базовый фон
    img = Image.new('RGB', (width, height), '#E2E8F0') 
    
    cx, cy = width // 2, height // 2 - 20

    # ==========================================
    # СЛОЙ 1: ФОН (ХАОС) - Делаем его бледным
    # ==========================================
    print("Генерируем бледный фон...")
    bg_layer = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    bg_draw = ImageDraw.Draw(bg_layer)

    # Уменьшаем количество фоновых символов, чтобы не было каши
    thought_colors = ["#BAE6FD", "#FDE68A", "#BBF7D0", "#FECDD3", "#DDD6FE"]
    for _ in range(600): 
        x = random.randint(0, width)
        y = random.randint(0, height)
        # Делаем их очень прозрачными (альфа 50), чтобы они не перебивали центр
        draw_thought_node(bg_draw, x, y, random.randint(3, 8), (*Image.new('RGB', (1, 1), random.choice(thought_colors)).getpixel((0,0)), 60))

    # Легкие линии фона
    for _ in range(300):
        x1, y1 = random.randint(0, width), random.randint(0, height)
        x2, y2 = x1 + random.randint(-150, 150), y1 + random.randint(-150, 150)
        bg_draw.line([(x1, y1), (x2, y2)], fill=(180, 180, 180, 40), width=1)

    img.paste(bg_layer, (0, 0), bg_layer)

    # ==========================================
    # СЛОЙ 2: НЕОНОВЫЙ МОЗГ
    # ==========================================
    print("Генерируем неоновый мозг...")
    glow_layer = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    glow_draw = ImageDraw.Draw(glow_layer)
    core_layer = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    core_draw = ImageDraw.Draw(core_layer)

    brain_points = []
    cerebellum_points = []

    for _ in range(50000):
        x = cx + random.uniform(-280, 280)
        y = cy + random.uniform(-250, 280)
        
        in_left = ((x - (cx - 65)) / 120)**2 + ((y - cy) / 175)**2 < 1
        in_right = ((x - (cx + 65)) / 120)**2 + ((y - cy) / 175)**2 < 1
        if (in_left or in_right) and y > cy + 80 and abs(x - cx) < 40 + (y - (cy+80))*0.2:
            in_left = False
            in_right = False
        in_cerebellum = ((x - cx) / 70)**2 + ((y - (cy + 130)) / 45)**2 < 1

        if in_left or in_right or in_cerebellum:
            if not in_cerebellum and abs(x - cx) < 15:
                if random.random() > 0.15: continue
            
            dist_left = ((x - (cx - 65)) / 120)**2 + ((y - cy) / 175)**2
            dist_right = ((x - (cx + 65)) / 120)**2 + ((y - cy) / 175)**2
            dist_cereb = ((x - cx) / 70)**2 + ((y - (cy + 130)) / 45)**2
            is_edge = (dist_left > 0.6) or (dist_right > 0.6) or (dist_cereb > 0.6)
            
            if is_edge:
                r_glow = random.randint(3, 8)
                alpha_glow = random.randint(20, 60)
                if in_cerebellum: glow_draw.ellipse([(x-r_glow, y-r_glow), (x+r_glow, y+r_glow)], fill=(57, 255, 20, alpha_glow))
                else: glow_draw.ellipse([(x-r_glow, y-r_glow), (x+r_glow, y+r_glow)], fill=(0, 255, 255, alpha_glow))
            else:
                r_core = random.randint(1, 4)
                r_glow = random.randint(5, 12)
                if in_cerebellum:
                    core_draw.ellipse([(x-r_core, y-r_core), (x+r_core, y+r_core)], fill=(57, 255, 20, 255))
                    glow_draw.ellipse([(x-r_glow, y-r_glow), (x+r_glow, y+r_glow)], fill=(57, 255, 20, 150))
                    cerebellum_points.append((x, y))
                else:
                    if random.random() < 0.4:
                        core_draw.ellipse([(x-r_core, y-r_core), (x+r_core, y+r_core)], fill=(255, 255, 255, 255))
                        glow_draw.ellipse([(x-r_glow, y-r_glow), (x+r_glow, y+r_glow)], fill=(255, 255, 255, 200))
                    else:
                        core_draw.ellipse([(x-r_core, y-r_core), (x+r_core, y+r_core)], fill=(0, 200, 255, 255))
                        glow_draw.ellipse([(x-r_glow, y-r_glow), (x+r_glow, y+r_glow)], fill=(0, 255, 255, 150))
                    brain_points.append((x, y))

    glow_layer_blurred = glow_layer.filter(ImageFilter.GaussianBlur(radius=15))
    img.paste(glow_layer_blurred, (0, 0), glow_layer_blurred)
    core_layer_blurred = core_layer.filter(ImageFilter.GaussianBlur(radius=1))
    img.paste(core_layer_blurred, (0, 0), core_layer_blurred)
    
    # Чип
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
    img.paste(chip_layer, (0, 0), chip_layer)

    # ==========================================
    # СЛОЙ 3: ГЛАВНЫЕ ИКОНКИ (НА ПЕРЕДНЕМ ПЛАНЕ)
    # ==========================================
    print("Рисуем главные иконки...")
    
    icons = ['folder', 'note', 'bell', 'heart', 'star', 'pin', 'clock', 'mic', 'cloud', 'lock', 'gear']
    shapes = ['circle', 'diamond', 'square', 'oval', 'rect']
    nodes = []
    
    for _ in range(14):
        while True:
            nx = random.randint(100, width - 100)
            ny = random.randint(100, height - 100)
            if math.hypot(nx - cx, ny - cy) > 280: 
                nodes.append((nx, ny, random.randint(35, 60), random.choice(shapes), random.choice(icons)))
                break

    colors = ["#FCE7F3", "#FEF3C7", "#DCFCE7", "#E0F2FE", "#F3E8FF", "#FFE4E6", "#CCFBF1", "#FEE2E2"]
    icon_color = "#1E293B"

    def draw_smooth_dotted_line(x1, y1, x2, y2, color, width):
        dist = math.hypot(x2-x1, y2-y1)
        steps = int(dist / 10)
        if steps < 2: steps = 2
        mid_x, mid_y = (x1 + x2) / 2, (y1 + y2) / 2
        offset = random.uniform(-80, 80) 
        dx, dy = x2 - x1, y2 - y1
        length = math.hypot(dx, dy)
        if length == 0: length = 1
        perp_x, perp_y = -dy / length, dx / length
        ctrl_x, ctrl_y = mid_x + perp_x * offset, mid_y + perp_y * offset

        for i in range(steps):
            t1, t2 = i / steps, (i + 0.5) / steps
            b1_x = (1-t1)**2 * x1 + 2*(1-t1)*t1 * ctrl_x + t1**2 * x2
            b1_y = (1-t1)**2 * y1 + 2*(1-t1)*t1 * ctrl_y + t1**2 * y2
            b2_x = (1-t2)**2 * x1 + 2*(1-t2)*t2 * ctrl_x + t2**2 * x2
            b2_y = (1-t2)**2 * y1 + 2*(1-t2)*t2 * ctrl_y + t2**2 * y2
            draw.line([(b1_x, b1_y), (b2_x, b2_y)], fill=color, width=width)

    # Линии от главных иконок
    for i, (nx, ny, r, shape, icon) in enumerate(nodes):
        for _ in range(2):
            target_x, target_y = random.choice(brain_points)
            draw_smooth_dotted_line(nx, ny, target_x, target_y, "#475569", 3) # Жирные темные линии
        
        for j, (mx, my, mr, mshape, micon) in enumerate(nodes):
            if i < j and math.hypot(nx - mx, ny - my) < 500:
                draw_smooth_dotted_line(nx, ny, mx, my, "#64748B", 3)

    # Сами иконки
    for i, (nx, ny, r, shape, icon) in enumerate(nodes):
        color = colors[i % len(colors)]
        outline_c = "#FFFFFF" # Белая обводка для контраста
        
        if shape == 'circle': draw.ellipse([(nx - r, ny - r), (nx + r, ny + r)], fill=color, outline=outline_c, width=4)
        elif shape == 'square': draw.rectangle([(nx - r, ny - r), (nx + r, ny + r)], fill=color, outline=outline_c, width=4)
        elif shape == 'diamond': draw.polygon([(nx, ny - r), (nx + r, ny), (nx, ny + r), (nx - r, ny)], fill=color, outline=outline_c)
        elif shape == 'oval': draw.ellipse([(nx - r*1.3, ny - r*0.7), (nx + r*1.3, ny + r*0.7)], fill=color, outline=outline_c, width=4)
        elif shape == 'rect': draw.rectangle([(nx - r*1.5, ny - r*0.8), (nx + r*1.5, ny + r*0.8)], fill=color, outline=outline_c, width=4)
        
        draw_main_icon(draw, icon, nx, ny, "#1E293B")

    output_file = "Perfect_Balance_Brain_SecondMemory.png"
    img.save(output_file, quality=100)
    print(f"ГОТОВО! Файл сохранен как {output_file}")

if __name__ == "__main__":
    create_focused_chaos()
