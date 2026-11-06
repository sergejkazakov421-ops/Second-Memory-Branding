from PIL import Image, ImageDraw, ImageFilter
import math
import random

def draw_icon(draw, icon_type, x, y, color):
    """Функция для рисования иконок"""
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


def create_master_brain():
    print("Создаем холст...")
    width, height = 1200, 900
    img = Image.new('RGB', (width, height), '#F8FAFC')
    draw = ImageDraw.Draw(img)

    cx, cy = width // 2, height // 2 - 20 # Чуть поднимаем центр

    # 1. ГЕНЕРАЦИЯ АНАТОМИЧЕСКОГО МОЗГА
    print("Генерируем анатомический мозг...")
    
    brain_layer = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    brain_draw = ImageDraw.Draw(brain_layer)

    # Генерируем очень много точек
    for _ in range(12000):
        x = cx + random.uniform(-250, 250)
        y = cy + random.uniform(-200, 250)
        
        # МАТЕМАТИЧЕСКАЯ МАСКА (Полушария + Мозжечок)
        # Левое полушарие (вытянутое вверх-вниз)
        in_left = ((x - (cx - 60)) / 130)**2 + ((y - cy) / 170)**2 < 1
        # Правое полушарие
        in_right = ((x - (cx + 60)) / 130)**2 + ((y - cy) / 170)**2 < 1
        
        # Мозжечок (внизу по центру)
        in_cerebellum = ((x - cx) / 80)**2 + ((y - (cy + 140)) / 60)**2 < 1

        # Проверяем, попадает ли в мозг
        if in_left or in_right or in_cerebellum:
            
            # Делаем центральную борозду (разрыв между полушариями)
            if not in_cerebellum and abs(x - cx) < 15:
                if random.random() > 0.1: # Оставляем 10% точек в борозде для связности
                    continue
            
            # Добавляем рыхлость по краям (если точка близко к границе, иногда пропускаем)
            edge_factor = random.random()
            is_edge = (in_left and ((x - (cx - 60)) / 130)**2 + ((y - cy) / 170)**2 > 0.7) or \
                      (in_right and ((x - (cx + 60)) / 130)**2 + ((y - cy) / 170)**2 > 0.7) or \
                      (in_cerebellum and ((x - cx) / 80)**2 + ((y - (cy + 140)) / 60)**2 > 0.7)
            
            if is_edge and edge_factor > 0.4: # 60% точек на краю отбрасываем для "пушистости"
                continue

            # Рисуем точку
            r = random.randint(2, 6)
            alpha = random.randint(100, 255)
            color = (random.randint(30, 100), random.randint(150, 220), 255, alpha)
            
            # Слегка сдвигаем точки для хаоса
            px = x + random.uniform(-5, 5)
            py = y + random.uniform(-5, 5)
            
            brain_draw.ellipse([(px-r, py-r), (px+r, py+r)], fill=color)

    # Добавляем четкую центральную линию (борозду)
    print("Рисуем борозду...")
    for y_line in range(int(cy - 160), int(cy + 130), 15):
        if random.random() > 0.3: # Пунктирная линия
            brain_draw.ellipse([(cx-2, y_line-2), (cx+2, y_line+2)], fill=(56, 189, 248, 200))

    # Размываем для мягкости
    brain_layer_blurred = brain_layer.filter(ImageFilter.GaussianBlur(radius=4))
    
    # Центральный чип
    print("Рисуем чип...")
    chip_size = 45
    chip_layer = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    chip_draw = ImageDraw.Draw(chip_layer)
    
    chip_draw.rectangle([(cx - chip_size, cy - chip_size), (cx + chip_size, cy + chip_size)], fill=(15, 23, 42, 255), outline=(56, 189, 248, 255), width=4)
    for angle in range(0, 360, 45):
        rad = math.radians(angle)
        end_x = cx + (chip_size + 40) * math.cos(rad)
        end_y = cy + (chip_size + 40) * math.sin(rad)
        chip_draw.line([(cx, cy), (end_x, end_y)], fill=(56, 189, 248, 255), width=3)
        chip_draw.ellipse([(end_x-4, end_y-4), (end_x+4, end_y+4)], fill=(14, 165, 233, 255))
    chip_draw.rectangle([(cx - 20, cy - 20), (cx + 20, cy + 20)], fill=(56, 189, 248, 255))

    img.paste(brain_layer_blurred, (0, 0), brain_layer_blurred)
    img.paste(chip_layer, (0, 0), chip_layer)


    # 3. РАССТАВЛЯЕМ ИКОНКИ (Хаос + Связи друг с другом)
    print("Расставляем фигуры и создаем сеть...")
    
    # (X, Y, Размер, Форма, Иконка)
    nodes = [
        (cx - 320, cy - 200, 45, 'circle', 'folder'),
        (cx - 450, cy + 50, 35, 'diamond', 'note'),
        (cx - 280, cy + 250, 50, 'square', 'bell'),
        (cx + 150, cy - 300, 40, 'circle', 'heart'),
        (cx + 380, cy - 150, 55, 'diamond', 'star'),
        (cx + 420, cy + 120, 45, 'square', 'pin'),
        (cx + 280, cy + 320, 50, 'circle', 'clock'),
        (cx - 50, cy + 380, 35, 'diamond', 'mic'),
        (cx - 480, cy - 100, 30, 'square', 'cloud'),
        (cx + 520, cy - 50, 30, 'circle', 'lock'),
        (cx + 120, cy + 420, 25, 'diamond', 'gear')
    ]

    colors = ["#FCE7F3", "#FEF3C7", "#DCFCE7", "#E0F2FE", "#F3E8FF", "#FFE4E6", "#CCFBF1", "#FEE2E2", "#E0F2FE", "#FEF3C7", "#FCE7F3"]
    icon_color = "#1E293B"

    # Рисуем связи (СЕТЬ)
    for i, (nx, ny, r, shape, icon) in enumerate(nodes):
        
        # 1. Линия к мозгу (если близко)
        angle_to_center = math.atan2(cy - ny, cx - nx)
        dist_to_center = math.hypot(nx - cx, ny - cy)
        
        if dist_to_center < 400:
            start_x = nx + r * math.cos(angle_to_center)
            start_y = ny + r * math.sin(angle_to_center)
            end_x = cx + 140 * math.cos(angle_to_center)
            end_y = cy + 160 * math.sin(angle_to_center)
            
            length = math.hypot(end_x - start_x, end_y - start_y)
            steps = int(length / 12)
            for step in range(steps):
                if step % 2 == 0:
                    x1 = start_x + (end_x - start_x) * (step / steps)
                    y1 = start_y + (end_y - start_y) * (step / steps)
                    x2 = start_x + (end_x - start_x) * ((step + 0.8) / steps)
                    y2 = start_y + (end_y - start_y) * ((step + 0.8) / steps)
                    draw.line([(x1, y1), (x2, y2)], fill="#94A3B8", width=2)

        # 2. Линии между иконками (паутина)
        for j, (mx, my, mr, mshape, micon) in enumerate(nodes):
            if i != j:
                dist_nodes = math.hypot(nx - mx, ny - my)
                # Если иконки близко друг к другу - соединяем
                if dist_nodes < 250:
                    angle_nodes = math.atan2(my - ny, mx - nx)
                    s_x = nx + r * math.cos(angle_nodes)
                    s_y = ny + r * math.sin(angle_nodes)
                    e_x = mx + mr * math.cos(angle_nodes + math.pi)
                    e_y = my + mr * math.sin(angle_nodes + math.pi)
                    
                    l = math.hypot(e_x - s_x, e_y - s_y)
                    st = int(l / 12)
                    for step in range(st):
                        if step % 2 == 0:
                            x1 = s_x + (e_x - s_x) * (step / st)
                            y1 = s_y + (e_y - s_y) * (step / st)
                            x2 = s_x + (e_x - s_x) * ((step + 0.8) / st)
                            y2 = s_y + (e_y - s_y) * ((step + 0.8) / st)
                            draw.line([(x1, y1), (x2, y2)], fill="#CBD5E1", width=2)


    # Теперь рисуем сами фигуры
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

    output_file = "Anatomical_Brain_SecondMemory.png"
    img.save(output_file, quality=100)
    print(f"ГОТОВО! Файл сохранен как {output_file}")

if __name__ == "__main__":
    create_master_brain()
