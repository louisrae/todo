from todo import app


def main():
    while True:
        action = input("What do you want to do? ")
        t = app.Todo("active.csv", "archive.csv")

        if action == "a":
            name = input("What is the name of the task? ")
            category = input("What is the category of the task? ")
            notes = input("Any Notes? ")
            t.add_task(name, category, notes)
        elif action == "ls":
            t.show_tasks()
        elif action == "d":
            d = input("What task name do you want to delete? ")
            t.delete_task(d)
        else:
            break


main()
