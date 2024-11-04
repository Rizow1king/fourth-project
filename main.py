# # Multiprocessing
# import time
# import multiprocessing
#
#
# def generate_number():
#     for i in range(1, 11):
#         print(i)
#         time.sleep(1)
#
#
# if __name__ == '__main__':
#     start = time.time()
#     pr1 = multiprocessing.Process(target=generate_number)
#     pr2 = multiprocessing.Process(target=generate_number)
#     pr3 = multiprocessing.Process(target=generate_number)
#     pr1.start()
#     pr2.start()
#     pr3.start()
#     pr1.join()
#     pr2.join()
#     pr3.join()
#     end = time.time()
#     print(f"dastur ishlashiga ketgan vaqt: {round(end - start)}")
# ---------------------------------------------------------------------------------------
# import time
# import multiprocessing
#
#
# def generate_number():
#     for i in range(1, 11):
#         print(i)
#         time.sleep(0.0000000001)
#
#
# if __name__ == '__main__':
#     start = time.time()
#     processes = []
#     for i in range(30):
#         pr = multiprocessing.Process(target=generate_number)
#         pr.start()
#         pr.join()
#         processes.append(i)
#     end = time.time()
#     print(f"dastur ishlashiga ketgan vaqt: {round(end - start, 2)}")
# --------------------------------------------------------------------------
# import time
# import requests
# import multiprocessing
#
#
# img_urls = [
#    'https://images.unsplash.com/photo-1516117172878-fd2c41f4a759',
#    'https://images.unsplash.com/photo-1532009324734-20a7a5813719',
#    'https://images.unsplash.com/photo-1524429656589-6633a470097c',
#    'https://images.unsplash.com/photo-1530224264768-7ff8c1789d79',
#    'https://images.unsplash.com/photo-1564135624576-c5c88640f235',
#    'https://images.unsplash.com/photo-1541698444083-023c97d3f4b6',
#    'https://images.unsplash.com/photo-1522364723953-452d3431c267',
#    'https://images.unsplash.com/photo-1513938709626-033611b8cc03',
#    'https://images.unsplash.com/photo-1507143550189-fed454f93097',
#    'https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e',
#    'https://images.unsplash.com/photo-1504198453319-5ce911bafcde',
#    'https://images.unsplash.com/photo-1530122037265-a5f1f91d3b99',
#    'https://images.unsplash.com/photo-1516972810927-80185027ca84',
#    'https://images.unsplash.com/photo-1550439062-609e1531270e',
#    'https://images.unsplash.com/photo-1549692520-acc6669e2f0c'
# ]
#
#
# def download_image(image_url: str, queue: multiprocessing.Queue):
#     print(multiprocessing.current_process())
#     image_name = image_url.split("/")[-1] + ".jpg"
#     request = requests.get(image_url)
#     if request.status_code == 200:
#         data = request.content
#         with open(f"images/{image_name}", mode="wb") as file:
#             file.write(data)
#         queue.put(f"{image_name} yuklandi✅")
#     else:
#         queue.put("Qandaydir hatolik ketdi!!!")
#
#
# if __name__ == '__main__':
#     start = time.time()
#
#     queue = multiprocessing.Queue()
#     processes = []
#     i = 0
#     for image_url in img_urls:
#         pr = multiprocessing.Process(target=download_image, args=(image_url, queue), name=f"Pr-{i}")
#         pr.start()
#         i += 1
#         processes.append(pr)
#
#     for pr in processes:
#         pr.join()
#
#     while not queue.empty():
#         print(queue.get())
#
#     end = time.time()
#
#     print(f"Dastur ishlashi uchun {round(end-start, 2)} secund vaqt ketdi!")

# ---------------------------------------------------------------------------------
# import time
# from collections import futures
#
# def generate_number():
#     for i in range(1, 11):
#         print(i)
#         time.sleep(1)
#
#
# if __name__ == '__main__':
#     start = time.time()
#     with
#     end = time.time()
# -----------------------------------------------------------
# import requests
# import time
# import multiprocessing
# from concurrent import futures
#
#
# img_urls = [
#    'https://images.unsplash.com/photo-1516117172878-fd2c41f4a759',
#    'https://images.unsplash.com/photo-1532009324734-20a7a5813719',
#    'https://images.unsplash.com/photo-1524429656589-6633a470097c',
#    'https://images.unsplash.com/photo-1530224264768-7ff8c1789d79',
#    'https://images.unsplash.com/photo-1564135624576-c5c88640f235',
#    'https://images.unsplash.com/photo-1541698444083-023c97d3f4b6',
#    'https://images.unsplash.com/photo-1522364723953-452d3431c267',
#    'https://images.unsplash.com/photo-1513938709626-033611b8cc03',
#    'https://images.unsplash.com/photo-1507143550189-fed454f93097',
#    'https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e',
#    'https://images.unsplash.com/photo-1504198453319-5ce911bafcde',
#    'https://images.unsplash.com/photo-1530122037265-a5f1f91d3b99',
#    'https://images.unsplash.com/photo-1516972810927-80185027ca84',
#    'https://images.unsplash.com/photo-1550439062-609e1531270e',
#    'https://images.unsplash.com/photo-1549692520-acc6669e2f0c'
# ]
#
#
# def download_image(image_url: str):
#     print(multiprocessing.current_process())
#     image_name = image_url.split("/")[-1] + ".jpg"
#     request = requests.get(image_url)
#     if request.status_code == 200:
#         data = request.content
#         with open(f"images/{image_name}", mode="wb") as file:
#             file.write(data)
#         return f"{image_name} yuklandi✅"
#     else:
#         return "Qandaydir hatolik ketdi!!!"
#
#
# if __name__ == '__main__':
#     start = time.time()
#
#     with futures.ProcessPoolExecutor() as executor:
#         res = executor.map(download_image, img_urls)
#     print(list(res))
#
#     end = time.time()
#
#     print(f"Dastur ishlashi uchun {round(end-start, 2)} secund vaqt ketdi!")
# --------------Dict--------------------
# 1---------
# print({ })
# 2-----------------
# my_dict = {"name": "Muhammadrizo"}
# print(my_dict.values())
# 3-----------------
# my_dict = {"name": "Muhammadrizo", "age": 14}
# print(my_dict.values())
# 4-------------------
# my_dict = {"name": "Muhammadrizo", "age": 14}
# print(list(my_dict.values()))
# 5------------------
# my_dict = {"name": "Muhammadrizo", "age": 14}
# print(list(my_dict.items()))
# 6----------------------
# my_dict = {"name": "Muhammadrizo", "age": 14}
# my_dict.pop("name")
#
# print(my_dict)
# 7------------------
# my_dict = {"name": "Muhammadrizo", "age": 14}
# print(list(my_dict.items()))
# 8------------------
# my_dict = {"name": "Muhammadrizo", "age": 14}
# my_dict.clear()
#
# print(my_dict)
# 9--------------------------
# my_dict = {"name": "Muhammadrizo", "age": 14}
# for i in my_dict.values():
#     if i == "name":
#         print("Bu kalit soz bor")
#     else:
#         print("Bu kalit soz yoq!!")
# 10-----------------------------------------
# my_dict = {"name": "Muhammadrizo", "age": 14, "lastname": "Tokhtashev"}
# print(my_dict.copy())
# 11-----------------------------------------
