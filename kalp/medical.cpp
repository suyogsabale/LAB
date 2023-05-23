#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>
#include <string>
#include <cstdlib>

using namespace std;

struct Patient {
    string name;
    string age;
    string gender;
};

void addPatient(vector<Patient>& patients) {
    Patient patient;
    cout << "Enter patient name: ";
    getline(cin >> ws, patient.name);
    cout << "Enter patient age: ";
    getline(cin >> ws, patient.age);
    cout << "Enter patient gender: ";
    getline(cin >> ws, patient.gender);
    patients.push_back(patient);
    cout << "Patient added successfully!" << endl;
}

void searchPatient(const vector<Patient>& patients) {
    string name;
    cout << "Enter patient name to search: ";
    getline(cin >> ws, name);
    bool found = false;
    for (const auto& patient : patients) {
        if (patient.name == name) {
            cout << "Patient found:" << endl;
            cout << "Name: " << patient.name << endl;
            cout << "Age: " << patient.age << endl;
            cout << "Gender: " << patient.gender << endl;
            found = true;
            break;
        }
    }
    if (!found) {
        cout << "Patient not found." << endl;
    }
}

void displayAllPatients(const vector<Patient>& patients) {
    if (patients.empty()) {
        cout << "No patients found." << endl;
        return;
    }
    cout << "All patients:" << endl;
    for (const auto& patient : patients) {
        cout << "Name: " << patient.name << endl;
        cout << "Age: " << patient.age << endl;
        cout << "Gender: " << patient.gender << endl;
    }
}

void predictDisease() {
    string symptoms;
    cout << "Enter the symptoms (separated by commas): ";
    getline(cin >> ws, symptoms);
    transform(symptoms.begin(), symptoms.end(), symptoms.begin(), ::tolower);

    unordered_map<string, vector<string>> symptomDiseaseMapping = {
        {"fever", {"flu", "malaria", "dengue"}},
        {"cough", {"common cold", "bronchitis", "pneumonia"}},
        {"headache", {"migraine", "tension headache", "sinusitis"}},
        {"abdominal pain", {"appendicitis", "gastritis", "gallstones"}},
        {"rash", {"allergic reaction", "eczema", "psoriasis"}}
    };

    vector<string> predictedDiseases;
    string symptom;
    size_t start = 0, end;
    while ((end = symptoms.find(',', start)) != string::npos) {
        symptom = symptoms.substr(start, end - start);
        if (symptomDiseaseMapping.count(symptom) > 0) {
            predictedDiseases.insert(predictedDiseases.end(), symptomDiseaseMapping[symptom].begin(), symptomDiseaseMapping[symptom].end());
        }
        start = end + 1;
    }
    symptom = symptoms.substr(start);
    if (symptomDiseaseMapping.count(symptom) > 0) {
        predictedDiseases.insert(predictedDiseases.end(), symptomDiseaseMapping[symptom].begin(), symptomDiseaseMapping[symptom].end());
    }

    if (!predictedDiseases.empty()) {
        cout << "Predicted diseases:" << endl;
        sort(predictedDiseases.begin(), predictedDiseases.end());
        predictedDiseases.erase(unique(predictedDiseases.begin(), predictedDiseases.end()), predictedDiseases.end());
        for (const auto& disease : predictedDiseases) {
            cout << "- " << disease << endl;
        }
    } else {
        cout << "No diseases found for the given symptoms." << endl;
    }
}

void suggestBestDoctor(const vector<string>& predictedDiseases) {
    unordered_map<string, string> diseaseDoctorMapping = {
        {"flu", "Dr. John Smith"},
        {"malaria", "Dr. Emily Johnson"},
        {"dengue", "Dr. Michael Davis"},
        {"common cold", "Dr. Sarah Thompson"},
    };

    cout << "Suggested best doctor(s):" << endl;
    for (const auto& disease : predictedDiseases) {
        if (diseaseDoctorMapping.count(disease) > 0) {
            cout << "- " << diseaseDoctorMapping[disease] << endl;
        } else {
            cout << "- No specific doctor found for " << disease << endl;
        }
    }
}

void exitProgram() {
    cout << "Exiting the program. Goodbye!" << endl;
    exit(EXIT_SUCCESS);
}

int main() {
    vector<Patient> patients;
    while (true) {
        cout << "\nHOSPITAL AND MEDICAL FACILITIES SYSTEM" << endl;
        cout << "1. Add Patient" << endl;
        cout << "2. Search Patient" << endl;
        cout << "3. Display All Patients" << endl;
        cout << "4. Predict Disease" << endl;
        cout << "5. Suggest Best Doctor" << endl;
        cout << "6. Exit" << endl;
        cout << "Enter your choice (1-6): ";
        string choice;
        getline(cin >> ws, choice);

        if (choice == "1") {
            addPatient(patients);
        } else if (choice == "2") {
            searchPatient(patients);
        } else if (choice == "3") {
            displayAllPatients(patients);
        } else if (choice == "4") {
            predictDisease();
        } else if (choice == "5") {
            suggestBestDoctor();
        } else if (choice == "6") {
            exitProgram();
        } else {
            cout << "Invalid choice. Please try again." << endl;
        }
    }

    return 0;
}
