from django.shortcuts import render


def index(request):

    # Authenticated users view their inbox
    # if request.user.is_authenticated:
    return render(request, "mail/inbox.html")

    # # Everyone else is prompted to sign in
    # else:
    #     return HttpResponseRedirect(reverse("login"))