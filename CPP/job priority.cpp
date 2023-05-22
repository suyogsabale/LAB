#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// Structure to represent a job
struct Job {
    int jobId;
    int burstTime;
    int priority;

    Job(int id, int burst, int prio) : jobId(id), burstTime(burst), priority(prio) {}
};

// Function to compare jobs based on their priority
bool compareJobs(const Job& job1, const Job& job2) {
    // Higher priority jobs have lower priority numbers
    return job1.priority < job2.priority;
}

// Function to schedule jobs based on priority
void scheduleJobs(vector<Job>& jobs) {
    // Sort the jobs based on their priority (in ascending order)
    sort(jobs.begin(), jobs.end(), compareJobs);

    int totalWaitingTime = 0;
    int currentTime = 0;

    for (const Job& job : jobs) {
        // Calculate waiting time for the current job
        int waitingTime = currentTime;
        totalWaitingTime += waitingTime;

        // Update current time and execute the job
        currentTime += job.burstTime;
        cout << "Job ID: " << job.jobId << ", Burst Time: " << job.burstTime << ", Priority: " << job.priority << ", Waiting Time: " << waitingTime << endl;
    }

    // Calculate average waiting time
    double averageWaitingTime = static_cast<double>(totalWaitingTime) / jobs.size();
    cout << "Average Waiting Time: " << averageWaitingTime << endl;
}

int main() {
    int numJobs;
    cout << "Enter the number of jobs: ";
    cin >> numJobs;

    vector<Job> jobs;

    for (int i = 0; i < numJobs; i++) {
        int jobId, burstTime, priority;
        cout << "Enter details for Job " << i + 1 << ":" << endl;
        cout << "Job ID: ";
        cin >> jobId;
        cout << "Burst Time: ";
        cin >> burstTime;
        cout << "Priority: ";
        cin >> priority;
        jobs.push_back(Job(jobId, burstTime, priority));
    }

    cout << "Job Scheduling Results:" << endl;
    scheduleJobs(jobs);

    return 0;
}
