from PIL import Image, ImageDraw, ImageFilter
import math
import random

def draw_icon(draw, icon_type, x, y, color):
    """Функция для рисования иконок (центрированная)"""
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


def create_perfect_brain():
    print("Создаем холст...")
    width, height = 1200, 900
    img = Image.new('RGB', (width, height), '#F8FAFC')
    draw = ImageDraw.Draw(img)

    cx, cy = width // 2, height // 2

    # 1. ГЕНЕРАЦИЯ МОЗГА (Форма по вашему контуру)
    print("Генерируем мозг по вашей форме...")
    
    # Создаем слой для точек мозга
    brain_layer = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    brain_draw = ImageDraw.Draw(brain_layer)

    # Генерируем 4000 точек
    for _ in range(4000):
        # Случайная позиция вокруг центра
        x = cx + random.uniform(-200, 200)
        y = cy + random.uniform(-180, 180)
        
        # МАТЕМАТИЧЕСКАЯ МАСКА ФОРМЫ МОЗГА
        # Левое полушарие (овал)
        dist_left = ((x - (cx - 50)) / 140)**2 + ((y - cy) / 160)**2
        # Правое полушарие (овал)
        dist_right = ((x - (cx + 50)) / 140)**2 + ((y - cy) / 160)**2
        
        # Проверяем, попадает ли точка в одно из полушарий
        if dist_left < 1.0 or dist_right < 1.0:
            # Оставляем пустую полосу по центру (борозда)
            if abs(x - cx) < 10 and random.random() > 0.2: 
                continue
            
            # Делаем края рыхлыми (если точка близко к границе, иногда пропускаем)
            edge_chance = random.random()
            if (dist_left > 0.8 or dist_right > 0.8) and edge_chance > 0.6:
                continue

            # Рисуем точку
            r = random.randint(2, 6)
            alpha = random.randint(100, 255)
            # Цвет от голубого к синему
            color = (random.randint(50, 100), random.randint(150, 200), 255, alpha)
            brain_draw.ellipse([(x-r, y-r), (x+r, y+r)], fill=color)

    # Размываем мозг для эффекта мягкости
    brain_layer_blurred = brain_layer.filter(ImageFilter.GaussianBlur(radius=3))
    
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

    # Склеиваем мозг и чип
    img.paste(brain_layer_blurred, (0, 0), brain_layer_blurred)
    img.paste(chip_layer, (0, 0), chip_layer)


    # 3. РАССТАВЛЯЕМ ИКОНКИ (Хаос + Разные фигуры)
    print("Расставляем фигуры и иконки...")
    
    # (X, Y, Размер, Форма, Иконка, Родитель)
    nodes = [
        (cx - 300, cy - 200, 45, 'circle', 'folder', 'brain'),
        (cx - 420, cy + 50, 35, 'diamond', 'note', 0),
        (cx - 250, cy + 250, 50, 'square', 'bell', 0),
        (cx + 150, cy - 280, 40, 'circle', 'heart', 'brain'),
        (cx + 350, cy - 150, 55, 'diamond', 'star', 'brain'),
        (cx + 400, cy + 100, 45, 'square', 'pin', 4),
        (cx + 250, cy + 300, 50, 'circle', 'clock', 'brain'),
        (cx - 50, cy + 350, 35, 'diamond', 'mic', 6),
        (cx - 450, cy - 100, 30, 'square', 'cloud', 0),
        (cx + 500, cy - 50, 30, 'circle', 'lock', 4),
        (cx + 100, cy + 400, 25, 'diamond', 'gear', 7)
    ]

    colors = ["#FCE7F3", "#FEF3C7", "#DCFCE7", "#E0F2FE", "#F3E8FF", "#FFE4E6", "#CCFBF1", "#FEE2E2", "#E0F2FE", "#FEF3C7", "#FCE7F3"]
    icon_color = "#1E293B"

    # Сначала рисуем линии связи
    for i, (nx, ny, r, shape, icon, parent) in enumerate(nodes):
        if parent == 'brain':
            angle_to_center = math.atan2(cy - ny, cx - nx)
            start_x = nx + r * math.cos(angle_to_center)
            start_y = ny + r * math.sin(angle_to_center)
            # Примерная граница мозга
            end_x = cx + 130 * math.cos(angle_to_center)
            end_y = cy + 150 * math.sin(angle_to_center)
        else:
            px, py, pr, pshape, picon, pparent = nodes[parent]
            angle_to_parent = math.atan2(py - ny, px - nx)
            start_x = nx + r * math.cos(angle_to_parent)
            start_y = ny + r * math.sin(angle_to_parent)
            end_x = px + pr * math.cos(angle_to_parent + math.pi)
            end_y = py + pr * math.sin(angle_to_parent + math.pi)

        # Рисуем пунктирную линию
        length = math.hypot(end_x - start_x, end_y - start_y)
        steps = int(length / 12)
        for step in range(steps):
            if step % 2 == 0:
                x1 = start_x + (end_x - start_x) * (step / steps)
                y1 = start_y + (end_y - start_y) * (step / steps)
                x2 = start_x + (end_x - start_x) * ((step + 0.8) / steps)
                y2 = start_y + (end_y - start_y) * ((step + 0.8) / steps)
                draw.line([(x1, y1), (x2, y2)], fill="#94A3B8", width=2)


    # Теперь рисуем сами фигуры поверх линий
    for i, (nx, ny, r, shape, icon, parent) in enumerate(nodes):
        color = colors[i]
        
        if shape == 'circle':
            draw.ellipse([(nx - r, ny - r), (nx + r, ny + r)], fill=color, outline="#CBD5E1", width=2)
        elif shape == 'square':
            draw.rectangle([(nx - r, ny - r), (nx + r, ny + r)], fill=color, outline="#CBD5E1", width=2)
        elif shape == 'diamond':
            points = [(nx, ny - r), (nx + r, ny), (nx, ny + r), (nx - r, ny)]
            draw.polygon(points, fill=color, outline="#CBD5E1")
        
        draw_icon(draw, icon, nx, ny, icon_color)

    output_file = "Perfect_Brain_SecondMemory.png"
    img.save(output_file, quality=100)
    print(f"ГОТОВО! Файл сохранен как {output_file}")

if __name__ == "__main__":
    create_perfect_brain()
