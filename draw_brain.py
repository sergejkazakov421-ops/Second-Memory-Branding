from PIL import Image, ImageDraw
import math

def create_brain_art():
    print("Создаем холст...")
    width, height = 800, 600
    img = Image.new('RGB', (width, height), '#F8F9FA')
    draw = ImageDraw.Draw(img)

    colors = [
        (220, 240, 235), (240, 230, 230), (245, 240, 220), 
        (220, 230, 245), (230, 220, 240)
    ]

    cx, cy = width // 2, height // 2
    
    print("Рисуем связи...")
    nodes = [
        (cx - 200, cy - 100, 45), (cx - 250, cy + 50, 35),
        (cx - 100, cy + 150, 50), (cx + 150, cy - 150, 40),
        (cx + 250, cy - 20, 55), (cx + 200, cy + 120, 45),
        (cx, cy - 180, 30)
    ]

    for (nx, ny, r) in nodes:
        angle = math.atan2(ny - cy, nx - cx)
        start_x = cx + 100 * math.cos(angle)
        start_y = cy + 100 * math.sin(angle)
        end_x = nx - r * math.cos(angle)
        end_y = ny - r * math.sin(angle)
        
        length = math.hypot(end_x - start_x, end_y - start_y)
        steps = int(length / 10)
        for i in range(steps):
            if i % 2 == 0:
                x1 = start_x + (end_x - start_x) * (i / steps)
                y1 = start_y + (end_y - start_y) * (i / steps)
                x2 = start_x + (end_x - start_x) * ((i + 1) / steps)
                y2 = start_y + (end_y - start_y) * ((i + 1) / steps)
                draw.line([(x1, y1), (x2, y2)], fill=(150, 150, 150), width=2)

    print("Рисуем облачка и иконки...")
    for i, (nx, ny, r) in enumerate(nodes):
        color = colors[i % len(colors)]
        draw.ellipse([(nx - r, ny - r), (nx + r, ny + r)], fill=color)
        
        if i == 0: # Булавка (Гео)
            draw.ellipse([(nx - 10, ny - 15), (nx + 10, ny + 5)], outline=(80, 80, 80), width=3)
            draw.polygon([(nx - 5, ny), (nx + 5, ny), (nx, ny + 15)], fill=(80, 80, 80))
        elif i == 1: # Часы (Будильник)
            draw.ellipse([(nx - 15, ny - 15), (nx + 15, ny + 15)], outline=(80, 80, 80), width=3)
            draw.line([(nx, ny), (nx, ny - 10)], fill=(80, 80, 80), width=2)
            draw.line([(nx, ny), (nx + 8, ny + 5)], fill=(80, 80, 80), width=2)
        elif i == 2: # Заметка
            draw.rectangle([(nx - 12, ny - 15), (nx + 12, ny + 15)], outline=(80, 80, 80), width=3)
            draw.line([(nx - 6, ny - 5), (nx + 6, ny - 5)], fill=(80, 80, 80), width=2)
            draw.line([(nx - 6, ny + 2), (nx + 6, ny + 2)], fill=(80, 80, 80), width=2)
        elif i == 3: # Микрофон (ИИ)
            draw.rounded_rectangle([(nx - 6, ny - 12), (nx + 6, ny + 4)], radius=6, outline=(80, 80, 80), width=3)
            draw.arc([(nx - 12, ny - 6), (nx + 12, ny + 12)], start=0, end=180, fill=(80, 80, 80), width=3)
            draw.line([(nx, ny + 12), (nx, ny + 18)], fill=(80, 80, 80), width=3)

    print("Рисуем центральный мозг...")
    brain_color = (245, 245, 245)
    outline_color = (100, 150, 200)
    
    draw.ellipse([(cx - 130, cy - 100), (cx + 130, cy + 100)], fill=brain_color, outline=outline_color, width=4)
    draw.polygon([(cx - 20, cy + 100), (cx, cy + 140), (cx + 20, cy + 100)], fill=brain_color, outline=outline_color)
    draw.line([(cx - 19, cy + 100), (cx + 19, cy + 100)], fill=brain_color, width=4)

    output_file = "SecondMemory_Brain.png"
    img.save(output_file)
    print(f"ГОТОВО! Файл сохранен как {output_file}")

if __name__ == "__main__":
    create_brain_art()
