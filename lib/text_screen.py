import pygame

def text_screen(title, description):

    # Initialize Pygame
    pygame.init()

    # Get the screen width and height
    screen_info = pygame.display.Info()
    screen_width = screen_info.current_w
    screen_height = screen_info.current_h

    # Open a fullscreen window
    window = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)

    # Hide the mouse cursor
    pygame.mouse.set_visible(False)

    # Set the background color
    background_color = (0, 0, 0)  # Black

    # Set text parameters
    title_font_size = 50
    font_size = 30
    title_font = pygame.font.Font(None, title_font_size)
    font = pygame.font.Font(None, font_size)
    font_color = (192, 192, 192)  # Gray

    # Define the text content

    # Create a list to store text surfaces and their respective rectangles
    text_surfaces = []
    text_rects = []

    # Calculate the position of each text
    text_x = screen_width // 2
    line_spacing = 40
    text_y = (screen_height // 2) - 50

    # Render and position the text
    title_surface = title_font.render(title, True, font_color)
    title_rect = title_surface.get_rect(center=(text_x, text_y))
    text_surfaces.append(title_surface)
    text_rects.append(title_rect)
    text_y += line_spacing

    description_surface = font.render(description, True, font_color)
    description_rect = description_surface.get_rect(center=(text_x, text_y))
    text_surfaces.append(description_surface)
    text_rects.append(description_rect)
    text_y += line_spacing

    info = 'Bitte drücken Sie "ESC" um zurückzukehren'
    info_surface = font.render(info, True, font_color)
    info_rect = info_surface.get_rect(center=(text_x, screen_height - 250))
    text_surfaces.append(info_surface)
    text_rects.append(info_rect)

    # Create a fixation cross surface
    cross_size = 70
    cross_surface = pygame.Surface((cross_size, cross_size), pygame.SRCALPHA)
    pygame.draw.line(cross_surface, (255, 255, 255), (cross_size // 2, 0), (cross_size // 2, cross_size), 5)
    pygame.draw.line(cross_surface, (255, 255, 255), (0, cross_size // 2), (cross_size, cross_size // 2), 5)
    cross_rect = cross_surface.get_rect(center=(screen_width // 2, screen_height // 2))

    # Main loop
    running = True
    while running:
        # Clear the screen
        window.fill(background_color)

        # Render and display the text
        for i in range(len(text_surfaces)):
            window.blit(text_surfaces[i], text_rects[i])

        # Update the display
        pygame.display.flip()

        # Process events
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a or pygame.K_ESCAPE:
                    running = False

    # Show the mouse cursor
    pygame.mouse.set_visible(True)

    # Close the window
    return
