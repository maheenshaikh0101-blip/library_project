from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .forms import NoteForm
from .models import Note


@login_required
def note_list(request):
    # Session feature: count how many times this user opened the list
    visits = request.session.get("visits", 0) + 1
    request.session["visits"] = visits

    # User-specific data: only this user's notes
    notes = Note.objects.filter(owner=request.user).order_by("-created_at")
    return render(request, "notes/note_list.html", {
        "notes": notes,
        "visits": visits,
    })


@login_required
def note_create(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.owner = request.user
            note.save()
            messages.success(request, "Note added successfully!")
            return redirect("note_list")
    else:
        form = NoteForm()
    return render(request, "notes/note_form.html", {"form": form, "heading": "Add Note"})


@login_required
def note_update(request, id):
    note = get_object_or_404(Note, id=id, owner=request.user)
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            messages.success(request, "Note updated successfully!")
            return redirect("note_list")
    else:
        form = NoteForm(instance=note)
    return render(request, "notes/note_form.html", {"form": form, "heading": "Update Note"})


@login_required
def note_delete(request, id):
    note = get_object_or_404(Note, id=id, owner=request.user)
    if request.method == "POST":
        note.delete()
        messages.success(request, "Note deleted.")
        return redirect("note_list")
    return render(request, "notes/note_delete.html", {"note": note})