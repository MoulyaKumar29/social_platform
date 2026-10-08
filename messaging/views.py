from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render

from .forms import MessageForm
from .models import Message


@login_required
def conversation(request, username):
    other_user = get_object_or_404(
        User,
        username=username
    )

    messages = Message.objects.filter(
        sender__in=[request.user, other_user],
        receiver__in=[request.user, other_user]
    ).order_by("created_at")

    Message.objects.filter(
        sender=other_user,
        receiver=request.user,
        is_read=False
    ).update(is_read=True)

    if request.method == "POST":
        form = MessageForm(request.POST)

        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.receiver = other_user
            message.save()

            return redirect(
                "conversation",
                username=other_user.username
            )
    else:
        form = MessageForm()

    return render(
    request,
    "messaging/conversation.html",
    {
        "other_user": other_user,
        "messages": messages,
        "form": form,
    }
)

@login_required
def inbox(request):
    sent_to = Message.objects.filter(
        sender=request.user
    ).values_list("receiver", flat=True)

    received_from = Message.objects.filter(
        receiver=request.user
    ).values_list("sender", flat=True)

    user_ids = set(sent_to) | set(received_from)

    users = User.objects.filter(
        id__in=user_ids
    ).exclude(
        id=request.user.id
    )

    return render(
        request,
        "messaging/inbox.html",
        {"users": users}
    )