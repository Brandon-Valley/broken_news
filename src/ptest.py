from simple_image_download import simple_image_download as simp

response = simp.simple_image_download

response().download('bear', 5, image_directory = 'test_dir')

print(response().urls('bear', 5))