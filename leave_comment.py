import html
def write_html(post={}):
    # TODO: Display the post the user is commenting on, and the existing comments

    # Initialize HTML content
    html_content = f"""<html>
<head>
    <title>Leave a Comment</title>
    <link rel="stylesheet" type="text/css" href="css/style.css">
    <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
</head>
<body>
    <h1>Yuzhuo's Web Journal</h1>
    <div class="leave-comment">
        <div class="post-body">
            {html.escape(post['body'])}
        </div>
        <h2>
            Leave a Comment on
            <a href="#{html.escape(post['title'])}">
                {html.escape(post['title'])}
            </a>
        </h2>

        <div class="post-body">
            <!-- Display existing comments -->
            <h3>Existing Comments</h3>
            <div class="comment-block">"""

    # Sort comments in chronological order
    post['comments'].sort(key=lambda x: x['id'])

    # Loop through comments and generate HTML for each comment
    for comment in post['comments']:
        html_content += f"""
        <comment>
            <div class="comment-body">
                {html.escape(comment['body']) if comment['body'] is not None else ''}
            </div>
            <div class="comment-author">
                {html.escape(comment['author']) if comment['author'] is not None else ''}
            </div>
        </comment>"""

    # Add the closing tags and the form for leaving a new comment
    html_content += f"""
            </div>
        </div>

        <form method="post">
            <label for="body">Comment</label>
            <textarea name="body"></textarea>
            <label for="name">Your name</label>
            <input name="name"></input>
            <input type="hidden" name="post_id" value="{post['id']}"></input>
            <input type="submit" name="submit" value="Leave Comment"></input>
        </form>
    </div>
    <a href="/">Home</a>
</body>
</html>"""

    return html_content
