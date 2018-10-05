from django.db import models




'''
TodoList
| id | name |
| 1  | grocery list |
| 2  | career list |

TodoListItem

 V primary key              V foreign key
| id | text            | TodoListID |
| 1  | apples          | 1          |
| 2  | watermelons     | 1          |
| 3  | get a job       | 2          |
| 4  | bread           | 1          |
| 5  | update resume   | 2          |
| 6  | update linkedin | 2          |


'''







class TodoList(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class TodoListItem(models.Model):
    text = models.CharField(max_length=100)
    todolist = models.ForeignKey(TodoList, on_delete=models.CASCADE, related_name='items')

    created_date = models.DateTimeField(auto_now_add=True)
    completed_date = models.DateTimeField(null=True, blank=True)

    def is_completed(self):
        return self.completed_date is not None

    def __str__(self):
        return self.text









