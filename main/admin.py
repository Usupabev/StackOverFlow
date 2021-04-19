from django.contrib import admin

from .models import *


class CodeImageInline(admin.TabularInline):
    model = CodeImage
    max_num = 10
    min_num = 1

@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    inlines = [CodeImageInline,]

class CommentInline(admin.TabularInline):
    model = Comment

@admin.register(Reply)
class ReplyAdmin(admin.ModelAdmin):
    inlines = [CommentInline,]
    list_filter = ('created', )