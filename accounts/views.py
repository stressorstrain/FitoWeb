from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CustomAuthForm, RegistrationForm, ProfileForm, ProjectsForm, UserUploadsForms, NotesForm
from .models import UserProfile, UserProjects, UserUploads, UserDates
from django.views.generic.edit import DeleteView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import TemplateView


def log_in(request):
    template = 'registration/login.html'
    user_req = request.user
    if user_req.is_authenticated:
        username = user_req.username
        if username == 'admin':
            log_out(request)
        else:
            return redirect('accounts:profilepage', username)
    else:
        form = CustomAuthForm()
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            name = user.first_name + "_" + user.last_name
            return redirect('accounts:profilepage', username)

        else:
            messages.error(request, "Error wrong username/password")
        return render(request, "registration/login.html", {'form': form})


def profile(request, username, **kwargs):
    if request.method == "POST":
        p_form = ProjectsForm(request.POST)
        doc_form = UserUploadsForms(request.POST, request.FILES)
        notes_form = NotesForm(request.POST)
        print(notes_form.errors)
        if p_form.is_valid():
            projeto = p_form.cleaned_data['projeto']
            data = p_form.cleaned_data['data']
            nivel = p_form.cleaned_data['nivel']
            project = UserProjects(user=request.user, projeto=projeto, data=data, nivel=nivel)
            project.save()

        elif doc_form.is_valid():
            doc = doc_form.cleaned_data['docname']
            type = doc_form.cleaned_data['type']
            projeto = doc_form.cleaned_data['projetos']
            user = UserProfile.objects.get(user=request.user)

            instance = UserUploads(user=user, projetos=projeto, docname=doc, type=type, file=request.FILES['file'])
            instance.save()

        elif notes_form.is_valid():
            user = UserProfile.objects.get(user=request.user)
            note_text = notes_form.cleaned_data['note_text']
            note_date = notes_form.cleaned_data['note_date']
            instance = UserDates(user=user, note_text=note_text, note_date=note_date)
            instance.save()

    profiles = UserProfile.objects.all().filter(user=request.user)
    avatar = avatarr(profiles)
    notas = UserDates.objects.all()
    user_pro = UserProjects.objects.all()
    user_doc = UserUploads.objects.all()

    pro_doc = projetos(user_doc, request)
    user_dates = nota_date(notas, request)
    doc_by_project = prodoc(pro_doc, user_doc)
    most_recent = UserUploads.objects.filter(user__user=request.user).latest('projetos').projetos

    upload_form = UserUploadsForms
    project_form = ProjectsForm
    notes_form = NotesForm

    return render(request, 'accounts/profile.html',
                  {
                      'user': request.user,
                      'avatar': avatar,
                      'upform': upload_form,
                      'projeto': user_pro,
                      'user_doc': user_doc,
                      'pro_doc': doc_by_project,
                      'user_pro': pro_doc,
                      'projects_form': project_form,
                      'notes_form': notes_form,
                      'notes': user_dates,
                      'all_notes': notas,
                      'recent': most_recent,

                  })


def avatarr(profiles):
    for prof in profiles:
        return prof.avatar


def prodoc(projs, docs):
    all = []
    for projeto in projs:
        prodoc = []
        for doc in docs:
            if doc.projetos == projeto:
                prodoc.append(doc.docname)
        all.append(prodoc)
    return all

def nota_date(notas, request):
    dates = []
    for note in notas:
        nt_list = []
        if str(note.user) == str(request.user):
            nt_list.append(note.note_date.strftime("%d"))
            nt_list.append(note.note_date.strftime("%m"))
            dates.append(nt_list)
    return dates


def projetos(doc, request):
    documentos = []
    for docs in doc:
        if str(docs.user) == str(request.user):
            if docs.projetos not in documentos:
                documentos.append(docs.projetos)
    return documentos


def log_out(request):
    print("ok")
    return render(request, 'base.html', {})


def redirector(request):
    model = User
    slug_field = "username"
    template_name = 'accounts/profile.html'


def register(request):
    if request.method == "POST":
        form1 = RegistrationForm(request.POST)
        form2 = ProfileForm(request.POST, request.FILES)
        if form1.is_valid() and form2.is_valid():
            user = form1.save(commit=False)
            username = form1.cleaned_data['username']
            raw_password = form1.cleaned_data['password1']
            user.set_password(raw_password)
            user.save()

            avatar = form2.cleaned_data["avatar"]
            profiles = UserProfile(user=user, avatar=avatar)
            profiles.save()

        else:
            print("not valid")

        return redirect('accounts:login')

    else:
        form = RegistrationForm()
        form2 = ProfileForm()
        print("k")
        return render(request, 'accounts/userc.html', {'form': form, 'form2':form2})


def user_page(request, user_id):
    pass


class DeleteNote(DeleteView):
    model = UserDates
    success_url = reverse_lazy(log_in)


class DeleteProject(DeleteView):
    model = UserProjects
    success_url = reverse_lazy(log_in)



