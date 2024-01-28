import html

def write_html(posts_with_comments=[]):
    # TODO: get all the posts and their comments
    #       chop up the below html and loop through the posts and comments to create 
    #       the page using content from the database

    # Sort posts in reverse chronological order
    posts_with_comments.sort(key=lambda x: x['id'], reverse=True)

    # Initialize the HTML string
    html_content = """<html>
<head>
  <title>Exercise 3 - A Web Journal</title>
  <link rel="stylesheet" type="text/css" href="css/style.css">
  <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
</head>
<body>
  <div class="compose-button">
    <a href="post" title="create post">
      <i class="material-icons">create</i>
    </a>
  </div>

  <h1>Yuzhuo's Web Journal</h1>

  <div id="posts">"""

    # Loop through the posts_with_comments and generate HTML for each post
    for post in posts_with_comments:
        html_content += f"""
    <post class="post" id="post_{post['id']}">
      <h2 class=post-title id="post_title_{post['id']}">
        {html.escape(post['title'])}
        <a href="#post_title_{post['id']}">
          <i class="material-icons">link</i>
        </a>
      </h2>

      <div class="post-body">
        {html.escape(post['body'])}
      </div>

      <h3>{len(post['comments'])} Comments</h3>
      <div class="comment-block">"""

        # Sort comments in chronological order
        post['comments'].sort(key=lambda x: x['id'])

        # Loop through comments and generate HTML for each comment
        for comment in post['comments']:
            html_content += f"""
        <comment>
          <div class="comment-body">
           {html.escape((comment['body']))}
          </div>
          <div class="comment-author">
            {html.escape(comment['author'])}
          </div>
        </comment>"""

        # Add a link to leave a comment
        html_content += f"""
        <a href="comment?post_id={post['id']}">
          <i class="material-icons">create</i>
          Leave a comment
        </a>
      </div>
    </post>"""

    # Close the HTML string
    html_content += """</div> <!-- end of posts block -->
</body>
</html>"""
    
    return html_content