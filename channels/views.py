from channels.models import Channel
from django.shortcuts import render
# from django.views.decorators import gzip
# from django.http import StreamingHttpResponse
# import cv2
# import threading


def home(request):
    channels = Channel.objects.all()
    return render(request, "channels/channels_list.html", {"channels": channels})


def channel(request):
    pass


# class VideoCamera(object):

#     """Stream View"""

#     def __init__(self):
#         self.video = cv2.VideoCapture(0)
#         (self.grabbed, self.frame) = self.video.read()
#         threading.Thread(target=self.update, args=()).start()

#     def __del__(self):
#         self.video.release()

#     def get_frame(self):
#         image = self.frame
#         _, jpeg = cv2.imencode(".jpg", image)
#         return jpeg.tobytes()

#     def update(self):
#         while True:
#             (self.grabbed, self.frame) = self.video.read()


# def gen(camera):
#     while True:
#         frame = camera.get_frame()
#         yield (b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n\r\n")


# @gzip.gzip_page
# def channel(request):
#     try:
#         cam = VideoCamera()
#         return StreamingHttpResponse(
#             gen(cam), content_type="multipart/x-mixed-replace;boundary=frame"
#         )
#     except:  # This is bad! replace it with proper handling
#         print("에러입니다...")
#         pass
