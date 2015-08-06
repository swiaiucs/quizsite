# coding: utf-8

from django.shortcuts import render

quizzes = {
	"klassiker": {
   		"name": u"Klassiska böcker",
	   	"description": u"Hur bra kan du dina klassiker?"
	},
	"fotboll": {
	   	"name": u"Thailand, Mallis eller Bulgarien?",
	   	"description": u"Vilken Svennechartrare är du?"
	},
	"kanda-hackare": {
	    	"name": u"Världens mest kända hackare",
	    	"description": u"Hackerhistoria är viktigt, kan du den?"	},
}


# Create your views here.

def startpage(request):
	context = {
		"quizzes": quizzes,
	}
	return render(request, "quiz/startpage.html", context)

def quiz(request, slug):
	context = {
		"quiz": quizzes[slug],
		"quiz_slug": slug,
	}
	return render(request, "quiz/quiz.html", context)

def question(request, slug, number):
	context = {
		"question_number": number,
	    	"question": u"Var äter du helst i Stockholm?",
		"answer1": u"Koh Phangan! Så himla genuint och gott. Värsta regnskogen inomhus också, riktigt läckert",
	   	"answer2": u"BARcelona - haha jättekul namn!!",
	    	"answer3": u"Vet inte, men det måste vara billigt",
	    	"quiz_slug": slug,
	}
	return render(request, "quiz/question.html", context)

def completed(request, slug):
	context = {
	    	"correct": 12,
	    	"total": 20,
		"quiz_slug": slug,
	}
	return render(request, "quiz/completed.html", context)









