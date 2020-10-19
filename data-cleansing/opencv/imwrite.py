import numpy as np
import cv2

# 画像のサイズを決める
img_size = (512, 512)

# サイズが512 × 512の緑色の画像を作ってください
image = np.array([
        [[0, 255, 0] for _ in range(img_size[1])]
            for _ in range(img_size[0])
    ])

# 作成した画像を表示してください
image = cv2.imshow('image', image)

# 画像をファイル名"my_green_img.jpg"で保存してください
cv2.imwrite('my_green_img.jpg', image)