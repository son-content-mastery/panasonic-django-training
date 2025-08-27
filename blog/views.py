from django.shortcuts import render, redirect
from .models import Post
from .forms import ContactForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def home(request):
    # Query all posts
    all_posts = Post.objects.all()

    context = {
        'posts': all_posts,
    }

    return render(request, 'blog/home.html', context)


@login_required(login_url='sign_in')
def post_detail(request, post_id):

    single_post = Post.objects.get(id=post_id)

    return render(request, 'blog/post_detail.html', {'post': single_post})


def contact(request):

    form = ContactForm
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            print("ฟอร์มถูกส่งเรียบร้อย")
            return redirect('home')
    else:
        form = ContactForm()

    return render(request, 'blog/contact.html', {'form': form})


def register(request):
    form = RegisterForm
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            print("สมัครสมาชิกเรียบร้อย")
            return redirect('home')
    else:
        form = RegisterForm()
        print("แสดงฟอร์มเรียบร้อย")

    return render(request, 'blog/register.html', {'myform': form})


def sign_in(request):

    if request.method == 'POST':
        username_form = request.POST["username"]
        password_form = request.POST["password"]
        user = authenticate(request, username=username_form, password=password_form)

        if user is not None:
            login(request, user)
            print("ล็อกอินสำเร็จ")
            return redirect('home')
        else:
            print("ไม่สำเร็จ")
            pass

    return render(request, 'blog/login.html')


def sign_out(request):
    logout(request)
    return redirect('home')

