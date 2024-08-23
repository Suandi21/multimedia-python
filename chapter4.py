import pygame # type: ignore
pygame.init()


# Mengatur tampilan
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("images (2).png")

# Memuat gambar
image = pygame.image.load('images (2).png')

# Memuat suara
sound = pygame.mixer.Sound('The Drum.mp3')

# Memutar suara
sound.play()

# Loop utama permainan dengan animasi
x = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Memperbarui posisi
    x += 5
    if x > 800:
        x = 0

    # Menggambar gambar di posisi baru
    screen.fill((0, 0, 0))  # Membersihkan layar dengan warna hitam
    screen.blit(image, (x, 100))

    # Memperbarui tampilan
    pygame.display.flip()

pygame.quit()