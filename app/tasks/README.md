### Here are the different tasks for creating or updating data in the database.
Notice that we have Tasks for Data Creation and Data updating. 
It's done like this to avoid rewriting the database each time using we want to update some entries. 
So those creation tasks are meant to be executed first and just once. 
After that, the updating tasks is better recommended to update the database.
```bash
craft schedule:run --task the_name_of_the_task
```
