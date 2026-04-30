"""
Smart Task Scheduler using Greedy Algorithm
============================================
Team Members:
- Sankeerthana   : AP24110011114
- Keerthana A    : AP24110011113
- Shruthi V      : AP24110011116
- P. Sadiya      : AP24110011194
- I. Vyshnavi    : AP24110011003
"""

class Task:
    def __init__(self, task_id, name, deadline, profit):
        self.task_id = task_id
        self.name = name
        self.deadline = deadline  # deadline in units (e.g., hours/days)
        self.profit = profit      # profit/priority of the task

    def __repr__(self):
        return f"Task({self.name}, Deadline={self.deadline}, Profit={self.profit})"


def greedy_task_scheduler(tasks):
    """
    Greedy Algorithm for Task Scheduling (Job Sequencing Problem).
    Selects tasks to maximize total profit within deadlines.
    
    Args:
        tasks (list): List of Task objects
    
    Returns:
        tuple: (selected_tasks, total_profit)
    """
    # Sort tasks by profit in descending order (Greedy choice)
    tasks_sorted = sorted(tasks, key=lambda x: x.profit, reverse=True)

    max_deadline = max(task.deadline for task in tasks)
    
    # Time slots (1-indexed), None means free
    slots = [None] * (max_deadline + 1)
    
    selected_tasks = []
    total_profit = 0

    for task in tasks_sorted:
        # Find the latest available slot before or at the deadline
        for slot in range(min(task.deadline, max_deadline), 0, -1):
            if slots[slot] is None:
                slots[slot] = task
                selected_tasks.append(task)
                total_profit += task.profit
                break

    return selected_tasks, total_profit


def display_schedule(selected_tasks, total_profit):
    """Display the scheduled tasks in a readable format."""
    print("\n" + "="*50)
    print("       SMART TASK SCHEDULER - GREEDY ALGORITHM")
    print("="*50)
    
    if not selected_tasks:
        print("No tasks could be scheduled.")
        return

    print(f"\n{'ID':<6} {'Task Name':<20} {'Deadline':<12} {'Profit':<10}")
    print("-" * 50)
    for task in selected_tasks:
        print(f"{task.task_id:<6} {task.name:<20} {task.deadline:<12} {task.profit:<10}")
    
    print("-" * 50)
    print(f"Total Tasks Scheduled : {len(selected_tasks)}")
    print(f"Total Profit Earned   : {total_profit}")
    print("="*50 + "\n")


def main():
    # Sample tasks: (id, name, deadline, profit)
    task_data = [
        (1, "Design UI",        2, 100),
        (2, "Write Report",     1, 50),
        (3, "Fix Bug",          2, 200),
        (4, "Code Review",      1, 20),
        (5, "Deploy App",       3, 150),
        (6, "Write Tests",      2, 80),
        (7, "Update Docs",      3, 60),
        (8, "Client Meeting",   1, 90),
    ]

    tasks = [Task(t[0], t[1], t[2], t[3]) for t in task_data]

    print("\nAll Available Tasks:")
    print(f"{'ID':<6} {'Task Name':<20} {'Deadline':<12} {'Profit':<10}")
    print("-" * 50)
    for task in tasks:
        print(f"{task.task_id:<6} {task.name:<20} {task.deadline:<12} {task.profit:<10}")

    selected_tasks, total_profit = greedy_task_scheduler(tasks)
    display_schedule(selected_tasks, total_profit)


if __name__ == "__main__":
    main()
