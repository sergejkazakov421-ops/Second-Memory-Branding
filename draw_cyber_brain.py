from PIL import Image, ImageDraw, ImageFilter
import math
import random

def create_cyber_brain():
    print("Создаем холст...")
    width, height = 1000, 800
    img = Image.new('RGB', (width, height), '#F4F7F9') # Очень светлый, почти белый фон
    draw = ImageDraw.Draw(img)

    cx, cy = width // 2, height // 2

    # 1. РИСУЕМ ПУНКТИРНЫЕ ЛИНИИ К ОБЛАЧКАМ
    print("Рисуем связи...")
    nodes = [
        (cx - 250, cy - 150, 55), (cx - 350, cy + 50, 45),
        (cx - 150, cy + 200, 60), (cx + 200, cy - 200, 50),
        (cx + 300, cy - 50, 65), (cx + 250, cy + 150, 55),
        (cx, cy - 250, 45)
    ]

    for (nx, ny, r) in nodes:
        angle = math.atan2(ny - cy, nx - cx)
        start_x = cx + 150 * math.cos(angle)
        start_y = cy + 150 * math.sin(angle)
        end_x = nx - (r + 10) * math.cos(angle)
        end_y = ny - (r + 10) * math.sin(angle)
        
        length = math.hypot(end_x - start_x, end_y - start_y)
        steps = int(length / 15)
        for i in range(steps):
            if i % 2 == 0:
                x1 = start_x + (end_x - start_x) * (i / steps)
                y1 = start_y + (end_y - start_y) * (i / steps)
                x2 = start_x + (end_x - start_x) * ((i + 0.5) / steps)
                y2 = start_y + (end_y - start_y) * ((i + 0.5) / steps)
                draw.line([(x1, y1), (x2, y2)], fill="#94A3B8", width=3)

    # 2. РИСУЕМ ОБЛАЧКА И ИКОНКИ
    print("Рисуем облачка...")
    colors = ["#E0F2FE", "#FCE7F3", "#FEF3C7", "#DCFCE7", "#F3E8FF", "#E0E7FF", "#FFE4E6"]
    icon_color = "#334155"
    
    for i, (nx, ny, r) in enumerate(nodes):
        draw.ellipse([(nx - r, ny - r), (nx + r, ny + r)], fill=colors[i], outline="#CBD5E1", width=2)
        
        # Иконки
        if i == 0: # Булавка
            draw.ellipse([(nx - 12, ny - 18), (nx + 12, ny + 6)], outline=icon_color, width=4)
            draw.polygon([(nx - 6, ny), (nx + 6, ny), (nx, ny + 18)], fill=icon_color)
        elif i == 1: # Часы
            draw.ellipse([(nx - 18, ny - 18), (nx + 18, ny + 18)], outline=icon_color, width=4)
            draw.line([(nx, ny), (nx, ny - 12)], fill=icon_color, width=4)
            draw.line([(nx, ny), (nx + 10, ny + 6)], fill=icon_color, width=4)
        elif i == 2: # Заметка
            draw.rectangle([(nx - 15, ny - 18), (nx + 15, ny + 18)], outline=icon_color, width=4)
            draw.line([(nx - 8, ny - 6), (nx + 8, ny - 6)], fill=icon_color, width=3)
            draw.line([(nx - 8, ny + 2), (nx + 8, ny + 2)], fill=icon_color, width=3)
            draw.line([(nx - 8, ny + 10), (nx + 4, ny + 10)], fill=icon_color, width=3)
        elif i == 3: # Микрофон
            draw.rounded_rectangle([(nx - 8, ny - 15), (nx + 8, ny + 5)], radius=8, outline=icon_color, width=4)
            draw.arc([(nx - 15, ny - 8), (nx + 15, ny + 15)], start=0, end=180, fill=icon_color, width=4)
            draw.line([(nx, ny + 15), (nx, ny + 22)], fill=icon_color, width=4)

    # 3. РИСУЕМ КИБЕР-МОЗГ (НЕЙРОСЕТЬ)
    print("Создаем кибернетический мозг (это займет пару секунд)...")
    
    # Слой для свечения мозга
    glow_layer = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    glow_draw = ImageDraw.Draw(glow_layer)

    # Математическая генерация точек мозга
    points = []
    # Левое и правое полушарие
    for _ in range(1500):
        # Случайный угол и радиус для создания формы двух долей
        side = random.choice([-1, 1])
        angle = random.uniform(0, math.pi * 2)
        radius = random.uniform(50, 180)
        
        # Деформация для придания формы мозга
        x = cx + side * radius * math.cos(angle) * 0.8
        y = cy + radius * math.sin(angle) * 0.9 - 20
        
        # Ограничиваем форму, чтобы не было слишком квадратно
        if (x - cx)**2 / 150**2 + (y - cy)**2 / 180**2 < 1:
            points.append((x, y))

    # Рисуем нейронные связи (линии между близкими точками)
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            dist = math.hypot(points[i][0] - points[j][0], points[i][1] - points[j][1])
            if dist < 25: # Если точки близко - соединяем
                alpha = int(255 - (dist * 10)) # Чем дальше, тем прозрачнее
                if alpha > 0:
                    glow_draw.line([points[i], points[j]], fill=(56, 189, 248, alpha), width=2)

    # Рисуем сами нейроны (точки)
    for p in points:
        r = random.randint(2, 4)
        glow_draw.ellipse([(p[0]-r, p[1]-r), (p[0]+r, p[1]+r)], fill=(14, 165, 233, 255))

    # 4. НАМЕК НА ИИ (ЦЕНТРАЛЬНЫЙ ЧИП)
    # Рисуем чип в центре
    chip_size = 60
    glow_draw.rectangle([(cx - chip_size, cy - chip_size), (cx + chip_size, cy + chip_size)], fill=(15, 23, 42, 255), outline=(56, 189, 248, 255), width=4)
    
    # Дорожки от чипа
    for angle in range(0, 360, 45):
        rad = math.radians(angle)
        end_x = cx + (chip_size + 40) * math.cos(rad)
        end_y = cy + (chip_size + 40) * math.sin(rad)
        glow_draw.line([(cx, cy), (end_x, end_y)], fill=(56, 189, 248, 200), width=3)
        glow_draw.ellipse([(end_x-4, end_y-4), (end_x+4, end_y+4)], fill=(14, 165, 233, 255))
    
    # Внутренний чип
    glow_draw.rectangle([(cx - 25, cy - 25), (cx + 25, cy + 25)], fill=(56, 189, 248, 255))
    
    # Размываем слой для эффекта свечения (Neon glow)
    glow_layer_blurred = glow_layer.filter(ImageFilter.GaussianBlur(radius=6))
    
    # Накладываем свечение на основной холст
    img.paste(glow_layer_blurred, (0, 0), glow_layer_blurred)
    # Накладываем четкий слой поверх
    img.paste(glow_layer, (0, 0), glow_layer)

    output_file = "CyberBrain_SecondMemory.png"
    img.save(output_file, quality=100)
    print(f"ГОТОВО! Файл сохранен как {output_file}")

if __name__ == "__main__":
    create_cyber_brain()
