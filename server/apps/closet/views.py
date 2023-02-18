from django.shortcuts import render, redirect, get_object_or_404
from server.apps.main.models import *
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, UpdateView
from django.views.decorators.http import require_POST
from itertools import chain
from django.utils.datastructures import MultiValueDictKeyError
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
from GoogleSearch import Search
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Create your views here.
# REVIEW : mysql 파일 삭제 요망
def closet_main(request, *args, **kwargs):
  clothes_list = Clothes.objects.filter(author=request.user)
  context = {
    'clothes_list': clothes_list,
  }
  return render(request,'closet/closet_main.html', context=context)

def closet_all(request, *args, **kwargs):
  post_list = Post.objects.filter(author=request.user) 
  context={
      'post_list':post_list,
  }   
  return render(request,'closet/closet_main.html',context=context)

# def clothes_list(request, Clothes, *args, **kwargs):
#   clothes_mapping = {
#     'top': Top,
#     'bottom': Bottom,
#     'outer': Outer,
#     'shoes': Shoes,
#     'acc': Acc,
#   }
#   clothes_list = clothes_mapping.get(Clothes).objects.filter(author=request.user)
#   context={
#     'clothes_list': clothes_list,
#     }   
#   return render(request,'closet/closet_main.html',context=context)
  
def outer_list(request, *args, **kwargs):
  clothes_list = Outer.objects.filter(author=request.user)
  context={
    'clothes_list': clothes_list,
  }   
  return render(request,'closet/closet_main.html',context=context)

def top_list(request, *args, **kwargs):
  clothes_list = Top.objects.filter(author=request.user)
  context={
    'clothes_list': clothes_list,
  }   
  return render(request,'closet/closet_main.html',context=context)

def bottom_list(request, *args, **kwargs):
  clothes_list = Bottom.objects.filter(author=request.user)
  context={
    'clothes_list': clothes_list,
  }   
  return render(request,'closet/closet_main.html',context=context)

def shoes_list(request, *args, **kwargs):
  clothes_list = Shoes.objects.filter(author=request.user)
  context={
    'clothes_list': clothes_list,
  }   
  return render(request,'closet/closet_main.html',context=context)

def acc_list(request, *args, **kwargs):
  clothes_list = Acc.objects.filter(author=request.user)
  context={
    'clothes_list': clothes_list,
  }   
  return render(request,'closet/closet_main.html',context=context)

def our_closet(request, *args, **kwargs):  
  # sort = request.GET.get('sort','')
  
  # if sort == 'new':
  #   post_list = Post.objects.filter(open=True).order_by("-pk")
  # elif sort == 'old':
  #   post_list = Post.objects.filter(open=True).order_by("pk")
  # elif sort == 'like':
  #   post_list = Post.objects.filter(open=True).order_by("")
  # else:
  #   post_list = Post.objects.filter(open=True).order_by("-pk")
    
  # page = request.GET.get('page', 1)
  # paginator = Paginator(post_li, 4)
  
  # try:
  #   posts = paginator.page(page)
  # except PageNotAnInteger:
  #   posts = paginator.page(1)
  # except EmptyPage:
  #   posts = paginator.page(paginator.num_pages)
  post_list = Post.objects.filter(open=True).order_by("-pk")

  context={
      'post_list' : post_list,
      }
  return render(request,'closet/our_closet.html',context=context)

def create_clothes(request, *args, **kwargs):
  error = '아직 입력하지 않은 값이 있습니다.'
  context={
    'error' : error,
    }
  if request.method == "POST":
    try:
      clothes = request.POST["clothes"]
    except MultiValueDictKeyError:
      return render(request, "closet/clothes_create.html", context=context) 
    if clothes == 'top':
      kind = Top
    elif clothes == 'bottom':
      kind = Bottom
    elif clothes == 'outer':
      kind = Outer
    elif clothes == 'shoes':
      kind = Shoes
    elif clothes == 'acc':
      kind = Acc
    author = request.user
    kind.objects.create(
      title=request.POST["title"],
      img=request.FILES["image"],
      buying=request.POST["buying"],
      author=author,
    )
    return redirect('closet:closet_main')
  return render(request, "closet/clothes_create.html") 

@csrf_exempt
def clothes_likes(request, pk, *args, **kwargs):
  user = request.user
  if user.is_authenticated:
    req = json.loads(request.body)
    clothes = get_object_or_404(Clothes, pk=pk)
    clothes_id = req['id']
    btnType = req['btnType']
    imgUrl = req['imgUrl']
    if btnType == 'like':
      clothes.likes.add(user)
    else:
      clothes.likes.remove(user)
    context = {'id' : clothes_id, 'btnType': btnType, 'imgUrl':imgUrl}
    return JsonResponse(context)
  # if request.user.is_authenticated:
  #   clothes = get_object_or_404(Clothes, pk=pk)
  #   users = clothes.likes.all()
  #   if users.filter(pk=request.user.pk).exists():
  #     clothes.likes.remove(request.user)
  #   else:
  #     clothes.likes.add(request.user)
  #   return redirect('closet:closet_main')
  #   # return redirect('accouts:login')위에거 대신 이거 떠야함! 나중에 로그인 합치고!!
  # return render(request, 'closet/our_closet.html')
  

def clothes_like_list(request, *args, **kwargs):
  user = User.objects.get(username=request.user)
  clothes_list = Clothes.objects.filter(likes=user)
  context={
    'clothes_list': clothes_list,
    'buylink_flag' : True,
  }   
  return render(request,'closet/closet_main.html',context=context)
  
def post_like_list(request, *args, **kwargs):
  user = User.objects.get(username=request.user)
  post_list = Post.objects.filter(likes=user)
  context={
    'post_list': post_list,
  }   
  return render(request,'closet/closet_main.html',context=context)
  
def buylink(request, pk, *args, **kwargs):
  cloth = Clothes.objects.filter(id=pk)
  context = {
    'cloth' : cloth[0],
    'fastflag' : False,
    'exactflag' : False,
  }
  if request.method == "POST":
    print(request.POST)
    choice = list(request.POST.values())[-1]

    if choice == '빠른 검색':
      output = Search(file_path=cloth[0].img.path)
      link = output['similar']
      context['link']=link
      context['fastflag'] = True
    elif choice == '정확한 검색':
      options = Options()
      options.add_argument('--headless')
      options.add_argument("window-size=1400,850")
      driver = webdriver.Chrome('/usr/local/bin/chromedriver',options=options)
      driver.get('http://www.google.hr/imghp')
      driver.implicitly_wait(10)
      elem = driver.find_element(By.CLASS_NAME, 'Gdd5U')
      elem.click()
      driver.find_element(By.NAME, 'encoded_image').send_keys(cloth[0].img.path)
      # items = driver.find_element(By.CSS_SELECTOR, 'div.Vd9M6.abDdKd.xuQ19b')
      titles_finder = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'div.Vd9M6.abDdKd.xuQ19b')))
      
      search_informations_list = []
      for num, title in enumerate(titles_finder):
        search_info_list = []
        text_info = title.text.split('\n')
        for element in text_info:
          if '₩' in element:
            search_info_list.append(element)
            break
        else:
          search_info_list.append('가격정보없음')
          
        a_tag_finder = title.find_element(By.XPATH, ".//a")
        img_tag_finder = a_tag_finder.find_element(By.XPATH, ".//div[1]/div[1]/div[1]/img")
        exact_url = a_tag_finder.get_dom_attribute('href')
        exact_src = img_tag_finder.get_dom_attribute('src')
        
        search_info_list.append(exact_url)
        search_info_list.append(exact_src)
        search_informations_list.append(search_info_list)
        #리스트 요소는 각각 리스트 : [가격, 구매링크, 이미지src] 로 구성되어있음
        if num >= 3:
          break
      context['search_informations_list']=search_informations_list
      context['exactflag'] = True
  return render(request,'closet/buylink.html', context=context)