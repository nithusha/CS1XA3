/* ********************************************************************************************
   | Handle Submitting Posts - called by $('#post-button').click(submitPost)
   ********************************************************************************************
   */
function submitResponse(data, status) {
    if (status == 'success') {
        // reload page to display new Post
        location.reload();
    }
    else {
        alert('Post Button Pressed' + status);
    }
}

function submitPost(event) {
    let postcontent = $('#post-text').text();
    let json_data = { 'postContent' : postcontent };
    // globally defined in messages.djhtml using i{% url 'social:like_view' %}
    let url_path =  post_submit_url;

    // AJAX post
    $.post(url_path,
           json_data,
           submitResponse);
    // TODO Objective 8: send contents of post-text via AJAX Post to post_submit_view (reload page upon success)
}

/* ********************************************************************************************
   | Handle Liking Posts - called by $('.like-button').click(submitLike)
   ********************************************************************************************
   */

function likeResponse(data,status) {
    if (status == 'success') {
        // reload page to display new Post
        location.reload();
    }
    else {
        alert('Like Button Pressed' + status);
    }

}
function submitLike(event) {

    let postID = event.target.id;
    let json_data = { 'postID' : postID };
    // globally defined in messages.djhtml using i{% url 'social:like_view' %}
    let url_path = like_post_url;

    // AJAX post
    $.post(url_path,
           json_data,
           likeResponse);
    
    // TODO Objective 10: send post-n id via AJAX POST to like_view (reload page upon success)
}

/* ********************************************************************************************
   | Handle Requesting More Posts - called by $('#more-button').click(submitMore)
   ********************************************************************************************
   */
function moreResponse(data,status) {
    if (status == 'success') {
        // reload page to display new Post
        location.reload();
    }
    else {
        alert('failed to request more posts' + status);
    }
}

function submitMore(event) {
    // submit empty data
    let json_data = { };
    // globally defined in messages.djhtml using i{% url 'social:more_post_view' %}
    let url_path = more_post_url;

    // AJAX post
    $.post(url_path,
           json_data,
           moreResponse);
}

/* ********************************************************************************************
   | Document Ready (Only Execute After Document Has Been Loaded)
   ********************************************************************************************
   */
$(document).ready(function() {
    // handle post submission
    $('#post-button').click(submitPost);
    // handle likes
    $('.like-button').click(submitLike);
    // handle more posts
    $('#more-button').click(submitMore);
});
