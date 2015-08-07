# coding: utf-8

from django.shortcuts import render
from quiz.models import Quiz
from django.shortcuts import redirect

# quizzes = {
# 	"klassiker": {
#    		"name": u"Vilken slags granne är du?",
# 	   	"description": u"tbd"
# 	},
# 	"fotboll": {
# 	   	"name": u"Vilken Svennechartrare är du?",
# 	   	"description": u"Det finns några ställen som Svennechartrare älskar mer. Vilken typ är du?"
# 	},
# 	"kanda-hackare": {
# 	    	"name": u"Är du en hund- eller kattmänniska?",
# 	    	"description": u"TBD"	},
# }



# Create your views here.

def startpage(request):
	context = {
		"quizzes": Quiz.objects.all(),
	}
	return render(request, "quiz/startpage.html", context)

def quiz(request, slug):
	context = {
	    	"quiz": Quiz.objects.get(slug=slug),
	}
	return render(request, "quiz/quiz.html", context)

def question(request, slug, number):
	number = int(number)
	quiz = Quiz.objects.get(slug=slug)
	questions = quiz.questions.all()
	question = questions[number - 1]
	if number > questions.count():
		return redirect("completed_page", quiz.slug)
	context = {
    		"question_number": number,
    		"question": question.question,
	    	"answer1": question.answer1,
    		"answer2": question.answer2,
	    	"answer3": question.answer3,
	    	"quiz": quiz,
	}
	return render(request, "quiz/question.html", context)

def completed(request, slug):
	context = {
	    	"correct": 12,
	    	"total": 20,
		"quiz_slug": slug,
	}
	return render(request, "quiz/completed.html", context)









