from django.shortcuts import render, redirect
from crudSystem.models import Member
from django.contrib import messages


def home(request):
    return render(request, 'index.html')

def register_members(request):
    if request.method == 'POST':
        member_firstname = request.POST['m-fname']
        member_secondname = request.POST['m-sname']
        member_idno = request.POST['m-idno']
        member_mobileno = request.POST['m-mobileno']
        member_dateofbirth = request.POST['m-dateofbirth']

        data = Member(first_name=member_firstname, second_name=member_secondname, id_no=member_idno,
                      mobile_no=member_mobileno, date_of_birth=member_dateofbirth)
        data.save()
        messages.success(request, 'Member added successfully')
        return redirect('register_members-url')
    return render(request, 'register-members.html')

def all_members(request):
    members = Member.objects.all()
    context = {'members': members}
    return render(request, 'all-members.html', context)

def delete_member(request,id):
    member = Member.objects.get(id=id)
    member.delete()
    messages.success(request, 'Member deleted successfully')
    return redirect('all_members')