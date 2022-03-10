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
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse

# Create your views here.
def loginPage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        print(username, password)
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if request.user.groups.filter(name="admin").exists():
                return redirect("dashboard")
            elif request.user.groups.filter(name="staff").exists() and request.user.is_active:
                print(user.email, user.password)
                return redirect("staffInstitutionPending")
            else:
                messages.info(request, "Account Invalid OR is Inactive")

        else:
            messages.info(request, "Username OR password is incorrect")

    context = {}
    return render(request, "adminhoax/login.html", context)


def logoutUser(request):
    logout(request)
    return redirect("loginPage")


@login_required(login_url="login")
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
    form = AddStaffAccount(initial={"is_staff": True})
    group = Group.objects.all().order_by("id")

    if request.method == "POST":
        form = AddStaffAccount(request.POST)
        if form.is_valid():
            print("pass")
            # form.cleaned_data["is_staff"] = True
            # request.user.is_staff = True
            print(form.cleaned_data)
            # breakpoint()

            form.save()

            gname = request.POST.get("gname")
            email = request.POST.get("email")
            # ugroup, __ = Group.objects.get_or_create(name=gname)
            print(gname)
            user = Account.objects.get(email=email)
            ugroup = Group.objects.get(name=gname)
            ugroup.user_set.add(user)
            print("pass")

            return redirect("accounts_staff")

    contain = {
        "form": form,
        "group": group,
    }
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
    group = Group.objects.all()

    uugroup = []
    for i in update_user.groups.all():
        uugroup.append(i.name)

    if request.method == "POST":
        form = UpdateAccount(request.POST, instance=update_user)
        print("error")
        if form.is_valid():

            form.save()

            gname = request.POST.get("gname")
            # ugroup, __ = Group.objects.get_or_create(name=gname)
            print(gname)
            user = Account.objects.get(id=pk)
            user.groups.clear()
            ugroup = Group.objects.get(name=gname)
            ugroup.user_set.add(user)

            # user = Account.objects.get(id=pk)
            # user.groups.add(ugroup)
            # grouptype

            return redirect("accounts_staff")

    contain = {
        "update_user": update_user,
        "form": form,
        "group": group,
        "uugroup": uugroup,
    }

    return render(request, "adminhoax/accounts_update.html", contain)


def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            # messages.success(request, 'Your password was successfully updated!')
            return redirect("dashboard")
        else:
            messages.error(request, "Please correct the error below.")
    else:
        form = PasswordChangeForm(request.user)
    return render(request, "adminhoax/change_password.html", {"form": form})


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


def staffhome(request):
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

    return render(request, "adminhoax/staffDashboard.html", contain)


def institution(request):
    institutionVerification = Verification.objects.all().filter(status="pending")


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


def institutionDisapproved(request):
    institutionVerification = Verification.objects.all().filter(status="disapproved")

    contain = {
        "institutionVerification": institutionVerification,
    }

    return render(request, "adminhoax/institutions_disapproved.html", contain)


def institutionDelete(request, pk):
    delete_institution = Institution.objects.get(id=pk)
    if request.method == "POST":
        delete_institution.delete()
        return redirect("institution")

    return render(request, "adminhoax/institutions_delete_confirm.html")


def institutionVerify(request, pk):
    institutionVerification = Verification.objects.get(id=pk)
    # institution = Institution.objects.get(id=institutionVerification.id)
    form = InstitutionVerifyForm(instance=institutionVerification)

    if request.method == "POST":
        form = InstitutionVerifyForm(request.POST, instance=institutionVerification)
        if form.is_valid():
            form.save()
            return redirect("institution")

    contain = {
        "institutionVerification": institutionVerification,
        # "institution": institution,
        "form": form,
    }

    return render(request, "adminhoax/institutions_view_verify.html", contain)


def staffInstitutionPending(request):
    institutionVerification = Verification.objects.all().filter(status="pending")

    contain = {
        "institutionVerification": institutionVerification,
    }

    return render(request, "adminhoax/staffInstPending.html", contain)


def staffInstitutionApproved(request):
    institutionVerification = Verification.objects.all().filter(status="approved")

    contain = {
        "institutionVerification": institutionVerification,
    }

    return render(request, "adminhoax/staffInstApproved.html", contain)


def staffInstitutionDisapproved(request):
    institutionVerification = Verification.objects.all().filter(status="disapproved")

    contain = {
        "institutionVerification": institutionVerification,
    }

    return render(request, "adminhoax/staffInstDisapproved.html", contain)


def staffInstitutionVerify(request, pk):
    # breakpoint()
    institutionVerification = Verification.objects.get(id=pk)
    institution = Institution.objects.get(id=institutionVerification.id)
    form = InstitutionVerifyForm(instance=institutionVerification)

    if request.method == "POST":
        form = InstitutionVerifyForm(request.POST, instance=institutionVerification)
        if form.is_valid():
            form.save()
            return redirect("staffInstitutionPending")

    contain = {
        "institutionVerification": institutionVerification,
        "institution": institution,
        "form": form,
    }

    return render(request, "adminhoax/staffInstVerify.html", contain)


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

    return render(request, "adminhoax/subscriptions_delete_confirm.html")


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
    article = Article.objects.all()

    contain = {
        "article": article,
    }

    return render(request, "adminhoax/publications.html", contain)


def publicationDelete(request, pk):
    delete_publication = Article.objects.get(id=pk)
    if request.method == "POST":
        delete_publication.delete()
        return redirect("publication")

    return render(request, "adminhoax/publications_delete_confirm.html")
