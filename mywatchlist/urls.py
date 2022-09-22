from django.urls import path
from Tugas2.mywatchlist.views import menerima_fungsi_html, menerima_fungsi_json, menerima_fungsi_xml, menerima_request_id_html
from mywatchlist.views import show_mywatchlist
from mywatchlist.views import menerima_fungsi_xml
from mywatchlist.views import menerima_fungsi_html
from mywatchlist.views import menerima_fungsi_json
from mywatchlist.views import menerima_request_id_json
from mywatchlist.views import menerima_fungsi_html
from mywatchlist.views import menerima_request_id_xml

app_name = 'mywatchlist'

urlpatterns = [
    path('',show_mywatchlist, name='show_mywatchlist'),
    path('xml/', menerima_fungsi_xml, name='mywatchlist/xml'),
    path('json/', menerima_fungsi_json, name='mywatchlist/json'),
    path('html', menerima_fungsi_html, name='mywatchlist/html'),
    path('json/<int:id>', menerima_request_id_json, name='menerima_request_id_json'),
    path('xml/<int:id>', menerima_request_id_xml, name='menerima_request_id_xml'),
    path('html/', menerima_fungsi_html, name='menerima_fungsi_html' )
]