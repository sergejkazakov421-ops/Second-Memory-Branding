from PIL import Image, ImageDraw, ImageFilter, ImageFont
import math
import random
import traceback

try:
    font = ImageFont.load_default()
except:
    font = None

def draw_thought_node(draw, x, y, size, color, is_rgba=False):
    c_fill = color if is_rgba else color[:3]
    c_out = (100, 100, 100, 255) if is_rgba else (100, 100, 100)
    c_icon = (20, 20, 20, 255) if is_rgba else (20, 20, 20)

    shape = random.choice(['circle', 'square', 'diamond', 'rect', 'oval'])
    if shape == 'circle': draw.ellipse([(x-size, y-size), (x+size, y+size)], fill=c_fill, outline=c_out)
    elif shape == 'square': draw.rectangle([(x-size, y-size), (x+size, y+size)], fill=c_fill, outline=c_out)
    elif shape == 'diamond': draw.polygon([(x, y-size), (x+size, y), (x, y+size), (x-size, y)], fill=c_fill, outline=c_out)
    elif shape == 'rect': draw.rectangle([(x-size, y-size*0.6), (x+size, y+size*0.6)], fill=c_fill, outline=c_out)
    elif shape == 'oval': draw.ellipse([(x-size*0.8, y-size*0.5), (x+size*0.8, y+size*0.5)], fill=c_fill, outline=c_out)

    sym = random.choice(['smile', 'sad', 'question', 'excl', 'bell', 'clock', 'pin', 'mic'])
    s = size * 0.6
    
    if sym == 'smile':
        draw.arc([(x-s, y-s), (x+s, y+s)], start=0, end=180, fill=c_icon, width=2)
        draw.ellipse([(x-s/2, y-s/2), (x-s/3, y-s/3)], fill=c_icon)
        draw.ellipse([(x+s/3, y-s/2), (x+s/2, y-s/3)], fill=c_icon)
    elif sym == 'sad':
        draw.arc([(x-s, y-s), (x+s, y+s)], start=180, end=0, fill=c_icon, width=2)
        draw.ellipse([(x-s/2, y-s/2), (x-s/3, y-s/3)], fill=c_icon)
        draw.ellipse([(x+s/3, y-s/2), (x+s/2, y-s/3)], fill=c_icon)
    elif sym == 'question' and font: draw.text((x-s/2, y-s), "?", fill=c_icon, font=font)
    elif sym == 'excl' and font: draw.text((x-s/4, y-s), "!", fill=c_icon, font=font)
    elif sym == 'bell':
        draw.arc([(x-s, y-s), (x+s, y+s)], start=180, end=0, fill=c_icon, width=2)
        draw.line([(x-s, y), (x-s*1.2, y+s*0.5), (x+s*1.2, y+s*0.5), (x+s, y)], fill=c_icon, width=2)
        draw.ellipse([(x-s/4, y+s*0.5), (x+s/4, y+s*0.8)], fill=c_icon)
    elif sym == 'clock':
        draw.ellipse([(x-s, y-s), (x+s, y+s)], outline=c_icon, width=2)
        draw.line([(x, y), (x, y-s*0.6)], fill=c_icon, width=2)
        draw.line([(x, y), (x+s*0.5, y+s*0.3)], fill=c_icon, width=2)
    elif sym == 'pin':
        draw.ellipse([(x-s*0.6, y-s), (x+s*0.6, y)], outline=c_icon, width=2)
        draw.polygon([(x-s*0.3, y-s*0.2), (x+s*0.3, y-s*0.2), (x, y+s*0.8)], fill=c_icon)
    elif sym == 'mic':
        draw.rounded_rectangle([(x-s*0.4, y-s), (x+s*0.4, y)], radius=3, outline=c_icon, width=2)
        draw.arc([(x-s*0.8, y-s*0.5), (x+s*0.8, y+s*0.8)], start=0, end=180, fill=c_icon, width=2)

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

def create_perfect_layout():
    print("Создаем холст...")
    width, height = 1200, 900
    img = Image.new('RGB', (width, height), '#E2E8F0') 
    draw = ImageDraw.Draw(img)
    
    cx, cy = width // 2, height // 2 - 20

    # ==========================================
    # СЛОЙ 1: БЛЕДНЫЙ ФОН С ПАУТИНОЙ
    # ==========================================
    print("Генерируем бледный фон и паутину...")
    bg_layer = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    bg_draw = ImageDraw.Draw(bg_layer)

    bg_colors = [(186, 230, 253, 60), (253, 230, 138, 60), (187, 247, 208, 60), (254, 205, 211, 60), (221, 214, 254, 60)]
    bg_nodes = [] # Список для хранения координат фоновых символов
    
    # 1. Сначала генерируем координаты и рисуем символы
    for _ in range(600): 
        x = random.randint(0, width)
        y = random.randint(0, height)
        size = random.randint(4, 10)
        color = random.choice(bg_colors)
        
        bg_nodes.append((x, y, size))
        draw_thought_node(bg_draw, x, y, size, color, is_rgba=True)

    # 2. Теперь рисуем паутину между ними
    for i in range(len(bg_nodes)):
        x1, y1, s1 = bg_nodes[i]
        # Ищем соседей для соединения
        connections = 0
        for j in range(i + 1, len(bg_nodes)):
            x2, y2, s2 = bg_nodes[j]
            dist = math.hypot(x2 - x1, y2 - y1)
            
            # Соединяем только близкие символы
            if dist < 90: 
                # Тонкая, почти прозрачная линия
                bg_draw.line([(x1, y1), (x2, y2)], fill=(150, 150, 150, 50), width=1)
                connections += 1
                if connections >= 3: # Ограничиваем количество связей для одного узла, чтобы не было каши
                    break

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

    for _ in range(30000):
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
            
            is_edge = False
            if in_left and dist_left > 0.6: is_edge = True
            if in_right and dist_right > 0.6: is_edge = True
            if in_cerebellum and dist_cereb > 0.6: is_edge = True
            
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
                else:
                    if random.random() < 0.4:
                        core_draw.ellipse([(x-r_core, y-r_core), (x+r_core, y+r_core)], fill=(255, 255, 255, 255))
                        glow_draw.ellipse([(x-r_glow, y-r_glow), (x+r_glow, y+r_glow)], fill=(255, 255, 255, 200))
                    else:
                        core_draw.ellipse([(x-r_core, y-r_core), (x+r_core, y+r_core)], fill=(0, 200, 255, 255))
                        glow_draw.ellipse([(x-r_glow, y-r_glow), (x+r_glow, y+r_glow)], fill=(0, 255, 255, 150))
                    brain_points.append((x, y))

    if len(brain_points) == 0:
        brain_points = [(cx, cy)]

    glow_layer_blurred = glow_layer.filter(ImageFilter.GaussianBlur(radius=15))
    img.paste(glow_layer_blurred, (0, 0), glow_layer_blurred)
    core_layer_blurred = core_layer.filter(ImageFilter.GaussianBlur(radius=1))
    img.paste(core_layer_blurred, (0, 0), core_layer_blurred)
    
    # Чип
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
    # СЛОЙ 3: ГЛАВНЫЕ ИКОНКИ
    # ==========================================
    print("Рисуем главные иконки и связи...")
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
            
            if random.random() > 0.6:
                thought_colors = [(186, 230, 253), (253, 230, 138), (187, 247, 208), (254, 205, 211), (221, 214, 254)]
                draw_thought_node(draw, b1_x + random.uniform(-20, 20), b1_y + random.uniform(-20, 20), random.randint(6, 12), random.choice(thought_colors), is_rgba=False)

    for i, (nx, ny, r, shape, icon) in enumerate(nodes):
        for _ in range(2):
            target_x, target_y = random.choice(brain_points)
            draw_smooth_dotted_line(nx, ny, target_x, target_y, "#475569", 3)
        
        for j, (mx, my, mr, mshape, micon) in enumerate(nodes):
            if i < j and math.hypot(nx - mx, ny - my) < 500:
                draw_smooth_dotted_line(nx, ny, mx, my, "#64748B", 3)

    for i, (nx, ny, r, shape, icon) in enumerate(nodes):
        color = colors[i % len(colors)]
        outline_c = "#FFFFFF" 
        
        if shape == 'circle': draw.ellipse([(nx - r, ny - r), (nx + r, ny + r)], fill=color, outline=outline_c, width=4)
        elif shape == 'square': draw.rectangle([(nx - r, ny - r), (nx + r, ny + r)], fill=color, outline=outline_c, width=4)
        elif shape == 'diamond': draw.polygon([(nx, ny - r), (nx + r, ny), (nx, ny + r), (nx - r, ny)], fill=color, outline=outline_c)
        elif shape == 'oval': draw.ellipse([(nx - r*1.3, ny - r*0.7), (nx + r*1.3, ny + r*0.7)], fill=color, outline=outline_c, width=4)
        elif shape == 'rect': draw.rectangle([(nx - r*1.5, ny - r*0.8), (nx + r*1.5, ny + r*0.8)], fill=color, outline=outline_c, width=4)
        
        draw_main_icon(draw, icon, nx, ny, "#1E293B")

    output_file = "Perfect_Web_Brain_SecondMemory.png"
    img.save(output_file, quality=100)
    print(f"ГОТОВО! Файл сохранен как {output_file}")

if __name__ == "__main__":
    try:
        create_perfect_layout()
    except Exception as e:
        print("\n--- ПРОИЗОШЛА ОШИБКА В PYTHON ---")
        print(e)
        traceback.print_exc()
