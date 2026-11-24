def normalize_answers(answers):
    return [answer.strip().lower() for answer in (answers or [])]




def calculate_by_category():
    category_totals = {}
    for expense in expenses:
        expense_cat = expense["category"]
        if expense["category"] in category_totals:
            category_totals[expense_cat] += expense["amount"]

        else:
             category_totals[expense_cat] = expense["amount"]
    return category_totals



def find_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            return task
    return None




def count_correct(questions, answers):
    count = 0
    #for i in range(len(answers)):
        #if questions[i]["answer"] == answers[i]:
    for question, answers in zip(questions, answers):
        if question["answer"] == answers:
            count += 1
    return count         


def pending_task[tasks]:
    return[tasks for task in tasks if task["completed"] == False]




return dict (counter(book["author"] for (book in books or [])))


def count_by_author(books):
    count = {}
    for book in books:
        author = book["author"]
        counts[author] = counts.get(author,0) + 1
    return counts   


def total_spending(expenses):
    """Return the """
    total = 0
    for expense in expenses:
        total += expense["amount"]
    return total    