# ipark_django

고려대 세종캠퍼스 교내 헬스장(Ipark) 출입 어플(https://github.com/mingyu3619/iParkiOS)
의 관리자 페이지입니다.

# 목차

+ 설치
+ Table 
+ 주요 기능
  + Covid Record,Live Data 
    + task schedule with pythonanywhere   
  + member Data
    + import file(excel)
    + image upload

# 설치

```
git clone https://github.com/mingyu3619/ipark_django.git
pip install -r requirements.txt
```

# 테이블

|테이블 이름 | 기능 |  속성 | 
|:----:|:----:|:----:|
|   Covid Record|   출입기록 저장    |  이름,출입시간, id(AutoField)...      |
|   Live Data        |   실시간 이용자 수 조회    | 이름,입장시간,예약상품 ...      |
|  Member Data        | 모든 회원 정보 저장, 회원식별에 사용      | **이메일(key)** , 이름,학번,이미지,예약상품 ...      |
|Notice        |  공지사항 공지     |    제목,내용,이미지   |
|   Lost_Found        |   분실물 공지    |     제목,내용,이미지  |
|   Complain        |   불편사항 접수 (미완성)    |    제목,내용,이미지   |

# 주요기능

+ Covid Record,Live Data : react natvie 어플을 통해 출입 과정 중 fetch(get,post,delete)
  + task schedule with pythonanywhere: 2시간에 한번 퇴장 QR 미인식자 삭제(pythonanywhere 의 Task 사용,schedule_liveData.py)  
+ member Data
  + import file(excel): 대용량 회원정보 django의 import_export 모듈을 이용해 Upload 
  
    + ![image](https://user-images.githubusercontent.com/86222639/154404450-28356dd4-af78-422e-ac65-be9d29f14310.png)

  + image upload:  
    + 이미지 업로드 후, member Data의 key와 같은 파일명을 update.
    +  django form , django admin 내에 upload.html url 커스텀
    + ipark_django/ido/views.py
    ```python
    def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        files = request.FILES.getlist('image')
        if form.is_valid():
            for f in files:
                email = f.name.split(".")[0]
                try:
                    instance = memberData.objects.get(email=email)
                    instance.image = f
                    instance.save()
                except memberData.DoesNotExist:
                    pass
                    # file_instance = memberData(name=f,email=f,image=f)
                # file_instance.save()

            return HttpResponse('upload success')
        else:
            return HttpResponse('bad')
    else:
        form = UploadFileForm()
    return render(request, 'image_upload.html', {'form': form})
    ```
    
     ![image](https://user-images.githubusercontent.com/86222639/154404932-ebc678ce-0f6c-4d80-9464-c3b1ce05407a.png)  
     
# 기술 스택
+ django
+ django admin
+ django form
+ react fetch
+ html
+ django restframework
