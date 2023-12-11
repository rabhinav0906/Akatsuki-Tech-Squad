Our system employs a decision tree in Python, utilizing the Tkinter library for the user interface. The model is trained and tested on datasets containing symptoms associated with various diseases. 
The user is presented with a series of symptoms, and their only task is to confirm their presence by clicking 'Yes.' 
If the user disagrees ('No'), another symptom is presented. Upon agreement, the model provides a preliminary diagnosis, suggesting the potential disease.

Furthermore, we've incorporated an additional dataset named "doctor_dataset," containing URLs linking to doctor profiles on Practo's website. 
Alongside the diagnosis output, the system displays a link to a relevant Practo page and the name of a doctor specializing in the identified condition. 
Clicking on this link directs the user to Practo, where detailed information about the doctor is available. Users can leverage this information to contact the doctor for further consultation based on their diagnosis.

![image](https://github.com/rabhinav0906/Doctro-Diagnosis/assets/141805520/3756da0d-cde9-4453-a9b3-f9d30f4e3095)
