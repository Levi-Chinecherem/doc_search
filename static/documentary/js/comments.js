$(document).ready(function() {
    // Submit comment
    $('#comment-form').on('submit', function(e) {
      e.preventDefault();
      var commentContent = $('#comment-textarea').val();
      
      $.ajax({
        type: 'POST',
        url: '{% url 'submit_comment' documentary.id %}',
        data: {
          'content': commentContent,
          'csrfmiddlewaretoken': '{{ csrf_token }}'
        },
        success: function(response) {
          // Clear comment textarea
          $('#comment-textarea').val('');
          
          // Show success notification
          showNotification('Comment submitted successfully.');
          
          // Add new comment to the comments list
          var commentItem = $('<li class="comment-item">' +
                                '<h4>{{ request.user }}</h4>' +
                                '<p>' + commentContent + '</p>' +
                                '<button class="reply-btn" data-comment-id="{{ response.comment_id }}">Reply</button>' +
                                '<div class="comment-reply" id="reply-form-{{ response.comment_id }}" style="display: none;">' +
                                  '<textarea class="reply-textarea" rows="3" cols="50" placeholder="Write a reply"></textarea>' +
                                  '<button class="submit-reply-btn" data-comment-id="{{ response.comment_id }}">Submit Reply</button>' +
                                '</div>' +
                                '<ul class="replies-list"></ul>' +
                              '</li>');
          $('.comments-list').append(commentItem);
        },
        error: function(xhr, errmsg, err) {
          // Show error notification
          showNotification('Error submitting comment. Please try again.');
        }
      });
    });
    
    // Submit reply
    $(document).on('submit', '.comment-reply', function(e) {
      e.preventDefault();
      var replyContent = $(this).find('.reply-textarea').val();
      var commentId = $(this).find('.submit-reply-btn').data('comment-id');
      
      $.ajax({
        type: 'POST',
        url: '{% url 'submit_reply' documentary.id %}',
        data: {
          'content': replyContent,
          'comment_id': commentId,
          'csrfmiddlewaretoken': '{{ csrf_token }}'
        },
        success: function(response) {
          // Clear reply textarea
          $('#reply-form-' + commentId).find('.reply-textarea').val('');
          
          // Show success notification
          showNotification('Reply submitted successfully.');
          
          // Add new reply to the replies list of the comment
          var replyItem = $('<li class="reply-item">' +
                              '<p><strong>{{ request.user }}:</strong> ' + replyContent + '</p>' +
                            '</li>');
          $('#reply-form-' + commentId).siblings('.replies-list').append(replyItem);
        },
        error: function(xhr, errmsg, err) {
          // Show error notification
          showNotification('Error submitting reply. Please try again.');
        }
      });
    });
    
    // Show notification popup
    function showNotification(message) {
      // Replace with your own notification implementation (e.g., Bootstrap modal, toast notification, etc.)
      alert(message);
    }
  });
  