from django.shortcuts import render, redirect
import datetime
from .models import *
from accounts.models import *
from transactions.models import *
from classrooms.models import *
from institutions.models import *
from notification.models import *
from publication.models import *
from transactions.models import *
from adminhoax.forms import *

# Create your views here.
def login(request):
    return render(request, "adminhoax/login.html")


def home(request):
    logs = Notification.objects.all()
    accountCount = Account.objects.count()
    instituionsCount = Institution.objects.count()
    articlesCount = Article.objects.count()
    transactionCount = Transaction.objects.count()

    contain = {
        "logs": logs,
        "accountCount": accountCount,
        "instituionsCount": instituionsCount,
        "articlesCount": articlesCount,
        "transactionCount": transactionCount,
    }

    return render(request, "adminhoax/index.html", contain)


def account(request):
    users = Account.objects.all()

    contain = {
        "users": users,
    }
    return render(request, "adminhoax/accounts.html", contain)


def accountDelete(request, pk):
    delete_user = Account.objects.get(id=pk)
    if request.method == "POST":
        delete_user.delete()
        return redirect("account")

    return render(request, "adminhoax/accounts_delete_confirm.html")


def classroom(request):
    recommendation = Recommendation.objects.all()

    contain = {
        "recommendation": recommendation,
    }

    return render(request, "adminhoax/classrooms.html", contain)


def classroomDelete(request, pk):
    delete_classroom = Recommendation.objects.get(id=pk)
    if request.method == "POST":
        delete_classroom.delete()
        return redirect("classroom")

    return render(request, "adminhoax/classrooms_delete_confirm.html")


def institution(request):
    institution = Institution.objects.all()

    contain = {
        "institution": institution,
    }

    return render(request, "adminhoax/institutions.html", contain)


def institutionVerify(request, pk):
    institutionVerification = Verification.objects.get(id=pk)
    institution = Institution.objects.get(id=institutionVerification.id)
    form = InstitutionVerifyForm(instance=institutionVerification)

    # if request.method == 'POST':
    #     form = InstitutionVerifyForm(request.POST, instance=institutionVerification)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('institution')

    contain = {
        "institutionVerification": institutionVerification,
        "institution": institution,
        "form": form,
    }

    return render(request, "adminhoax/institutions_view_verify.html", contain)


def subscription(request):
    subscription = SubscriptionPlan.objects.all()

    contain = {
        "subscription": subscription,
    }

    return render(request, "adminhoax/subscriptions.html", contain)


def subscriptionAdd(request, pk):

    if request.method == "POST":
        # print('Printing POST:', request.POST)
        formset = AddSubscriptionPlan(request.POST)
        if formset.is_valid():
            formset.save()
            return redirect("/")

    context = {"form": formset}
    return render(request, "accounts/order_form.html", context)


def subscriptionDelete(request, pk):
    delete_subscription = SubscriptionPlan.objects.get(id=pk)
    if request.method == "POST":
        delete_subscription.delete()
        return redirect("subscription")

    return render(request, "adminhoax/subscription_delete_confirm.html")


def transaction(request):
    transaction = Transaction.objects.all()

    contain = {
        "transaction": transaction,
    }

    return render(request, "adminhoax/transactions.html", contain)


def publication(request):
    publication = Article.objects.all()

    contain = {
        "publication": publication,
    }

    return render(request, "adminhoax/publications.html", contain)
