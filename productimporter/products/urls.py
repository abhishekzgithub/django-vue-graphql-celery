from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'^$',views.product_form_view,name="productform"),
    url(r'^upload/$',views.upload_files_view,name="upload_files_view"),
    url(r'^show/$',views.show_files_view,name="show_files_view"),
    url(r'^deletedata/$',views.drop_product_data_view,name="drop_product_data_view"),
    url(r'^search/$',views.search_product,name="search_product"),
    url(r'^get_csv_view/$',views.get_csv_view,name="get_csv_view"),
]