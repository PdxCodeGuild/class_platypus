from django.db import models




# The user should be presented with an input field and a button (in a form). When they click the button, it should save the data to the server and show the newly-added item in the list.

class TodoItem(models.Model):
    # text description
    list_item = models.CharField(max_length=200)
    # created date
    created_date = models.DateTimeField('date created')
    # completed date
    completed_date = models.DateTimeField('date completed')
    # boolean representing completion
    item_complete = models.BooleanField(default=False)
