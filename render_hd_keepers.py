import os
import shutil
import math
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

ASSET_DIR = "f:/Fly-Rank-AI/FL-03/assets"
BRAIN_DIR = "C:/Users/Hridoy/.gemini/antigravity-ide/brain/634783a7-719a-4a61-8f40-632b6f39d2ce"

os.makedirs(ASSET_DIR, exist_ok=True)
os.makedirs(BRAIN_DIR, exist_ok=True)

# -------------------------------------------------------------
# 1. HERO TEXTURE KEEPER (HD Render)
# -------------------------------------------------------------
def render_hero_texture_keeper():
    W, H = 1920, 1080
    img = Image.new('RGBA', (W, H), (11, 15, 25, 255)) # #0B0F19
    
    # 1A. Radial Glow Layer (Indigo/Cyan Gradient)
    glow = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    glow_draw = ImageDraw.Draw(glow)
    
    # Cyan Glow top-left
    cx, cy = int(W * 0.3), int(H * 0.4)
    for r in range(600, 0, -5):
        alpha = int(35 * (1 - r / 600)**2)
        glow_draw.ellipse([cx-r, cy-r, cx+r, cy+r], fill=(6, 182, 212, alpha))
        
    # Indigo Glow bottom-right
    cx2, cy2 = int(W * 0.7), int(H * 0.6)
    for r in range(700, 0, -5):
        alpha = int(40 * (1 - r / 700)**2)
        glow_draw.ellipse([cx2-r, cy2-r, cx2+r, cy2+r], fill=(99, 102, 241, alpha))
        
    img = Image.alpha_composite(img, glow)
    
    # 1B. Grid Lines
    grid = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    grid_draw = ImageDraw.Draw(grid)
    grid_step = 60
    for x in range(0, W, grid_step):
        grid_draw.line([(x, 0), (x, H)], fill=(255, 255, 255, 10), width=1)
    for y in range(0, H, grid_step):
        grid_draw.line([(0, y), (W, y)], fill=(255, 255, 255, 10), width=1)
    img = Image.alpha_composite(img, grid)
    
    # 1C. Glassmorphic UI Wireframe Cards
    cards_layer = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    cdraw = ImageDraw.Draw(cards_layer)
    
    # Central Card Frame
    card1 = [250, 180, 1670, 900]
    cdraw.rectangle(card1, fill=(17, 24, 39, 180), outline=(6, 182, 212, 120), width=2)
    
    # Inner Sub-cards
    cdraw.rectangle([300, 240, 920, 840], fill=(15, 23, 42, 150), outline=(99, 102, 241, 90), width=1)
    cdraw.rectangle([960, 240, 1620, 520], fill=(15, 23, 42, 150), outline=(6, 182, 212, 90), width=1)
    cdraw.rectangle([960, 560, 1620, 840], fill=(15, 23, 42, 150), outline=(59, 130, 246, 90), width=1)
    
    # Isometric Network Node Connections
    nodes = [
        (400, 350), (650, 300), (820, 480), (550, 650), (780, 720),
        (1050, 350), (1350, 300), (1500, 420), (1100, 680), (1420, 750)
    ]
    
    for i, (n1x, n1y) in enumerate(nodes):
        for j, (n2x, n2y) in enumerate(nodes):
            dist = math.hypot(n1x - n2x, n1y - n2y)
            if 0 < dist < 320:
                line_alpha = int(120 * (1 - dist / 320))
                cdraw.line([(n1x, n1y), (n2x, n2y)], fill=(6, 182, 212, line_alpha), width=2)
                
    for nx, ny in nodes:
        # Outer glow ring
        cdraw.ellipse([nx-12, ny-12, nx+12, ny+12], fill=(99, 102, 241, 80), outline=(6, 182, 212, 200), width=2)
        # Inner core
        cdraw.ellipse([nx-5, ny-5, nx+5, ny+5], fill=(255, 255, 255, 240))
        
    img = Image.alpha_composite(img, cards_layer)
    final_rgb = img.convert('RGB')
    
    path1 = os.path.join(ASSET_DIR, "01_hero_texture_keeper.png")
    final_rgb.save(path1, quality=95)
    shutil.copy(path1, os.path.join(BRAIN_DIR, "01_hero_texture_keeper.png"))
    print("Rendered HD 01_hero_texture_keeper.png")

# -------------------------------------------------------------
# 2. DELEGATION TEXTURE KEEPER (HD Render)
# -------------------------------------------------------------
def render_delegation_texture_keeper():
    W, H = 1920, 1080
    img = Image.new('RGBA', (W, H), (11, 15, 25, 255))
    
    draw = ImageDraw.Draw(img)
    
    # Ambient radial background
    glow = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    for r in range(800, 0, -6):
        alpha = int(45 * (1 - r / 800)**2)
        gd.ellipse([960-r, 540-r, 960+r, 540+r], fill=(6, 182, 212, alpha))
    img = Image.alpha_composite(img, glow)
    
    # Translucent glass container
    card = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    cd = ImageDraw.Draw(card)
    cd.rectangle([200, 150, 1720, 930], fill=(17, 24, 39, 210), outline=(6, 182, 212, 150), width=2)
    
    # Subtle internal grid
    for x in range(250, 1700, 80):
        cd.line([(x, 180), (x, 900)], fill=(255, 255, 255, 8), width=1)
    for y in range(200, 900, 80):
        cd.line([(220, y), (1700, y)], fill=(255, 255, 255, 8), width=1)
        
    # AI Delegation Network Flow Nodes (Left = User, Middle = Agent Router, Right = Execution Tools)
    user_node = (450, 540)
    router_node = (960, 540)
    tools = [(1470, 320), (1470, 540), (1470, 760)]
    
    # Connections User -> Router
    cd.line([user_node, router_node], fill=(6, 182, 212, 220), width=4)
    
    # Connections Router -> Tools
    for t in tools:
        cd.line([router_node, t], fill=(99, 102, 241, 200), width=3)
        
    # Draw Nodes
    for pt, label, col in [(user_node, "USER INPUT", (59, 130, 246)), (router_node, "AGENT ROUTER", (6, 182, 212))]:
        cd.ellipse([pt[0]-35, pt[1]-35, pt[0]+35, pt[1]+35], fill=(15, 23, 42, 240), outline=col, width=3)
        cd.ellipse([pt[0]-12, pt[1]-12, pt[0]+12, pt[1]+12], fill=col)
        
    for t in tools:
        cd.ellipse([t[0]-25, t[1]-25, t[0]+25, t[1]+25], fill=(15, 23, 42, 240), outline=(99, 102, 241), width=2)
        cd.ellipse([t[0]-8, t[1]-8, t[0]+8, t[1]+8], fill=(99, 102, 241))
        
    img = Image.alpha_composite(img, card)
    final_rgb = img.convert('RGB')
    
    path2 = os.path.join(ASSET_DIR, "07_delegation_texture_keeper.png")
    final_rgb.save(path2, quality=95)
    shutil.copy(path2, os.path.join(BRAIN_DIR, "07_delegation_texture_keeper.png"))
    print("Rendered HD 07_delegation_texture_keeper.png")

# -------------------------------------------------------------
# 3. CTA GLASS NODE KEEPER (HD 3D Isometric Cube Render)
# -------------------------------------------------------------
def render_cta_glass_node_keeper():
    W, H = 1080, 1080
    img = Image.new('RGBA', (W, H), (11, 15, 25, 255))
    
    # Radial Backdrop
    glow = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    for r in range(450, 0, -4):
        alpha = int(50 * (1 - r / 450)**2)
        gd.ellipse([540-r, 540-r, 540+r, 540+r], fill=(6, 182, 212, alpha))
    img = Image.alpha_composite(img, glow)
    
    # Draw 3D Isometric Glass Cube in Center
    cube = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    cd = ImageDraw.Draw(cube)
    
    cx, cy = 540, 500
    size = 220
    
    # 3D Isometric Coordinates
    # Top Face
    top_poly = [
        (cx, cy - size),
        (cx + int(size * 0.866), cy - int(size * 0.5)),
        (cx, cy),
        (cx - int(size * 0.866), cy - int(size * 0.5))
    ]
    
    # Left Face
    left_poly = [
        (cx - int(size * 0.866), cy - int(size * 0.5)),
        (cx, cy),
        (cx, cy + size),
        (cx - int(size * 0.866), cy + int(size * 0.5))
    ]
    
    # Right Face
    right_poly = [
        (cx, cy),
        (cx + int(size * 0.866), cy - int(size * 0.5)),
        (cx + int(size * 0.866), cy + int(size * 0.5)),
        (cx, cy + size)
    ]
    
    # Fill faces with translucent glass shades
    cd.polygon(top_poly, fill=(30, 41, 59, 230), outline=(6, 182, 212, 255), width=3)
    cd.polygon(left_poly, fill=(15, 23, 42, 230), outline=(99, 102, 241, 200), width=3)
    cd.polygon(right_poly, fill=(17, 24, 39, 230), outline=(6, 182, 212, 200), width=3)
    
    # Inner Glowing Core Node
    cd.ellipse([cx-24, cy-24, cx+24, cy+24], fill=(6, 182, 212, 240), outline=(255, 255, 255, 255), width=2)
    
    img = Image.alpha_composite(img, cube)
    final_rgb = img.convert('RGB')
    
    path3 = os.path.join(ASSET_DIR, "09_cta_glass_node_keeper.png")
    final_rgb.save(path3, quality=95)
    shutil.copy(path3, os.path.join(BRAIN_DIR, "09_cta_glass_node_keeper.png"))
    print("Rendered HD 09_cta_glass_node_keeper.png")

render_hero_texture_keeper()
render_delegation_texture_keeper()
render_cta_glass_node_keeper()

print("ALL 3 KEEPER IMAGES RENDERED IN ULTRA HIGH DEFINITION!")
