from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from .models import BasicHabit, AdvancedHabit

# Create your views here.
def dashboard(request):
    context = {
        'basic_habits':BasicHabit.objects.all(),
    }
    if request.user.is_authenticated:
        return render(request, "manager/dashboard.html", context)
    else:
        return redirect('home')

class ViewBasicHabit(ListView):
    model = BasicHabit
    template_name = "manager/dashboard.html"
    context_object_name = "basic_habits"

class CreateBasicHabit(LoginRequiredMixin, CreateView):
    model = BasicHabit
    template_name = "manager/createHabit.html"
    fields = ["name", "time", "frequency"]

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class UpdateBasicHabit(UpdateView, LoginRequiredMixin, UserPassesTestMixin):
    model = BasicHabit
    template_name = "manager/viewHabit.html"
    fields = ["name", "time", "frequency"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['id']=self.object.id
        context['basic_habit']=self.object
        context['advanced_habits'] = AdvancedHabit.objects.all()
        return context
    
    def test_func(self):
        habit = self.get_object()
        if self.request.user == habit.owner:
            return True
        return False

class DeleteBasicHabit(DeleteView, LoginRequiredMixin, UserPassesTestMixin):
    model = BasicHabit
    template_name = "manager/deleteHabit.html"
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['id']=self.object.id
        return context
    
    def test_func(self):
        habit = self.get_object()
        if self.request.user == habit.owner:
            return True
        return False
    
class CreateAdvancedHabit(LoginRequiredMixin, CreateView):
    model = AdvancedHabit
    template_name = "manager/createAdvHabit.html"
    fields = ["basic"]
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
    
class UpdateAdvancedHabit(UpdateView, LoginRequiredMixin, UserPassesTestMixin):
    model = AdvancedHabit
    template_name = "manager/viewAdvHabit.html"
    fields = ["time", "place", "env_obvious", "habit_bundling", "culture", "figure", "benefits", "motivation_ritual", "habit_shaping", "reduce_friction", "incentive", "progress"]
    
    def test_func(self):
        habit = self.get_object()
        if self.request.user == habit.owner:
            return True
        return False

