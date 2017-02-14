import SimpleGUICS2Pygame.simpleguics2pygame as GUI

DEPTH = 5


def fractal(canvas, center, radius, depth, const):

    canvas.draw_circle(center, radius, 2, 'blue')

    if depth < DEPTH:
        fractal(canvas, (center[0] - const / 3, center[1]), radius / 2.5, depth + 1, const / 3)
        fractal(canvas, (center[0], center[1] - const / 3), radius / 2.5, depth + 1, const / 3)
        fractal(canvas, (center[0] + const / 3, center[1]), radius / 2.5, depth + 1, const / 3)
        fractal(canvas, (center[0], center[1] + const / 3), radius / 2.5, depth + 1, const / 3)


def draw(canvas):
    fractal(canvas, (250, 250), 40, 0, 300)

frame = GUI.create_frame("Frame", 500, 500)
frame.set_draw_handler(draw)
frame.start()
