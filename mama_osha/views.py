from django.shortcuts import render, redirect


def home(request):
    
    posts= Post.objects.all()
   
    if request.method == 'POST':
        form = UploadForm(request.POST,request.FILES)

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form =UploadForm()
        print (form)

    return render(request, 'mama_osha/home.html', locals())