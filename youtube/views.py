from django.shortcuts import render, redirect
from pytube import *
from django.views.generic import View 

class home(View):
    def __init__(self,url=None):
        self.url = url
    def get(self,request):
        return render(request,'youtube/youtube.html')
    def post(self,request):
        # for fetching the video
        if request.POST.get('fetch-vid'):
            self.url = request.POST.get('given_url')
            video = YouTube(self.url)
            print(video)
            vidTitle,vidThumbnail = video.title,video.thumbnail_url
            qual,stream = [],[]
            for vid in video.streams.filter(progressive=True):
                qual.append(vid.resolution)
                stream.append(vid)
            print(stream)
            context = {'vidTitle':vidTitle,'vidThumbnail':vidThumbnail,
                        'qual':qual,'stream':stream,
                        'url':self.url}
            return render(request,'youtube/youtube.html',context)

        # for downloading the video
        elif request.POST.get('download-vid'):
            self.url = request.POST.get('given_url')
            video = YouTube(self.url)
            stream = [x for x in video.streams.filter(progressive=True)]
            video_qual = video.streams[int(request.POST.get('download-vid')) - 1]
            video_qual.download(filename="Downloads")
            return redirect('home')

        return render(request,'youtube/youtube.html')









# # defining function
# def youtube(request):
  
#     # checking whether request.method is post or not
#     if request.method == 'POST':
        
#         # getting link from frontend
#         link = request.POST['link']
#         video = YouTube(link)
  
#         # setting video resolution
#         stream = video.streams.get_highest_resolution()
          
#         # downloads video
#         stream.download()
  
#         # returning HTML page
#         return render(request, 'youtube/youtube.html')
#     return render(request, 'youtube/youtube.html')