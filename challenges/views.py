from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.template.loader import render_to_string
from django.urls import reverse


monthly_challenges = {
    "january" : "it's january",
    "feb" : None,
    "march" : "it's march",
    "apr" : "it's april",
    "may" : "it's may",
    "june" : "it's june",
    "july" : "it's july",
    "agust" : "it's agust",
    "septemberr" : "it's september",
    "octber" : "it's octber",
    "november" : "it's november",
    "december" : None

}

def index(request):
    # list_items = ""
    months = list(monthly_challenges.keys())
    #
    # for month in months:
    #     month_path = reverse("month-challenge", args=[month])
    #     list_items += f'<li> <a href="{month_path}">{month.capitalize()} </a> </li>'
    #
    # response_data = f"<ul>{list_items}</ul>"
    return render(request, "challenges/index.html", {
        'months': months
    })


def monthly_challenges_by_int(request, month):
    months = list(monthly_challenges.keys())
    print(months)
    if month > len(months):
        return HttpResponseNotFound(f"You Enterd a Wrong Month {month}")
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)
def monthly_challenge(request, month):
    try:
        monthly_text = monthly_challenges[month]
        return render(request,"challenges/challenges.html", {
            'text': monthly_text,
            'month': month
            })
    except:
        monthly_text = HttpResponseNotFound(f"<h1> This month '{month}'is no registerd </h1>")
    return HttpResponse(monthly_text)

