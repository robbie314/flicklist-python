<!DOCTYPE html>
<html>
    <head>
    </head>
    <body>

    </body>
</html>
'''

<form>
<form action="/add" method="post">
    <label>
        I want to add
        <input type = "text" name="new-movie"/>
    </label>
    <input type ="submit" value="Add it/>"
</form>

<form action = "/cross-off" method="post"
<label>
    I want ot cross off
    <select name = "crossed-off-movie"/>
    {% for movie in movies %}

        <option value= "{{movie}}"{{movie}}</option>
