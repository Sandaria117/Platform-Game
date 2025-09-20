# Platform-Game

<img width="800" alt="screenshot" src="https://github.com/user-attachments/assets/5b9abe6e-3191-47b1-9a2a-f1b463b879e4" />

## Tổng quan
**Platform-Game** là một trò chơi platform 2D được phát triển bằng **Python** sử dụng thư viện **Pygame**.  
Người chơi sẽ điều khiển nhân vật di chuyển trên bản đồ, nhảy qua chướng ngại vật, thu thập vật phẩm và vượt qua các màn chơi được thiết kế sẵn.

---

## Công nghệ sử dụng
-  **Python**  
-  **Pygame** để xây dựng gameplay, xử lý nhân vật và va chạm  
-  **Tiled Map Editor** để thiết kế bản đồ  
-  **PyTMX** để load map `.tmx` từ Tiled vào game  

---

## Cách setup & chạy game
1. Cài đặt thư viện cần thiết:
   ```bash
   pip install pygame
   pip install pytmx
2. Clone re
- git clone https://github.com/Sandaria117/Platform-Game.git
- cd Platform-Game
3. Chạy Game
- python code/main.py

---

## Cách chơi
- Di chuyển theo mũi tên, tấn công bằng Q
- Mục tiêu: Hoàn thành màn chơi bằng việc thu thập coin, hạ gục quái để đủ điểm yêu cầu
