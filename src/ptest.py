from simple_image_download import simple_image_download as simp

response = simp.simple_image_download

# response().download('bear', 5, image_directory = 'test_dir')
response().download("Breaking news! Russian customs officials said they had detained a star American basketball player after finding hashish oil in her luggage at an airport near Moscow. The Russian news agency has identified the player as Brittney Griner.", 5)

print(response().urls('bear', 5))