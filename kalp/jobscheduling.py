def schedule_jobs(jobs):
    # Sort the jobs in non-decreasing order of their finish times
    jobs.sort(key=lambda x: x[1])

    n = len(jobs)
    result = []
    result.append(jobs[0])

    prev_finish = jobs[0][1]

    for i in range(1, n):
        job_start = jobs[i][0]
        job_finish = jobs[i][1]

        # Check if the job can be scheduled
        if job_start >= prev_finish:
            result.append(jobs[i])
            prev_finish = job_finish

    return result


# Take input from the user
n = int(input("Enter the number of jobs: "))
jobs = []

print("Enter the start and finish time of each job:")

for _ in range(n):
    start, finish = map(int, input().split())
    jobs.append((start, finish))

scheduled_jobs = schedule_jobs(jobs)

print("Scheduled jobs:")
for job in scheduled_jobs:
    print("Start Time:", job[0], "Finish Time:", job[1])
