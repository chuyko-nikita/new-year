#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

import curses
import subprocess
import os
import random
import time
from itertools import cycle

FONT = {
    'А': [
        "  .o.  ",
        " .o.o. ",
        ".o...o.",
        ".ooooo.",
        ".o...o.",
        ".o...o.",
        ".o...o.",
    ],
    'Б': [
        ".ooooo.",
        ".o.....",
        ".o.....",
        ".oooo..",
        ".o...o.",
        ".o...o.",
        ".oooo..",
    ],
    'В': [
        ".oooo..",
        ".o...o.",
        ".o...o.",
        ".oooo..",
        ".o...o.",
        ".o...o.",
        ".oooo..",
    ],
    'Г': [
        ".ooooo.",
        ".o.....",
        ".o.....",
        ".o.....",
        ".o.....",
        ".o.....",
        ".o.....",
    ],
    'Д': [
        "..ooo..",
        ".o...o.",
        ".o...o.",
        ".o...o.",
        ".o...o.",
        ".ooooo.",
        "o.....o",
    ],
    'Е': [
        ".ooooo.",
        ".o.....",
        ".o.....",
        ".oooo..",
        ".o.....",
        ".o.....",
        ".ooooo.",
    ],
    'Ё': [
        "..o.o..",
        ".ooooo.",
        ".o.....",
        ".oooo..",
        ".o.....",
        ".o.....",
        ".ooooo.",
    ],
    'Ж': [
        "o..o..o",
        ".o.o.o.",
        "..ooo..",
        "..ooo..",
        ".o.o.o.",
        "o..o..o",
        "o..o..o",
    ],
    'З': [
        ".oooo..",
        ".....o.",
        ".....o.",
        "..ooo..",
        ".....o.",
        ".....o.",
        ".oooo..",
    ],
    'И': [
        ".o...o.",
        ".o...o.",
        ".o..oo.",
        ".o.o.o.",
        ".oo..o.",
        ".o...o.",
        ".o...o.",
    ],
    'Й': [
        "..o.o..",
        ".o...o.",
        ".o..oo.",
        ".o.o.o.",
        ".oo..o.",
        ".o...o.",
        ".o...o.",
    ],
    'К': [
        ".o...o.",
        ".o..o..",
        ".o.o...",
        ".oo....",
        ".o.o...",
        ".o..o..",
        ".o...o.",
    ],
    'Л': [
        "..oooo.",
        ".o...o.",
        ".o...o.",
        ".o...o.",
        ".o...o.",
        ".o...o.",
        "o....o.",
    ],
    'М': [
        ".o...o.",
        ".oo.oo.",
        ".o.o.o.",
        ".o.o.o.",
        ".o...o.",
        ".o...o.",
        ".o...o.",
    ],
    'Н': [
        ".o...o.",
        ".o...o.",
        ".o...o.",
        ".ooooo.",
        ".o...o.",
        ".o...o.",
        ".o...o.",
    ],
    'О': [
        "..ooo..",
        ".o...o.",
        ".o...o.",
        ".o...o.",
        ".o...o.",
        ".o...o.",
        "..ooo..",
    ],
    'П': [
        ".ooooo.",
        ".o...o.",
        ".o...o.",
        ".o...o.",
        ".o...o.",
        ".o...o.",
        ".o...o.",
    ],
    'Р': [
        ".oooo..",
        ".o...o.",
        ".o...o.",
        ".oooo..",
        ".o.....",
        ".o.....",
        ".o.....",
    ],
    'С': [
        "..oooo.",
        ".o.....",
        ".o.....",
        ".o.....",
        ".o.....",
        ".o.....",
        "..oooo.",
    ],
    'Т': [
        ".ooooo.",
        "...o...",
        "...o...",
        "...o...",
        "...o...",
        "...o...",
        "...o...",
    ],
    'У': [
        ".o...o.",
        ".o...o.",
        "..o.o..",
        "...o...",
        "...o...",
        "..o....",
        ".o.....",
    ],
    'Ф': [
        "...o...",
        ".ooooo.",
        "o..o..o",
        "o..o..o",
        ".ooooo.",
        "...o...",
        "...o...",
    ],
    'Х': [
        ".o...o.",
        "..o.o..",
        "...o...",
        "...o...",
        "...o...",
        "..o.o..",
        ".o...o.",
    ],
    'Ц': [
        ".o...o.",
        ".o...o.",
        ".o...o.",
        ".o...o.",
        ".o...o.",
        ".oooooo",
        "......o",
    ],
    'Ч': [
        ".o...o.",
        ".o...o.",
        ".o...o.",
        "..oooo.",
        ".....o.",
        ".....o.",
        ".....o.",
    ],
    'Ш': [
        "o..o..o",
        "o..o..o",
        "o..o..o",
        "o..o..o",
        "o..o..o",
        "o..o..o",
        ".ooooo.",
    ],
    'Щ': [
        "o..o..o",
        "o..o..o",
        "o..o..o",
        "o..o..o",
        "o..o..o",
        ".oooooo",
        "......o",
    ],
    'Ъ': [
        ".oo....",
        "..o....",
        "..o....",
        "..ooo..",
        "..o..o.",
        "..o..o.",
        "..ooo..",
    ],
    'Ы': [
        ".o...o.",
        ".o...o.",
        ".o...o.",
        ".oo..o.",
        ".o.o.o.",
        ".o.o.o.",
        ".oo..o.",
    ],
    'Ь': [
        ".o.....",
        ".o.....",
        ".o.....",
        ".ooo...",
        ".o..o..",
        ".o..o..",
        ".ooo...",
    ],
    'Э': [
        "..ooo..",
        ".....o.",
        ".....o.",
        "..oooo.",
        ".....o.",
        ".....o.",
        "..ooo..",
    ],
    'Ю': [
        ".o..oo.",
        ".o.o..o",
        ".o.o..o",
        ".ooo..o",
        ".o.o..o",
        ".o.o..o",
        ".o..oo.",
    ],
    'Я': [
        "..oooo.",
        ".o...o.",
        ".o...o.",
        "..oooo.",
        "...o.o.",
        "..o..o.",
        ".o...o.",
    ],
    ' ': [
        ".......",
        ".......",
        ".......",
        ".......",
        ".......",
        ".......",
        ".......",
    ],
    ',': [
        ".......",
        ".......",
        ".......",
        ".......",
        "...oo..",
        "...o...",
        "..o....",
    ],
    '-': [
        ".......",
        ".......",
        ".......",
        ".ooooo.",
        ".......",
        ".......",
        ".......",
    ],
}


def text_to_ascii(text):
    lines = [""] * 7
    for char in text.upper():
        if char in FONT:
            for i in range(7):
                lines[i] += FONT[char][i] + " "
        else:
            for i in range(7):
                lines[i] += "....... "
    return lines


# Ваши фразы
QUOTES = [
    ["А СНЕГ ИДЕТ", "ПО ЩЕКАМ МНЕ", "БЬЕТ БЬЕТ"],
    ["СВЕТЛАЯ БУДЕТ", "ПОЛОСА"],
    ["С НОВЫМ ГОДОМ", "КРОШКА"],
]


def compile_tree():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    c_file = os.path.join(script_dir, "tree.c")
    exe_file = os.path.join(script_dir, "tree")
    
    if not os.path.exists(c_file):
        return None, "tree.c not found"
    
    result = subprocess.run(
        ["cc", "-O3", "-o", exe_file, c_file, "-lm"],
        capture_output=True, text=True
    )
    
    if result.returncode != 0:
        return None, result.stderr
    
    return exe_file, None


def generate_tree(exe_file, depth=3, zoom=1.5):
    try:
        result = subprocess.run(
            [exe_file, str(depth), str(zoom)],
            capture_output=True, text=True,
            timeout=30
        )
        return result.stdout
    except subprocess.TimeoutExpired:
        return ""


def parse_tree(tree_str):
    lines = tree_str.split('\n')
    buffer = []
    light_positions = []
    
    for row_idx, line in enumerate(lines):
        if not line:
            continue
        row = []
        for col_idx, char in enumerate(line):
            if char in '#o&j':
                light_positions.append((row_idx, col_idx))
                row.append(('light', char))
            elif char == '=':
                row.append(('ribbon', char))
            elif char == '.':
                row.append(('tree', char))
            elif char == ' ':
                row.append(('empty', ' '))
            else:
                row.append(('tree', char))
        buffer.append(row)
    
    return buffer, light_positions


def init_colors():
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_GREEN, -1)
    curses.init_pair(2, curses.COLOR_YELLOW, -1)
    curses.init_pair(3, curses.COLOR_RED, -1)
    curses.init_pair(4, curses.COLOR_CYAN, -1)
    curses.init_pair(5, curses.COLOR_MAGENTA, -1)
    curses.init_pair(6, curses.COLOR_WHITE, -1)
    curses.init_pair(7, 240, -1) if curses.COLORS > 16 else curses.init_pair(7, 8, -1)


def draw_tree(stdscr, buffer, start_y, start_x, active_lights):
    for row_idx, row in enumerate(buffer):
        y = start_y + row_idx
        for col_idx, (cell_type, char) in enumerate(row):
            x = start_x + col_idx
            try:
                if cell_type == 'empty':
                    continue
                elif cell_type == 'ribbon':
                    stdscr.addstr(y, x, '=', curses.color_pair(6) | curses.A_BOLD)
                elif cell_type == 'light':
                    pos_key = (row_idx, col_idx)
                    if pos_key in active_lights:
                        stdscr.addstr(y, x, 'o', curses.color_pair(active_lights[pos_key]) | curses.A_BOLD)
                    else:
                        stdscr.addstr(y, x, char, curses.color_pair(1))
                else:
                    stdscr.addstr(y, x, char, curses.color_pair(1))
            except curses.error:
                pass


def draw_big_quote(stdscr, quote_lines, center_y, left_margin, max_width):
    start_x = left_margin
    
    all_lines = []
    for text in quote_lines:
        ascii_lines = text_to_ascii(text)
        all_lines.extend(ascii_lines)
        all_lines.append("")
    
    total_height = len(all_lines)
    start_y = center_y - total_height // 2
    
    try:
        for i, line in enumerate(all_lines):
            y = start_y + i
            visible_line = line[:max_width - left_margin - 2]
            clean_line = visible_line.replace('.', ' ').replace('o', '█')
            stdscr.addstr(y, start_x, clean_line, curses.color_pair(6) | curses.A_BOLD)
        
        subtitle_y = start_y + total_height + 2
        subtitle = "—  в с ё   с б у д е т с я"
        stdscr.addstr(subtitle_y, start_x, subtitle, curses.color_pair(6) | curses.A_BOLD)
    except curses.error:
        pass


def draw_snowflakes(stdscr, snowflakes, height, width):
    new_snowflakes = []
    for x, y, speed in snowflakes:
        y += speed
        if y < height - 1:
            new_snowflakes.append((x, y, speed))
            try:
                stdscr.addstr(int(y), int(x), '.', curses.color_pair(7))
            except curses.error:
                pass
    if random.random() < 0.25:
        new_snowflakes.append((random.randint(0, max(1, width - 2)), 0, random.uniform(0.1, 0.25)))
    return new_snowflakes


def main(stdscr):
    try:
        curses.curs_set(0)
    except:
        pass
    stdscr.nodelay(True)
    stdscr.timeout(100)
    curses.mousemask(0)
    init_colors()
    
    height, width = stdscr.getmaxyx()
    
    stdscr.addstr(height // 2, width // 2 - 10, "Compiling...", curses.color_pair(6))
    stdscr.refresh()
    
    exe_file, error = compile_tree()
    if error:
        stdscr.addstr(height // 2 + 1, 2, f"Error: {error}", curses.color_pair(3))
        stdscr.refresh()
        time.sleep(3)
        return
    
    stdscr.addstr(height // 2, width // 2 - 10, "Generating...", curses.color_pair(6))
    stdscr.refresh()
    
    tree_str = generate_tree(exe_file, depth=3, zoom=1.5)
    buffer, light_positions = parse_tree(tree_str)
    
    if not buffer:
        stdscr.addstr(height // 2 + 1, 2, "Failed to generate tree", curses.color_pair(3))
        stdscr.refresh()
        time.sleep(3)
        return
    
    tree_height = len(buffer)
    tree_width = max(len(row) for row in buffer) if buffer else 0
    
    frame = 0
    snowflakes = []
    quote_cycle = cycle(QUOTES)
    current_quote = next(quote_cycle)
    quote_timer = 0
    active_lights = {}
    
    light_spots = random.sample(light_positions, min(100, len(light_positions))) if light_positions else []
    
    while True:
        try:
            key = stdscr.getch()
            if key in [ord('q'), ord('Q'), 27]:
                break
            
            height, width = stdscr.getmaxyx()
            stdscr.clear()
            
            left_area = width // 2
            right_margin = (width - left_area - tree_width) // 2
            tree_x = left_area + right_margin
            tree_y = max(1, (height - tree_height) // 2)
            left_margin = right_margin
            
            if frame % 20 == 0 and light_spots:
                spot = random.choice(light_spots)
                if spot in active_lights:
                    del active_lights[spot]
                else:
                    active_lights[spot] = random.choice([2, 3, 4, 5])
                while len(active_lights) > 15:
                    del active_lights[random.choice(list(active_lights.keys()))]
            
            snowflakes = draw_snowflakes(stdscr, snowflakes, height, width)
            draw_big_quote(stdscr, current_quote, height // 2, left_margin, left_area)
            
            quote_timer += 1
            if quote_timer > 50:
                quote_timer = 0
                current_quote = next(quote_cycle)
            
            draw_tree(stdscr, buffer, tree_y, tree_x, active_lights)
            
            stdscr.refresh()
            frame += 1
            time.sleep(0.1)
        except KeyboardInterrupt:
            break
        except curses.error:
            pass


if __name__ == '__main__':
    curses.wrapper(main)
