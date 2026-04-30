# Smart Task Scheduler using Greedy Algorithm

## Project Overview
This project implements a **Smart Task Scheduler** using the **Greedy Algorithm** (Job Sequencing Problem). It schedules tasks to maximize total profit while respecting deadlines.

---

## Team Members

| Name           | Registration Number |
|----------------|---------------------|
| Sankeerthana   | AP24110011114       |
| Keerthana A    | AP24110011113       |
| Shruthi V      | AP24110011116       |
| P. Sadiya      | AP24110011194       |
| I. Vyshnavi    | AP24110011003       |

---

## Algorithm Used
**Greedy Algorithm - Job Sequencing Problem**

### How It Works:
1. Sort all tasks in **descending order of profit**.
2. For each task, find the **latest available time slot** before or on its deadline.
3. If a free slot is found, schedule the task there.
4. Repeat until all tasks are processed.

### Time Complexity:
- Sorting: `O(n log n)`
- Slot assignment: `O(n * d)` where `d` is the maximum deadline

### Space Complexity:
- `O(d)` for time slots array

---

## Files
| File | Description |
|------|-------------|
| `smart_task_scheduler.py` | Main Python implementation |
| `README.md` | Project documentation |

---

## How to Run

### Prerequisites
- Python 3.x installed

### Steps
```bash
# Clone the repository
git clone <your-repo-url>

# Navigate to the project folder
cd smart-task-scheduler

# Run the program
python smart_task_scheduler.py
```

---

## Sample Output
```
All Available Tasks:
ID     Task Name            Deadline     Profit    
--------------------------------------------------
1      Design UI            2            100       
2      Write Report         1            50        
3      Fix Bug              2            200       
...

==================================================
       SMART TASK SCHEDULER - GREEDY ALGORITHM
==================================================

ID     Task Name            Deadline     Profit    
--------------------------------------------------
3      Fix Bug              2            200       
5      Deploy App           3            150       
1      Design UI            1            100       
8      Client Meeting       1            90        
--------------------------------------------------
Total Tasks Scheduled : 4
Total Profit Earned   : 540
==================================================
```

---

## Concepts Covered
- Greedy Algorithm
- Job Sequencing with Deadlines
- Time Slot Management
- Python OOP (Classes and Methods)

---

## Course
**Data Structures and Algorithms (DSA)**  
Academic Year: 2024-25
