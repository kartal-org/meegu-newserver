from pickle import TRUE
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
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import user_passes_test

# Create your views here.
def loginPage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username, password)
        user = authenticate(username=username, password=password)

        # if request.user.is_superuser:
        if user is not None:
            login(request, user)
            # return redirect('dashboard')
            # return redirect('dashboard')
            # if request.user.is_superuser:
            breakpoint()
            if request.user.is_staff:
                # if request.user.is_superuser:
                return redirect("dashboard")
            else:
                print(user.email, user.password)
                return redirect("institution")
        else:
            # print("error")
            messages.info(request, "Username OR password is incorrect")

    context = {}
    return render(request, "adminhoax/login.html", context)


def logoutUser(request):
    logout(request)
    return redirect("loginPage")


@login_required(login_url="login")
@user_passes_test(lambda u: u.is_superuser)
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
    users = Account.objects.all().filter(is_staff=False)

    contain = {
        "users": users,
    }
    return render(request, "adminhoax/accounts.html", contain)


def accountStaff(request):
    users = Account.objects.all().filter(is_staff=True)

    contain = {
        "users": users,
    }
    return render(request, "adminhoax/accounts_staff.html", contain)


def accountAdd(request):
    form = AddStaffAccount()

    #%verifier_group = Group.objects.get(name='verifier')

    if request.method == "POST":
        form = AddStaffAccount(request.POST)
        print(request.POST.get("username"))
        print(request.POST.get("email"))
        print(request.POST.get("password"))
        breakpoint()
        if form.is_valid:
            # form.groups.add(verifier_group)
            # user = form.cleaned_data.get('email')
            form.save()
            return redirect("accounts_staff")

    contain = {"form": form}
    return render(request, "adminhoax/accounts_add.html", contain)


def accountDelete(request, pk):
    delete_user = Account.objects.get(id=pk)
    if request.method == "POST":
        delete_user.delete()
        return redirect("account")

    return render(request, "adminhoax/accounts_delete_confirm.html")


def accountUpdate(request, pk):
    update_user = Account.objects.get(id=pk)
    form = UpdateAccount(instance=update_user)

    if request.method == "POST":
        form = UpdateAccount(request.POST, instance=update_user)
        print("error")
        if form.is_valid():
            print("error")
            verifier_group = Group.objects.get(name="verifier")
            update_user.groups.add(verifier_group)

            form.save()
            return redirect("account")

    contain = {
        "update_user": update_user,
        "form": form,
        #'permgroups':permgroups,
    }

    return render(request, "adminhoax/accounts_update.html", contain)


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
    institutionVerification = Verification.objects.all().filter(status="pending")

    contain = {
        "institutionVerification": institutionVerification,
    }

    return render(request, "adminhoax/institutions.html", contain)


def institutionApproved(request):
    institutionVerification = Verification.objects.all().filter(status="approved")

    contain = {
        "institutionVerification": institutionVerification,
    }

    return render(request, "adminhoax/institutions_approved.html", contain)


def institutionDelete(request, pk):
    delete_institution = Institution.objects.get(id=pk)
    if request.method == "POST":
        delete_institution.delete()
        return redirect("institution")

    return render(request, "adminhoax/institutions_delete_confirm.html")


def institutionVerify(request, pk):
    institutionVerification = Verification.objects.get(id=pk)
    institution = Institution.objects.get(id=institutionVerification.id)
    form = InstitutionVerifyForm(instance=institutionVerification)

    if request.method == "POST":
        form = InstitutionVerifyForm(request.POST, instance=institutionVerification)
        if form.is_valid():
            form.save()
            return redirect("institution")

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


def subscriptionAdd(request):
    form = AddSubscriptionPlan()
    if request.method == "POST":
        form = AddSubscriptionPlan(request.POST)
        if form.is_valid:
            form.save()
            return redirect("subscription")

    contain = {"form": form}
    return render(request, "adminhoax/subscriptions_add.html", contain)


def subscriptionDelete(request, pk):
    delete_subscription = SubscriptionPlan.objects.get(id=pk)
    if request.method == "POST":
        delete_subscription.delete()
        return redirect("subscription")

    return render(request, "adminhoax/subscription_delete_confirm.html")


def subscriptionUpdate(request, pk):
    plan = SubscriptionPlan.objects.get(id=pk)
    form = UpdateSubscriptionPlan(instance=plan)

    if request.method == "POST":
        form = UpdateSubscriptionPlan(request.POST, instance=plan)
        if form.is_valid():
            form.save()
            return redirect("subscription")

    contain = {
        "plan": plan,
        "form": form,
    }

    return render(request, "adminhoax/subscriptions_update.html", contain)


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
