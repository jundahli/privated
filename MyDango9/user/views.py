from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from .form import MyUserCreationForm
from .models import MyUser
from django.contrib.auth.models import Permission

# Create your views here.
def loginView(request):
    tips = '请登录'
    title = '用户登录'
    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        if MyUser.objects.filter(username=username):
            user = authenticate(username=username,password=password)
            if user:
                if user.is_active:
                    login(request,user)
                return redirect('/')
            else:
                tips = '账号密码错误,请重新输入'
        else:
            tips = '用户不存在,去注册'
    return render(request,'user.html',locals())

def registerView(request):
    # 设置标题和另外两个URL链接
    title = '用户注册'
    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        if MyUser.objects.filter(username=username):
            tips = '用户已存在'
        else:
            user = MyUser.objects.create_user(username=username,password=password)
            user.save()
            permission = Permission.objects.filter(codename='visit_Product')[0]
            user.user_permissions.add(permission)
            return redirect('/user/login.html')
    return render(request,'user.html',locals())

def setpasswordView(request):
    # 设置标题和另外两个URL链接
    title = '修改密码'
    unit_2 = '/user/login.html'
    unit_2_name = '立即登录'
    unit_1 = '/user/register.html'
    unit_1_name = '立即注册'
    new_password = True
    if request.method == 'POST':
        username = request.POST.get('username', '')
        old_password = request.POST.get('password', '')
        new_password = request.POST.get('new_password', '')
        if User.objects.filter(username=username):
            user = authenticate(username=username,password=old_password)
            # 判断用户的账号密码是否正确
            if user:
                user.set_password(new_password)
                user.save()
                tips = '密码修改成功'
            else:
                tips = '原始密码不正确'
        else:
            tips = '用户不存在'
    return render(request, 'user.html', locals())

# 使用make_password实现密码修改
from django.contrib.auth.hashers import make_password
def setpasswordView_1(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        old_password = request.POST.get('password', '')
        new_password = request.POST.get('new_password', '')
        # 判断用户是否存在
        user = User.objects.filter(username=username)
        if User.objects.filter(username=username):
            user = authenticate(username=username,password=old_password)
            # 判断用户的账号密码是否正确
            if user:
                # 密码加密处理并保存到数据库
                dj_ps = make_password(new_password, None, 'pbkdf2_sha256')
                user.password = dj_ps
                user.save()
            else:
                print('原始密码不正确')
    return render(request, 'user.html', locals())

# 用户注销，退出登录
def logoutView(request):
    logout(request)
    return redirect('/')