from django.shortcuts import render, redirect
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserChangeForm,
    PasswordChangeForm,
)
from django.views.generic import CreateView, UpdateView
from django.contrib.auth import login, logout
from articles.forms import Registration, EditUserProfileForm
from django.contrib.auth.models import User
from articles.models import *
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.db import transaction


# Create your views here.


def signup_view(request):
    if request.method == 'POST':
        form = Registration(request.POST)
        if form.is_valid():
            user = form.save()
            # user log in
            login(request, user)
            return redirect('articles:article_list')
    else:
        form = Registration()

    return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('articles:article_list')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout_views(request):
    if request.method == 'POST':
        logout(request)
        return redirect('articles:article_list')
    else:
        return redirect('articles:article_list')


@login_required
def profile_view(request):
    args = {'user': request.user}
    return render(request, 'profile.html', args)


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditUserProfileForm(request.POST, instance=request.user)
        if form.is_valid:
            form.save()
            return redirect('accounts:profile_view')
    else:
        form = EditUserProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'edit_profile.html', args)


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.POST, user=request.user)
        if form.is_valid:
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('accounts:profile_view')
        else:
            return redirect('accounts:change_password')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'edit_profile.html', args)


## new view for updating profile because --EditProfile-- dosent work yet.
@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        # user_form = UserForm(request.POST, instance=request.user)
        profile_form = EditUserProfileForm(request.POST, instance=request.user.userprofile)
        if profile_form.is_valid():
            # user_form.save()
            profile_form.save()
            # messages.success(request, _('Your profile was successfully updated!'))
            return redirect('accounts:profile_view')
        # else:
            # messages.error(request, _('Please correct the error below.'))

    else:
        # user_form = UserForm(instance=request.user)
        profile_form = EditUserProfileForm(instance=request.user.userprofile)
    return render(request, 'edit_profile.html', {
        # 'user_form': user_form,
        'profile_form': profile_form
    })


class EditProfile(UpdateView):
    form_class = EditUserProfileForm
    template_name = 'edit_profile.html'
    success_url = '/accounts/profile/'
    # def get_queryset(self):
    #     return self.request.user
        # return User.objects.filter(user=self.request.user)

    def get_queryset(self):
        return Profile.objects.filter(user=self.request.user)

    def get_form_kwargs(self):
        kwargs = super(EditProfile, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    # def get_form_class(self):
    #     """Return the form class to use in this view."""
    #     if self.fields is not None and self.form_class:
    #         raise ImproperlyConfigured(
    #             "Specifying both 'fields' and 'form_class' is not permitted."
    #         )
    #     if self.form_class:
    #         print('1111111111111111111 level')
    #         print(self.form_class)
    #         return self.form_class
    #     else:
    #         if self.model is not None:
    #             # If a model has been explicitly provided, use it
    #             model = self.model
    #         elif hasattr(self, 'object') and self.object is not None:
    #             # If this view is operating on a single object, use
    #             # the class of that object
    #             model = self.object.__class__
    #         else:
    #             # Try to get a queryset and extract the model class
    #             # from that
    #             model = self.get_queryset().model
    #         if self.fields is None:
    #             raise ImproperlyConfigured(
    #                 "Using ModelFormMixin (base class of %s) without "
    #                 "the 'fields' attribute is prohibited." % self.__class__.__name__
    #             )
    #         print('222222222222 level')
    #         return model_forms.modelform_factory(model, fields=self.fields)



    # def get_form(self, form_class=None):
    #     """Return an instance of the form to be used in this view."""
    #     if form_class is None:
    #         form_class = self.get_form_class()
    #     return form_class(**self.get_form_kwargs())

    
    def get_object(self):
        obj = self.request.user
        print('>>>>>>>>>>>>>>>>>>>>obj>>>>>>>=', obj)
        return obj
