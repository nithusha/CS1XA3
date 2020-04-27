from django.http import HttpResponse,HttpResponseNotFound
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages

from . import models

from social.forms import UpdateUserInfoForm, InterestForms

def messages_view(request):
    """Private Page Only an Authorized User Can View, renders messages page
       Displays all posts and friends, also allows user to make new posts and like posts
    Parameters
    ---------
      request: (HttpRequest) - should contain an authorized user
    Returns
    --------
      out: (HttpResponse) - if user is authenticated, will render private.djhtml
    """
    if request.user.is_authenticated:
        user_info = models.UserInfo.objects.get(user=request.user)

        otherpplpost = models.Post.objects.order_by('-timestamp')
        
        for post in otherpplpost:
            likes  = post.likes.all()
            if user_info in likes:
                post.liked_yn = True
            else:
                post.liked_yn = False
        
        posts = otherpplpost
        # TODO Objective 10: check if user has like post, attach as a new attribute to each post
        request.session['count1'] = request.session.get('count1', 1)
        context = { 'user_info' : user_info
                  , 'posts' : posts }
        return render(request,'messages.djhtml',context)

    request.session['failed'] = True
    return redirect('login:login_view')

def account_view(request):
    """Private Page Only an Authorized User Can View, allows user to update
       their account information (i.e UserInfo fields), including changing
       their password
    Parameters
    ---------
      request: (HttpRequest) should be either a GET or POST
    Returns
    --------
      out: (HttpResponse)
                 GET - if user is authenticated, will render account.djhtml
                 POST - handle form submissions for changing password, or User Info
                        (if handled in this view)
    """
    if request.user.is_authenticated:        
        if request.method == 'POST':
            form = PasswordChangeForm(request.user, request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)
          
        form = PasswordChangeForm(request.user)        
        
        user_info = models.UserInfo.objects.get(user=request.user)
        context = { 'user_info' : user_info,
                'change_form' : form }
        return render(request,'account.djhtml',context)

    request.session['failed'] = True
    return redirect('login:login_view')


def update_user_view(request):

    if request.user.is_authenticated:
        if request.method == 'POST' and 'update' in request.POST:
            updateform = UpdateUserInfoForm(request.POST, request.user)
            if updateform.is_valid():
                employment = updateform.cleaned_data['employment']
                location = updateform.cleaned_data['location']
                birthday = updateform.cleaned_data['birthday']
                user_info = models.UserInfo.objects.get(user=request.user)
                if not employment:
                    pass
                else:
                    user_info.employment = employment

                if not birthday:
                    pass
                else:
                    user_info.birthday = birthday

                if not location:
                    pass
                else:
                    user_info.location = location

                user_info.save()
                return redirect('social:update_user_view')
        
        if request.method == 'POST' and 'interest' in request.POST:
            updateinterestform = InterestForms(request.POST, request.user)
            if updateinterestform.is_valid():
                unstripped_ints = updateinterestform.cleaned_data['interests']
                ints = [x.strip() for x in unstripped_ints.split(',')]
                user_info = models.UserInfo.objects.get(user=request.user)
                if not ints:
                    pass
                else:
                    for i in ints:
                        if models.Interest.objects.filter(label__iexact=i):
                            int_instance = models.Interest.objects.filter(label__iexact=i)
                        else:
                            int_instance = models.Interest.objects.create(label = i)
                        
                        user_info.interests.add(int_instance)
                return redirect('social:update_user_view')
    

        userupdateform = UpdateUserInfoForm(request.POST)       
        userinterestform = InterestForms(request.POST)
        user_info = models.UserInfo.objects.get(user=request.user)
        context = { 'user_info' : user_info,
                'update_form' : userupdateform,
                'interest_form' : userinterestform }
        return render(request,'updateuser.djhtml',context)
    
def people_view(request):
    """Private Page Only an Authorized User Can View, renders people page
       Displays all users who are not friends of the current user and friend requests
    Parameters
    ---------
      request: (HttpRequest) - should contain an authorized user
    Returns
    --------
      out: (HttpResponse) - if user is authenticated, will render people.djhtml
    """
    if request.user.is_authenticated:

        user_info = models.UserInfo.objects.get(user=request.user)
        friends = user_info.friends.all()
        allusers = models.UserInfo.objects.exclude(user=request.user)
        notfriends = allusers.difference(friends)

        all_people = notfriends

        request.session['count'] = request.session.get('count', 1)

        friendrequests = models.FriendRequest.objects.filter(to_user=user_info)
        friend_requests = friendrequests

        myrequests = models.FriendRequest.objects.filter(from_user = user_info)
        
        allrelations = []
        for req in friendrequests:
            allrelations.append(req.from_user)
        for req in myrequests:
            allrelations.append(req.to_user)

        context = { 'user_info' : user_info,
                    'all_people' : all_people,
                    'friend_requests' : friend_requests,
                    'allrelations' : allrelations
                    }

        return render(request,'people.djhtml',context)

    request.session['failed'] = True
    return redirect('login:login_view')

def like_view(request):
    '''Handles POST Request recieved from clicking Like button in messages.djhtml,
       sent by messages.js, by updating the corrresponding entry in the Post Model
       by adding user to its likes field
    Parameters
	----------
	  request : (HttpRequest) - should contain json data with attribute postID,
                                a string of format post-n where n is an id in the
                                Post model

	Returns
	-------
   	  out : (HttpResponse) - queries the Post model for the corresponding postID, and
                             adds the current user to the likes attribute, then returns
                             an empty HttpResponse, 404 if any error occurs
    '''
    postIDReq = request.POST.get('postID')
    otherpplpost = models.Post.objects.order_by('-timestamp')

    if postIDReq is not None:
        # remove 'post-' from postID and convert to int
        # TODO Objective 10: parse post id from postIDReq
        postID = int(postIDReq[5:])
        postkey = otherpplpost[postID]
        if request.user.is_authenticated:
            # TODO Objective 10: update Post model entry to add user to likes field
            user_info = models.UserInfo.objects.get(user = request.user)
            postkey.likes.add(user_info)

            # return status='success'
            return HttpResponse()
        else:
            return redirect('login:login_view')

    return HttpResponseNotFound('like_view called without postID in POST')

def post_submit_view(request):
    '''Handles POST Request recieved from submitting a post in messages.djhtml by adding an entry
       to the Post Model
    Parameters
	----------
	  request : (HttpRequest) - should contain json data with attribute postContent, a string of content

	Returns
	-------
   	  out : (HttpResponse) - after adding a new entry to the POST model, returns an empty HttpResponse,
                             or 404 if any error occurs
    '''
    postContent = request.POST.get('postContent')
    if postContent is not None:
        if request.user.is_authenticated:

            user_info = models.UserInfo.objects.get(user = request.user)

            models.Post.objects.create(owner = user_info, content = postContent)

            # return status='success'
            return HttpResponse()
        else:
            return redirect('login:login_view')

    return HttpResponseNotFound('post_submit_view called without postContent in POST')

def more_post_view(request):
    '''Handles POST Request requesting to increase the amount of Post's displayed in messages.djhtml
    Parameters
	----------
	  request : (HttpRequest) - should be an empty POST

	Returns
	-------
   	  out : (HttpResponse) - should return an empty HttpResponse after updating hte num_posts sessions variable
    '''
    if request.user.is_authenticated:
        request.session['count1'] = request.session['count1'] + 1

        # return status='success'
        return HttpResponse()

    return redirect('login:login_view')

def more_ppl_view(request):
    '''Handles POST Request requesting to increase the amount of People displayed in people.djhtml
    Parameters
	----------
	  request : (HttpRequest) - should be an empty POST

	Returns
	-------
   	  out : (HttpResponse) - should return an empty HttpResponse after updating the num ppl sessions variable
    '''
    if request.user.is_authenticated:
        request.session['count'] = request.session['count'] + 1

        return HttpResponse()

    return redirect('login:login_view')

def friend_request_view(request):
    '''Handles POST Request recieved from clicking Friend Request button in people.djhtml,
       sent by people.js, by adding an entry to the FriendRequest Model
    Parameters
	----------
	  request : (HttpRequest) - should contain json data with attribute frID,
                                a string of format fr-name where name is a valid username

	Returns
	-------
   	  out : (HttpResponse) - adds an etnry to the FriendRequest Model, then returns
                             an empty HttpResponse, 404 if POST data doesn't contain frID
    '''
    frID = request.POST.get('frID')
    if frID is not None:
        # remove 'fr-' from frID
        username = frID[3:]

        if request.user.is_authenticated:
            friend = models.User.objects.get(username = username)
            friend_info = models.UserInfo.objects.get(user = friend)
            user_info = models.UserInfo.objects.get(user = request.user)
            #allfriendrequests = models.FriendRequest.objects.filter(to_user = user_info)
            models.FriendRequest.objects.create(to_user = friend_info, from_user = user_info )

            return HttpResponse()
        else:
            return redirect('login:login_view')

    return HttpResponseNotFound('friend_request_view called without frID in POST')

def accept_decline_view(request):
    '''Handles POST Request recieved from accepting or declining a friend request in people.djhtml,
       sent by people.js, deletes corresponding FriendRequest entry and adds to users friends relation
       if accepted
    Parameters
	----------
	  request : (HttpRequest) - should contain json data with attribute decision,
                                a string of format A-name or D-name where name is
                                a valid username (the user who sent the request)

	Returns
	-------
   	  out : (HttpResponse) - deletes entry to FriendRequest table, appends friends in UserInfo Models,
                             then returns an empty HttpResponse, 404 if POST data doesn't contain decision
    '''
    data = request.POST.get('decision')
    if data is not None:
        # TODO Objective 6: parse decision from data
        dec = data[0]
        username = data[2:]
        friend = models.User.objects.get(username = username)
        friend_info = models.UserInfo.objects.get(user = friend)
        user_info = models.UserInfo.objects.get(user = request.user)
        requestobject = models.FriendRequest.objects.filter(to_user = user_info, from_user = friend_info)
        requestobject.delete()
        if request.user.is_authenticated:
            if dec == 'A':
                user_info.friends.add(friend_info)
                friend_info.friends.add(user_info)


            # TODO Objective 6: delete FriendRequest entry and update friends in both Users

            # return status='success'
            return HttpResponse()
        else:
            return redirect('login:login_view')

    return HttpResponseNotFound('accept-decline-view called without decision in POST')
