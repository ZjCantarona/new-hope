from django.urls import path

from .views import (
    table_members, list_members, thumbnail_members, detail_member, edit_member, update_member, add_member, create_member, restore_member,
    delete_member, filter_members, search_members, get_members_by_statuses, get_members_by_speakers, list_deleted_members,
    list_ministries, add_ministries, create_ministry,
    list_speakers, add_speaker, create_speaker, delete_ministry, delete_speaker, update_ministry, update_speaker, detail_speaker, thumbnail_speaker
)

urlpatterns = [
    # UrlConf For Members
    path('list/', list_members, name="list_members"),
    path('table/', table_members, name="table_members"),
    path('thumbnail/', thumbnail_members, name="thumbnail_members"),
    path('detail/<int:pk>/', detail_member, name="detail_member"),
    path('edit/<int:pk>/', edit_member, name="edit_member"),
    path('update/<int:pk>/', update_member, name="update_member"),
    path('add/', add_member, name="add_member"),
    path('create/', create_member, name="create_member"),
    path('delete/<int:pk>/', delete_member, name="delete_member"),
    path('filter/', filter_members, name="filter_members"),
    path('list/search/', search_members, name="search_members"),
    path('list/<status>/', get_members_by_statuses, name="get_members_by_statuses"),
    path('list_by_speaker/<speaker>/', get_members_by_speakers, name="get_members_by_speaker"),
    path('deleted/list/', list_deleted_members, name="list_deleted_members"),
    path('restore/<int:pk>/', restore_member, name="restore_members"),


    # UrlConf For Ministries
    path('ministries/list/', list_ministries, name="list_ministries"),
    path('ministries/add/', add_ministries, name="add_ministry"),
    path('ministries/create/', create_ministry, name="create_ministry"),
    path('ministries/delete/<int:pk>/', delete_ministry, name="delete_ministry"),
    path('ministries/update/<int:pk>/', update_ministry, name="update_ministry"),

    # UrlConf For Speakers
    path('speakers/list/', list_speakers, name="list_speakers"),
    path('speakers/add/', add_speaker, name="add_speaker"),
    path('speakers/create/', create_speaker, name="create_speaker"),
    path('speakers/delete/<int:pk>/', delete_speaker, name="delete_speaker"),
    path('speakers/update/<int:pk>/', update_speaker, name="update_speaker"),
    path('speakers/detail/<int:pk>/', detail_speaker, name="detail_speaker"),
    path('speakers/thumbnail/', thumbnail_speaker, name="thumbnail_speaker"),
]