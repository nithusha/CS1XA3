# CS1XA3 Project 03
#### Nithusha Sivakumar | sivakumn | 400088188

## Usage

Install conda environment with:
`conda activate djangoenv`

Run locally with:
`python manage.py runserver localhost:8000`

Run on mac1xa3.ca with:
`python manage.py runserver localhost:10096`

Login using these credentials:
Username: TestUser
Password: 1234

## Objective 01: Complete Login and SignUp Pages

**Description:**
The login page has already been completed:
- this feature is displayed in [login.djhtml](https://github.com/nithusha/CS1XA3/blob/master/Project03/login/templates/login.djhtml) which is rendered by login_view
- it makes a POST Request to /e/sibakumn/ which is handled by login_view
- if authentication is successful, ie. user exists and correct credentials are put in, it redirects to /e/sibakumn/social/messages/ which is rendered by messages_view

The signup page:
- this feature is displayed in [signup.djhtml](https://github.com/nithusha/CS1XA3/tree/master/Project03) which is rendered by signup_view
- signup.djhtml contains an empty `UserCreationForm()`
- it makes a POST Request to /e/sibakumn/create/ which is handled by create_view
- create_view creates a new user using the username and password provided from `UserCreationForm()`
- if authentication is successful, satisfies conditions of the password, username isn't taken, etc., it redirects to /e/sibakumn/social/messages/ 

**Exception:**
- if /e/sibakumn/ is called without arguments, it redirects to login.djhtml
- if incorrect username or password provided for login, it redirects to login.djhtml
- if authentication of user in signup is unsuccessful, signup_failed message thrown: Username or Password didn't meet requirements. Please try again.

## Objective 02: Adding User Profile and Interests

**Description:**
- this feature is displayed in social_base.djhtml which renders messages.djhtml, people.djhtml and account.djhtml which is rendered by messages_view, people_view and account_view respectively
- for adding user profile and interests, social_base.djhtml is rendered by account_view and update_user_view

## Objective 03: Account Settings Page

**Description:**
- this feature is displayed in account.djhtml and updateuser.djhtml rendered by account_view and update_user_view
- the ChangePassword button makes a POST Request to /e/sibakumn/social/account/ which is rendered by account_view
- a modal which is rendered by account_view pops up and allows users to change their password using PasswordChangeForm()
- the Update User Info button redirects to /e/sibakumn/social/userinfo/ which is rendered by update_user_view and displayed in updateuser.djhtml
- it makes a POST Request to /e/sibakumn/social/userinfo/ which is handled by update_user_view 
    - if request.POST == 'update', ie. when user clicks Update button, then it creates a UpdateUserInfoForm() which is a custom form in forms.py and updates UserInfo object as needed for employment, birthday and interest
    - if request.POST == 'interest', ie. when user clicks Add Interest button, then it creates a InterestForms() which is a custom form in forms.py and updates the class Interest and adds instance of this interest to the UserInfo object
- it then redirects to /e/sibakumn/social/account displaying the updated info

**Exception:**
- if birthday is not typed in the format as given, then no changes will be rendered, the Update button simply refreshes the page
- if user is not authenticated then /e/sibakumn/social/account/ will redirect to login.djhtml

## Objective 04: Displaying People List

**Description:**
- this feature is displayed in people.djhtml which is rendered by people_view
    - the people displayed in people.djhtml are all Users in the database that are not friends with the logged in user
    - if a friend request exists between the user and any other users in the database, the friendrequest button is disabled
- it sends an AJAX POST Request from people.js to /e/sibakumn/social/moreppl/ which is handled by more_ppl_view 
    - more_ppl_view uses a session variable to increment how many people are displayed in people.djhtml and refreshes page on success

**Exception:**
- if user is not authenticated, then /e/sibakumn/social/people/ will redirect to login.djhtml

## Objective 05: Sending Friend Requests

**Description:**
- this feature is displayed in people.djhtml which is rendered by friend_request_view
- it sends an AJAX POST Request from people.js to /e/sibakumn/social/friendrequest/ which is handled by friend_request_view
    - creates a FriendRequest object in the database and reloads on success

**Exception:**
- if user is not authenticated then /e/sibakumn/social/friend_request_view/ will redirect to login.djhtml

## Objective 06: Accepting / Declining Friend Requests

**Description:**
- this feature is displayed in people.djhtml which is rendered by friend_request_view
- the Accept/Decline buttons send an AJAX POST Request from people.js to /e/sibakumn/social/acceptdecline/ which is handled by accept_decline_view
    - the FriendRequest instance is deleted from the FriendRequest model
    - if A was in the id sent to accept_decline_view, users are added to each other's friend list 

**Exception:**
- if user is not authenticated then /e/sibakumn/social/accept_decling_view/ will redirect to login.djhtml

## Objective 07: Displaying Friends

**Description:**
- this feature is displayed in messages.djhtml which is rendered by messages_view
    - to display all friends, messages.djhml iterates through all User objects in user's friend list

**Exception:**
- if user is not authenticated then /e/sibakumn/social/messages/ redirects to login.djhml

## Objective 08: Submitting Posts

**Description:**
- this feature is displayed in messages.djhtml which is rendered by messages_view
- when post-button is clicked, it sends an AJAX POST Request from messages.js to /e/sibakumn/social/postsubmit/ which is handled by post_submit_view
    - post-submit-view gets post-content from messages.js and creates an instance of the Post model

**Exception:**
- if user is not authenticated, then /e/sibakumn/social/postsubmit/ redirects to login.djhtml

## Objective 09: Displaying Post List

**Description:**
- this feature is displayed in messages.djhtml which is rendered by messages_view
    - messages_view queries through all Post objects, including those that are not friends and displays them from newest to oldest
- it sends an AJAX POST Request from messages.js to /e/sibakumn/social/morepost/ which is handled by more_post_view 
    - more_post_view uses a session variable to increment how many posts are displayed in messages.djhtml and refreshes page on success

**Exception:**
- if user is not authenticated then /e/sibakumn/social/messages/ will redirect to login.djhtml
- if user is not authenticated, then /e/sibakumn/social/morepost/ will also redirect to login.djhtml

## Objective 10: Liking Posts and Displaying Like Count

**Description:**
- this feature is displayed in messages.djhtml which is rendered by messages_view
- when post-{{forloop.counter0}} button is clicked  it send an AJAX POST Request from messages.js to /e/sibakumn/social/like/ whih is handled by like_view
    - like_view adds the user to the list of users who have liked the post, by querying through all Posts and using the counter within the POST Request to find the right post
    - the button is disabled if the user is already in the list of users who have liked the post and is handled by messages_view by setting an extra boolean attribute 
    - once clicked, the page refreshes on success and disables the like button 
**Exception:**
- if user is not authenticated then /e/sibakumn/social/like_view/ redirects to login.djhtml 

## Objective 11: Create a Test Database 

**Description:**
There are 20 Test Users in this Database. These are their usernames and credentials .

| Username | Password |
| -------- | ------- |
| TestUser-01 | `1234-01student` |
| TestUser-02 | `1234-02student` |
| TestUser-03 | `1234-03student` |
| TestUser-04 | `1234-04student` |
| TestUser-05 | `1234-05student` |
| TestUser-06 | `1234-06student` |
| TestUser-07 | `1234-07student` |
| TestUser-08 | `1234-08student` |
| TestUser-09 | `1234-09student` |
| TestUser-10 | `1234-10student` |
| TestUser-11 | `1234-11student` |
| TestUser-12 | `1234-12student` |
| TestUser-13 | `1234-13student` |
| TestUser-14 | `1234-14student` |
| TestUser-15 | `1234-15student` |
| TestUser-16 | `1234-16student` |
| TestUser-17 | `1234-17student` |
| TestUser-18 | `1234-18student` |
| TestUser-19 | `1234-19student` |
| TestUser-20 | `1234-20student` |


