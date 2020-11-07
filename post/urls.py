from django.conf.urls import url
from . import views
 
urlpatterns = [
    url(r'(?P<pk>[0-9]+)/', views.PostDetail.as_view(), name='detail'),
    url(r'', views.PostList.as_view(), name='posts')
]
#<script type="syntaxhighlighter" class="brush: python"><![CDATA[]]></script><p></p>
#<p style="line-height: 2;"><span style="font-size: 12pt;">다음으로 장고 프로젝트 URL에 post 앱 url을 추가합니다.</span></p>

from django.conf.urls import url, include
from django.contrib import admin
 
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'post/', include('post.urls')),
]



