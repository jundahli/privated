from django.contrib import admin
from .models import *

# Register your models here.

#修改title和header

admin.site.site_title = 'MyDjango后台管理'
admin.site.site_header = 'MyDjango'

#自定义ProductAdmin类并继承ModelAdmin
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    #设置显示字段
    list_display = ['id','name','weight','size','type']
    #设置可搜索的字段并在admin后台数据生成搜索框,如有外键,应使用双下划线连接两个模型的字段
    search_fields = ['id','name','type__type_name']
    #设置过滤器,在后台数据的右侧生成导航栏,如有外键,应使用双下划线连接两个模型的字段
    list_filter = ['name','type__type_name']
    #设置排序方式,['id']为升序,降序为['-id']
    ordering = ['id']
    #设置时间选择器,如字段中有时间格式才可以使用
    #date_hierarchy = Field
    #在添加新数据时,设置可添加数据的字段
    fields = ['name','weight','size','type']
    #设置可读字段,在修改或新增数据时使其无法设置
    readonly_fields = ['name']

    #重写get_readonly_fields函数,设置超级用户和普通用户的权限
    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            self.readonly_fields = []
        return self.readonly_fields

#在admin.py的ProductAdmin 中添加自定义字段
#添加自定义字段,在属性list_display中添加自定义字段colored_type, colored_type来自于模型Product
    list_display.append('colored_type')

    def get_queryset(self, request):
        qs = super(ProductAdmin,self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(id__lt=6)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'type':
            if not request.user.is_superuser:
                kwargs["queryset"] = Type.objects.filter(id__lt=4)
        return super(admin.ModelAdmin,self).formfield_for_foreignkey(db_field,
                                        request,**kwargs)

    #修改保存方法
    def save_model(self, request, obj, form, change):
        if change:
            #获取当前用户名
            user = request.user
            #使用模型获取数据,pk代表具有主键属性的字段
            name = self.model.objects.get(pk=obj.pk).name
            #使用表单获取数据
            weight = form.cleaned.data['weight']
            #写入日志文件
            f = open('/home/kenco/MyDjango_log.txt','a')
            f.write('产品:' + str(name) + ',被用户: '+str(user)+' 修改'+'\r\n')
            f.close()
        else:
            pass
        super(ProductAdmin,self).save_model(request,obj,form,change)

    def delete_model(self, request, obj):
        pass
        super(ProductAdmin,self).delete_model(request,obj)
