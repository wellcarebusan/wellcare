from django.urls import path
from . import views
from django.http import HttpResponse

urlpatterns = [
    ################ 회사소개 ##############
    path('', views.index, name='index'),
    path('intro/greeting', views.greeting, name='greeting'),
    path('intro/status', views.status, name='status'),
    path('intro/way', views.way, name='way'),
    ################ 장기요양보험 ##############
    path('longterm/insurance', views.insurance, name='insurance'),
    path('longterm/procedure', views.procedure, name='procedure'),
    path('longterm/enroll', views.enroll, name='enroll'),
    ################ 방문서비스 ##############
    path('homecare', views.homecare, name='homecare'),
    path('homecare/wash', views.wash, name='wash'),
    ################ 중산층 ##############
    path('classcare', views.classcare, name='classcare'),
    ################ 24t시간돌봄 ##############
    path('allday', views.allday, name='allday'),
    ################ 요양복지사 모집 ##############
    path('hirement', views.hirement, name='hirement'),
    path('hirement/delete/<int:delete_employee_id>', views.employee_delete, name='employee_delete'),
    path('2fjnklfqsr4dasf3v4rf32/13/fa3553/142/klafd/1/afa/23/dd45b/12313/bfd/s2/<int:detail_employee_id>/12/51/adfdfasf4efada4rafd32agd', views.employee_detail, name='employee_detail'),
    ###robot###
    path('robots.txt/', lambda x: HttpResponse("User-Agent: Yeti\n Allow:/", content_type="text/plain")),
]
