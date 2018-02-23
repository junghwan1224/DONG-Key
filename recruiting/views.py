from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.urls import reverse
from django.http.response import Http404, HttpResponse, JsonResponse
from django.http import HttpResponseRedirect
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string

from club.models import Club
from .models import AdminResume, ApplicantResume, Question
from .forms import QuestionForm, AdminResumeForm, ApplicantResumeForm, ShortAnswerForm, LongAnswerForm


def admin_resume_list(request, club_pk):
    club = get_object_or_404(Club, pk=club_pk)
    resume_list = AdminResume.objects.filter(club=club)
    ctx = {
        'club': club,
        'resume_list': resume_list,
    }
    return render(request, 'recruiting/admin_resume_list.html', ctx)


def applicant_resume_form_list(request, club_pk):
    club = get_object_or_404(Club, pk=club_pk)
    resume_form_list = AdminResume.objects.filter(club=club)
    ctx ={
        'club': club,
        'resume_form_list': resume_form_list,
    }
    return render(request, 'recruiting/applicant_resume_form_list.html', ctx)


def applicant_resume_list(request, club_pk, resume_pk):
    club = get_object_or_404(Club, pk=club_pk)
    applicant_resume_list = ApplicantResume.objects.filter(admin_resume__pk=resume_pk)
    ctx = {
        'club':club,
        'applicant_resume_list': applicant_resume_list,
    }
    return render(request, 'recruiting/applicant_resume_form_list.html', ctx)


def create_admin_resume(request, club_pk):
    club = get_object_or_404(Club, pk=club_pk)
    admin_resume_form = AdminResumeForm(request.POST or None)
    if request.method =="POST" and admin_resume_form.is_valid():
        resume = admin_resume_form.save(commit=False)
        resume.club = club
        resume.save()
        return redirect(reverse('recruiting:read_admin_resume', kwargs={
            'club_pk': club.pk,
            'resume_pk': resume.pk,
        }))
    ctx ={
        'club': club,
        'admin_resume_form': admin_resume_form,
    }
    return render(request,'recruiting/create_admin_resume.html', ctx)


def read_admin_resume(request, club_pk, resume_pk):
    club = get_object_or_404(Club, pk=club_pk)
    admin_resume = get_object_or_404(AdminResume, pk=resume_pk)
    ctx = {
        'club': club,
        'admin_resume': admin_resume,
        'question_form': QuestionForm(),
    }
    return render(request, 'recruiting/read_admin_resume.html', ctx)


def create_question(request, club_pk, resume_pk):
    if request.method == "POST":
        club = Club.objects.get(pk=club_pk)
        resume = get_object_or_404(AdminResume, pk=resume_pk)
        question_form = QuestionForm(request.POST)

        if question_form.is_valid(): # 추가 질문 내용이 추가 안됨
            question = question_form.save(commit=False)
            question.admin_resume = resume
            question.save()

            return render(request, 'recruiting/question.html', {'question': question, })
            # return HttpResponseRedirect("recruiting/question.html", {'question': question})

    return HttpResponse(status=405)
    # return render_to_response('recruiting/question.html', {'question': question })


def answer_formset_factory(question_list, data=None):
    formset = []
    for question in question_list:
        if question.is_short_answer:
            form = ShortAnswerForm(data, prefix=question.pk)
        else:
            form = LongAnswerForm(data, prefix=question.pk)
        form.question = question
        formset.append(form)
    return formset


def create_applicant_resume_list(request, club_pk):
    club = Club.objects.get(pk=club_pk)
    is_member = request.user.member_set.filter(club__pk=club_pk).exists()
    ctx ={
        'club': club,
        'is_member': is_member,
    }
    return render(request, 'recruiting/create_applicant_resume_list.html', ctx)


def create_applicant_resume(request, club_pk, resume_pk):
    club = Club.objects.get(pk=club_pk)
    admin_resume = get_object_or_404(AdminResume, pk=resume_pk)
    question_list = Question.objects.filter(admin_resume__pk=resume_pk)

    applicant_resume_form = ApplicantResumeForm(request.POST or None)

    short_question_list = [q for q in question_list if q.is_short_answer]
    short_answer_formset = answer_formset_factory(short_question_list, data=request.POST or None)

    long_question_list = [q for q in question_list if not q.is_short_answer]
    long_answer_formset = answer_formset_factory(long_question_list, data=request.POST or None)

    if request.method == 'POST' and applicant_resume_form.is_valid():
        resume = applicant_resume_form.save(commit=False)
        resume.admin_resume = admin_resume
        resume.applicant = request.user
        resume.save()

        for short_answer_form in short_answer_formset:
            short_answer = short_answer_form.save(commit=False)
            short_answer.applicant_resume = resume
            short_answer.question = short_answer_form.question
            short_answer.save()
        for long_answer_form in long_answer_formset:
            long_answer = long_answer_form.save(commit=False)
            long_answer.applicant_resume = resume
            long_answer.question = long_answer_form.question
            long_answer.save()

        return redirect(reverse('recruiting:read_applicant_resume', kwargs={
            'club_pk': club.pk,
            'resume_pk': resume.pk,
        }))
    ctx = {
        'club': club,
        'resume': admin_resume,
        'applicant_resume_form': applicant_resume_form,
        'short_answer_formset': short_answer_formset,
        'long_answer_formset': long_answer_formset,
    }
    return render(request, 'recruiting/create_applicant_resume.html', ctx)


def read_applicant_resume(request, club_pk, resume_pk):
    club = Club.objects.get(pk=club_pk)
    resume = ApplicantResume.objects.get(pk=resume_pk)
    ctx ={
        'club': club,
        'resume': resume,
    }
    return render(request, 'recruiting/read_applicant_resume.html', ctx)